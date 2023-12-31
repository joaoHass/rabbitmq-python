import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Random queue name generated by the rabbitmq, that deletes
# when the consumer connection is closed.
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_bind(exchange='logs', queue=queue_name)

print('Waiting for logs')

def callback(ch, method, properties, body):
    print(f'* {body}')
    
    
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()