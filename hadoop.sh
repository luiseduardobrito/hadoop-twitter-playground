#!/bin/bash

set -e
set -o pipefail

rm -rf "$(pwd)/.tmp/tweets.txt" &> /dev/null || true
mkdir "$(pwd)/.tmp"  &> /dev/null || true

. envs.sh
./crawler.py "$1" &> "$(pwd)/.tmp/tweets.txt";

# TODO
export HADOOP_HOME="/home/ec2012/ra138760/hadoop-2.7.2";

echo "Removing previous output files from HDFS..."
"$HADOOP_HOME/bin/hadoop dfs" -rm -r /user/hduser/twitter/output.txt;

echo "Copying input tweets to HDFS..."
"$HADOOP_HOME/bin/hadoop" dfs -copyFromLocal -f "$(pwd)/.tmp/tweets.txt" "/user/hduser/twitter";

echo "Copying mapper script to HDFS...";
"$HADOOP_HOME/bin/hadoop" dfs -copyFromLocal -f "$(pwd)/mapper.py" "/user/hduser/twitter";

echo "Copying reducer script to HDFS...";
"$HADOOP_HOME/bin/hadoop" dfs -copyFromLocal -f "$(pwd)/reducer.py" "/user/hduser/twitter";

echo "Copying reporter script to HDFS...";
"$HADOOP_HOME/bin/hadoop" dfs -copyFromLocal -f "$(pwd)/reporter.py" "/user/hduser/twitter";

echo "Running map reducer step..."
"$HADOOP_HOME/bin/hadoop" jar "$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar" \
  -file "$(pwd)/mapper.py"      -mapper "$(pwd)/mapper.py"   \
  -file "$(pwd)/reducer.py"     -reducer "$(pwd)/reducer.py" \
  -input "/user/hduser/twitter/tweets.txt"    -output "/user/hduser/twitter/output.txt"
