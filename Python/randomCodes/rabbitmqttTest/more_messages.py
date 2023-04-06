import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

# Declare the 'ping' queue
channel.queue_declare(queue='ping')

# Declare the 'pong' queue
channel.queue_declare(queue='pong')

# Define a callback function to handle incoming messages


def callback(ch, method, properties, body):
    print("Received message: %r" % body)


# Set up a consumer to listen for incoming messages
channel.basic_consume(
    queue='pong', on_message_callback=callback, auto_ack=True)

# Send 3 messages to the queue
for i in range(3):
    message = f"Message {i+1}"
    channel.basic_publish(exchange='', routing_key='ping', body=message)
    print(f"Sent message: '{message}'")

# Start consuming messages
print("Waiting for incoming messages...")
channel.start_consuming()
