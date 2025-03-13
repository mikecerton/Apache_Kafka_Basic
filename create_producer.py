from kafka import KafkaProducer
from faker import Faker
import json

"""
Explanation:
Key Serialization: Using str.encode directly converts the key (a string) into bytes, which is simpler and more concise.
Value Serialization: The value is serialized into a JSON string and then encoded in UTF-8, which remains the same as before.
"""
# Initialize Faker instance
fake = Faker()

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:29092",  # Kafka broker address
    key_serializer=lambda k: str(k).encode('utf-8'),  # Serialize key as a string encoded in UTF-8
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize value as JSON
)

# Generate fake data
fake_data = {
    "name": fake.name(),
    "address": fake.address(),
    "email": fake.email(),
    "phone_number": fake.phone_number(),
    "company": fake.company(),
    "job": fake.job(),
}

# Generate a key (you can use a unique identifier, such as user ID, or just a random number)
key = fake.uuid4()  # Generates a unique UUID for each message

# Send fake data to Kafka topic with key
producer.send('test_101', key=key, value=fake_data)

# Ensure the message is sent
producer.flush()

# Close the producer after use
producer.close()

print(f"Fake data sent with key {key} successfully!")
