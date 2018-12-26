https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html

Download and extract Zookeeper http://mirrors.estointernet.in/apache/zookeeper/

Download and kalfka http://mirrors.estointernet.in/apache/kafka/2.1.0/kafka-2.1.0-src.tgz

set up JAVA_HOME and java in path env variable

set up ZOOKEEPER_HOME and in path env varible

Rename file “zoo_sample.cfg” to “zoo.cfg”

Find and edit dataDir=/tmp/zookeeper to :\zookeeper-3.4.7\data

Run Zookeeper by opening a new cmd and type zkserver

Find and edit the line log.dirs=/tmp/kafka-logs” to “log.dir= C:\kafka_2.11-0.9.0.0\kafka-logs in C:\kafka_2.11-0.9.0.0\config\server.properties

Running a Kafka Server: go to kalfka home dir and run .\bin\windows\kafka-server-start.bat .\config\server.properties command in cmd


Creating Topics : kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

Creating a Producer: kafka-console-producer.bat --broker-list localhost:9092 --topic test

Creating a Consumer: kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test


Now type anything in the producer command prompt and press Enter, and you should be able to see the message in the other consumer command prompt.


List Topics: kafka-topics.bat --list --zookeeper localhost:2181  
Describe Topic: kafka-topics.bat --describe --zookeeper localhost:2181 --topic [Topic Name]
Read messages from the beginning: kafka-console-consumer.bat --zookeeper localhost:2181 --topic [Topic Name] --from-beginning
Delete Topic: kafka-run-class.bat kafka.admin.TopicCommand --delete --topic [topic_to_delete] --zookeeper localhost:2181
