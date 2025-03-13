from kafka import KafkaConsumer
import json

# Create Kafka consumer 1
consumer_1 = KafkaConsumer(
    'test_101',  # Topic name
    bootstrap_servers='localhost:9092',  # Kafka broker address
    group_id='test-consumer-group',  # Consumer group ID
    key_deserializer=lambda k: k.decode('utf-8'),  # Deserialize key (string)
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize value (JSON)
)

# Create Kafka consumer 2 (same group)
consumer_2 = KafkaConsumer(
    'test_101',  # Topic name
    bootstrap_servers='localhost:9092',  # Kafka broker address
    group_id='test-consumer-group',  # Consumer group ID
    key_deserializer=lambda k: k.decode('utf-8'),  # Deserialize key (string)
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize value (JSON)
)

# Consumer 1 (part 1 of the group) consumes messages
print("Consumer 1 started and waiting for messages...")
for message in consumer_1:
    print(f"Consumer 1 - Consumed message with key: {message.key}")
    print(f"Value: {message.value}")

# Consumer 2 (part 2 of the group) consumes messages
print("Consumer 2 started and waiting for messages...")
for message in consumer_2:
    print(f"Consumer 2 - Consumed message with key: {message.key}")
    print(f"Value: {message.value}")

# Close consumers after use (this will run indefinitely unless manually stopped)
consumer_1.close()
consumer_2.close()
