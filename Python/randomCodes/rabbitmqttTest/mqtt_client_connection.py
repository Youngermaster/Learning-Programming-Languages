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

# Send a message to the queue
channel.basic_publish(exchange='', routing_key='ping', body='Ping!')

print("Sent message: 'Ping!'")

# Start consuming messages
print("Waiting for incoming messages...")
channel.start_consuming()
