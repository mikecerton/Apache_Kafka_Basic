# Apache_Kafka_Tutorial
&emsp;Apache Kafka is a distributed event streaming platform designed for high-throughput, fault-tolerant, and real-time data streaming. It consists of several key components, each playing a crucial role in data ingestion, processing, and delivery.

### Basic concepts of Kafka
<img src="https://howtodoinjava.com/wp-content/uploads/2023/06/Apache-Kafka-Architecture.png" alt="diagram" width="700" />
picture from https://howtodoinjava.com/wp-content/uploads/2023/06/Apache-Kafka-Architecture.png

#### 1. Producer:
&emsp;A Producer is a client that sends messages to Kafka topics. It determines which partition a message will be sent to, either randomly or based on a key. Producers can configure acknowledgment levels for message delivery guarantees (e.g., acknowledgment from the leader or all replicas). Producers play a key role in pushing data to Kafka, enabling real-time data ingestion.
#### 2. Consumer:
&emsp;A Consumer reads messages from Kafka topics. It pulls data from Kafka partitions, typically in a pull-based manner, allowing consumers to control when to read messages. Consumers track their progress using offsets to ensure they process messages in order and can resume from the last consumed message after a failure.
#### 3. Consumer Group:
&emsp;A Consumer Group consists of multiple consumers that work together to consume data from Kafka topics. Each consumer in the group reads from a different partition, enabling parallel processing. Kafka manages offsets for each consumer group, ensuring that each message is consumed only once, providing scalability and fault tolerance.
#### 4. Topic:
&emsp;A Topic is a logical channel in Kafka where producers send messages and consumers subscribe to consume them. Topics are partitioned for scalability and parallel processing. Each partition stores messages in order, and topics can be configured with retention policies (time- or size-based) to manage how long messages are kept.
#### 5. Partition:
&emsp;A Partition is a unit of data storage within a Kafka topic. Each partition holds an ordered, immutable log of messages and is distributed across brokers in a Kafka cluster. Partitions allow Kafka to scale horizontally, enabling parallel data processing, and each partition has one leader broker responsible for read and write operations.
#### 6. Offset:
&emsp;An Offset is a unique identifier for each message within a Kafka partition. It tracks the position of the consumer in the partition's log, ensuring that consumers can read messages in order. Consumers commit offsets to Kafka to mark the last successfully read message, allowing them to resume from that point after failures or restarts.

### Install Apache Kafka using Docker-compose
run (multiple node)
```bash
  docker-compose up -d
```
or (single node)
```bash
services:
  broker:
    image: apache/kafka:latest
    container_name: broker
    ports:
      - "9092:9092"
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_LISTENERS: PLAINTEXT://broker:9092,CONTROLLER://broker:9093
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@broker:9093
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_NUM_PARTITIONS: 3
```
install Kafka-related Python packages
```bash
  pip install kafka-python
```

### Disclaimer
 - https://kafka.apache.org/
 - https://github.com/apache/kafka
 - https://hub.docker.com/r/apache/kafka



