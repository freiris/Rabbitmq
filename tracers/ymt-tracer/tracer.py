#!/usr/bin/env python
import pika
import sys
import simplejson

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.1.0.2', port=5672, virtual_host='/nova', credentials=pika.PlainCredentials('guest', 'test')))
channel = connection.channel()

result = channel.queue_declare(exclusive=False, auto_delete=True)
queue_name = result.method.queue

if len(sys.argv) <= 1:
	rkey = '#'
else:
	rkey = sys.argv[1]
channel.queue_bind(exchange='amq.rabbitmq.trace', queue=queue_name, routing_key=rkey)
#channel.queue_bind(exchange='amq.rabbitmq.log', queue=queue_name, routing_key='#')
print ' [*] Msg Tracer with routing key:', rkey, '. To exit press CTRL+C'

def callback(ch, method, properties, body):
	ret = {}
#	ret['routing_key'] = method.routing_key
	ret["headers"] = properties.headers
	try:
		ret["body"] = simplejson.loads(body.replace("'","\"")) #?doesn't work?
	except Exception, e:
		with open('failure11.txt', 'w') as fail:
			fail.write(str(ret) + '\n')
			ret["body"] = body
	print ret

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
