import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
#declare the queque connect to loca host make queque durable
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

##rabbitmq wont give the message if its busy
channel.basic_qos(prefetch_count=1)
#consume function
channel.basic_consume(queue='task_queue', on_message_callback=callback)
#start consuming
channel.start_consuming()