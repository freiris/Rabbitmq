#!/usr/bin/env python
import pika
import sys
import simplejson
from optparse import OptionParser

__AUTHOR__ = 'ymt+yong'
__VERSION__ = '1.2'



def _run(host, port, vhost, user, password, rkey):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, virtual_host=vhost,credentials=pika.PlainCredentials(user, password)))
	channel = connection.channel()
	result = channel.queue_declare(exclusive=False, auto_delete=True)
	queue_name = result.method.queue
	channel.queue_bind(exchange='amq.rabbitmq.trace', queue=queue_name, routing_key=rkey)
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

	channel.basic_consume(callback, queue=queue_name, no_ack=True)
	channel.start_consuming() 


def main():
    parser = OptionParser('usage: %prog')
    parser.add_option('', '--host', metavar='host', default='localhost', help='rabbitmq host address, default: %default')
    parser.add_option('', '--port', metavar='port', default=5672, type='int', help='rabbitmq port, default: %default')
    parser.add_option('', '--vhost', metavar='vhost', default='/', help='rabbitmq vhost, default: %default')
    parser.add_option('', '--user', metavar='user', default='guest', help='rabbitmq user, default: %default')
    parser.add_option('', '--password', metavar='password', default='guest', help='rabbitmq password, default: %default')
    parser.add_option('', '--rkey', metavar='rkey', default='#', help='rabbitmq routing key, default: %default')
    (options, args) = parser.parse_args()
    _run(options.host, options.port, options.vhost, options.user, options.password, options.rkey)

if __name__ == '__main__':
    main()

