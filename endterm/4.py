#работа с очередью
import pika
import sys

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
#создавая основные конекшоны
#параметр "durable" сохраняет все месэджы в очереди
#message containing all the information iwritten after 1.py in terminal
message = ' '.join(sys.argv[1:]) or "Hello World!"
#deliver message to queque
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent {}".format(message))
#закрываем канал
connection.close()