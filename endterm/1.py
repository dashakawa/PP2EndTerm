import pika
#функция напечатает на скрин полученное сообщене
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'hello')
#связь с локальной хостом и очередью 

def callback(ch, method, properties, body):
    print(' [x] Received: {}'.format(body))
#функция которая принимает сообщения с очереди
channel.basic_consume(queue = 'hello', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
#started consuming
channel.start_consuming()