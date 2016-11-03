hdfs dfs -copyToLocal /user/s1637356/assignment1/task2  ~/exc/cw1/task2/output/
hdfs dfs -rm -r /user/s1637356/assignment1/task2 
hdfs dfs -copyToLocal /user/s1637356/assignment1/task1 ~/exc/cw1/task1/output/ 
cat ~/exc/cw1/task1/output/task1/part-00000 | head -20 > output.out
