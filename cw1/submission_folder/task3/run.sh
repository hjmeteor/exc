hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input /user/s1637356/assignment1/task2 \
 -output /user/s1637356/data/cw1/task3/output \
 -mapper /bin/cat \
 -file /bin/cat \
 -reducer reducer.py \
 -file reducer.py
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input /user/s1637356/data/cw1/task3/output \
 -output /user/s1637356/assignment1/task3  \
 -mapper /bin/cat \
 -file /bin/cat \
 -reducer reducer2.py \
 -file reducer2.py \
 -numReduceTasks 1