#Hello world

#подключается библиотека
import pika
#connection with localcost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#its connected now to the broker on local machine
#скуфештп ф йгуйгу
channel.queue_declare(queue = 'hello')
#Hello world sending the message
channel.basic_publish(exchange = '', routing_key = 'hello', body = 'Hello World!')

print('[x] Sent "Hello World!"')
#close the connection
connection.close()