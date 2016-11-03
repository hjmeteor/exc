hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options="-k1,1n -k2,2" \
 -input /data/assignments/ex1/uniLarge.txt  \
 -output /user/s1637356/data/cw1/task8/output \
 -mapper mapper.py \
 -file mapper.py \
 -reducer reducer.py \
 -file reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input /user/s1637356/data/cw1/task8/output  \
 -output /user/s1637356/assignment1/task8  \
 -mapper /bin/cat \
 -file /bin/cat \
 -reducer reducer2.py \
 -file reducer2.py \
 -numReduceTasks 1