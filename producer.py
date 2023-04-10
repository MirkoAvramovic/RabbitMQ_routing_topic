import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

#this message will be received by paymentsconsumer and userconsumer
user_payments_message = "A european user paid for something"

channel.basic_publish(exchange='mytopicexchange', 
                      routing_key='user.europe.payments', body=user_payments_message)

print(f"sent message: {user_payments_message}")

#this message will be received only by analyticsconsumer
business_order_message = "A european business oredered goods"

channel.basic_publish(exchange='mytopicexchange', 
                      routing_key='business.europe.order', body=business_order_message)

print(f"sent message: {business_order_message}")

connection.close()