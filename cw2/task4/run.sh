hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options="-k1,1n -k2,2n" \
 -input /data/assignments/ex2/part2/stackLarge.txt \
 -output /user/s1637356/data/cw2/task4/output \
 -mapper mapper.py \
 -file mapper.py \
 -reducer reducer.py \
 -file reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D stream.num.map.output.key.fields=2 \
 -D mapreduce.partition.keypartitioner.options=-k1,1 \
 -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2n" \
 -input /user/s1637356/data/cw2/task4/output \
 -output /user/s1637356/assignment2/task4 \
 -mapper /bin/cat \
 -file /bin/cat \
 -combiner combiner.py \
 -file combiner.py \
 -reducer reducer2.py \
 -file reducer2.py \
 -numReduceTasks 1 \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
