#!/bin/bash
hdfs dfs -rm -r /user/$USER/temperatures/nocombine
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapreduce.job.reduces=2 -input /user/$USER/temperatures/input.txt -output /user/$USER/temperatures/nocombine -mapper cat -reducer reduce.py -file reduce.py
