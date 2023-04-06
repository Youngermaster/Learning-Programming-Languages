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
    response = f"Pong: {body}"
    channel.basic_publish(exchange='', routing_key='pong', body=response)
    print(f"Sent response: '{response}'")


# Set up a consumer to listen for incoming messages
channel.basic_consume(
    queue='ping', on_message_callback=callback, auto_ack=True)

# Start consuming messages
print("Waiting for incoming messages...")
channel.start_consuming()
