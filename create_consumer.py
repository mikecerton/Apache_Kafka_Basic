from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    'test_101',  # Topic name
    bootstrap_servers='localhost:29092',  # Kafka broker address
    group_id='test-consumer-group',  # Consumer group ID
    key_deserializer=lambda k: k.decode('utf-8'),  # Deserialize key (string)
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize value (JSON)
)

# Consume messages
print("Consumer started and waiting for messages...")
for message in consumer:
    print(f"Consumed message with key: {message.key}")
    print(f"Value: {message.value}")

# Close the consumer after use (this will run indefinitely unless manually stopped)
consumer.close()
