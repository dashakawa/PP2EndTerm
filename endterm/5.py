#WORK QUEUES   
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'task_queue', durable = True)
#creating basic connection
#durable сохраняет все параметры


message = ' '.join(sys.argv[1:]) or "Hello World!"

#DELIVERING MESSAGE TO QUEUE
channel.basic_publish(exchange = '',
                      routing_key = 'task_queue',
                      body = message,
                      properties = pika.BasicProperties(
                          #удостовериться что очередь не потеряет все мэсседжи
                          #даже если раббит перезагрузиться
                          delivery_mode = 2
                      ))

print(" [x] Sent %r" % message)

#close the channel
channel.close()