hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D map.output.key.field.separator=' ' \
-D num.key.fields.for.partition=2 \
 -input /user/s1637356/assignment1/task4  \
 -output /user/s1637356/assignment1/task6  \
 -mapper /bin/cat \
 -file /bin/cat \
 -reducer reducer.py \
 -file reducer.py \W
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner