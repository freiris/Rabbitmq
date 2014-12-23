#!/usr/bin/env python
'''
rabbitmq message trace parser

usage:
	$ python parse.py 
	<< output >>
'''

import json
from pprint import pprint
from optparse import OptionParser


__AUTHOR__ = 'yongxiang'
__VERSION__ = '1.1'


def _msgparse(filename):
	json_data=open(filename)
	data = json.load(json_data)#load from file
	# detailed parse option
	for item in data:
#		print "*********************************************************************"
#		print 'raw item:', item
#               print "---------------------------------------------------------------------"
	        body = item["body"]
		bodydict = json.loads(body)
		if "oslo.message" in bodydict.keys():
			msg = bodydict["oslo.message"]
			msgdict = json.loads(msg)
			bodydict["oslo.message"] = msgdict
		item["body"] = bodydict
		pprint(item) # works for test10.json and test12.json with unparsed body in tracer-yong.py

#		print item["body"]["oslo.message"]["_context_request_id"]
		"""
		# works for test11.json with parsed body field in tracer-new.py
		msg = item["body"]["oslo.message"]
		msgdict = json.loads(msg)#loads from string 
#		print msgdict["_unique_id"]
#		print msgdict["args"]["values"]["report_count"]
		item["body"]["oslo.message"] = msgdict
#		print item["body"]["oslo.message"]["args"]["values"]["report_count"] #can be parsed, some item has this field
		print item["headers"]["properties"]["priority"]
		print item
		"""
	json_data.close()

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('', '--filename', metavar='filename', help='json file to parse')
	(options, args) = parser.parse_args()
	_msgparse(options.filename)


if __name__ == '__main__':
	main()
