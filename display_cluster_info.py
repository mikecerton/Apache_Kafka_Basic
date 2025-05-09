from kafka.admin import KafkaAdminClient

# Create a KafkaAdminClient instance
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:49092",  # Kafka broker address
    client_id="my_admin_client"  # Client ID for identification
)

cluster_info = admin_client.describe_cluster()
print("Cluster ID:", cluster_info.get("cluster_id"))
print("Current Controller Broker ID:", cluster_info.get("controller_id"))
print("Nodes:")

for node in cluster_info.get("brokers", []):
    print(f"  - Node ID: {node['node_id']}, Host: {node['host']}, Port: {node['port']}")
