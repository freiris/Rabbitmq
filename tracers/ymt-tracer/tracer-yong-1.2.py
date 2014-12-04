#!/usr/bin/env python
import pika
import sys
import json
from optparse import OptionParser

__AUTHOR__ = 'ymt+yong'
__VERSION__ = '1.2'



def _run(host, port, vhost, user, password, rkey):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, virtual_host=vhost,credentials=pika.PlainCredentials(user, password)))
	channel = connection.channel()
	result = channel.queue_declare(exclusive=False, auto_delete=True)
	queue_name = result.method.queue
	channel.queue_bind(exchange='amq.rabbitmq.trace', queue=queue_name, routing_key=rkey)

	def callback(ch, method, properties, body):
		ret = {}
		ret["headers"] = properties.headers
#		ret["method"] = method
#		ret["properties"] = properties
                ret["body"] = body
#		print(json.dumps(ret)+',') # print in a compact way 
		print(json.dumps(ret, indent=4)+',')# dumps can be easily reloaded as json format;comma(,) is used to seperate each json object, and form a json array when surrounded with [].Note: delete the last one comma.
	"""	print "***************************method**********************************"
                print method
                print "***************************properties**********************************"
                print properties
                print "***************************body**********************************"
                print body
                print "#########################################################################"
	"""
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

