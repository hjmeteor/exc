#!/bin/bash
hdfs dfs -rm -r /user/$USER/temperatures/combine
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapreduce.job.reduces=2 -input /user/$USER/temperatures/input.txt -output /user/$USER/temperatures/combine -mapper map.py -combiner combine.py -reducer reduce.py -file map.py -file combine.py -file reduce.py
