import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_hello', durable=True)

channel.basic_publish(exchange='',
                      routing_key='task_hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=pika.DeliveryMode.Persistent
                      ))

print("[x] sent 'Hello World!'")
connection.close()