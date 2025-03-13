from kafka.admin import KafkaAdminClient, NewTopic

# Create Kafka admin client
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:29092",
    client_id="my_admin_client"
)

# Create a topic with partitions and replication factor
topic = NewTopic(
    name="test_101",
    num_partitions=3,          # Set the number of partitions
    replication_factor=3       # Set replication factor
)

# Create topic
admin_client.create_topics(new_topics=[topic], validate_only=False)

print("Topic created successfully!")