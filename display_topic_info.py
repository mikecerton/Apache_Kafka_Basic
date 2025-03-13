from kafka.admin import KafkaAdminClient

# Create an admin client
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:29092"  # Change to your Kafka broker
)

# Fetch topic metadata
topic_metadata = admin_client.describe_topics(admin_client.list_topics())

# Display topic information
for topic in topic_metadata:
    print(f"Topic Name: {topic['topic']}")
    print(f"Number Of Partitions: {len(topic['partitions'])}")
    for partition in topic['partitions']:
        print(f"  Partition: {partition['partition']}")
        print(f"  Leader: {partition['leader']}")
        print(f"  Replicas: {partition['replicas']}")
        print(f"  ISR: {partition['isr']}")
    print("-" * 40)

# Close the admin client
admin_client.close()


