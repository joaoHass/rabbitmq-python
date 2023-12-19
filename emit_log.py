import pika, sys

connection = pika.BlockingConnection(pika.BaseConnection('localhost'))
channel = connection.channel()

# We want to send the message to as many queues possible,
# hence the fanout type.
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: It's over Anakin! I've got the high ground"
channel.basic_publish(exchange='logs', routing_key='', body=message)

print(f'[x] sent {message}')

connection.close()
