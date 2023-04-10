import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"Payments Service - received new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

#routing_key of producer must finish with the word "payments"
channel.queue_bind(exchange='mytopicexchange', queue=queue.method.queue, 
                   routing_key='#.payments')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, 
                      on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()