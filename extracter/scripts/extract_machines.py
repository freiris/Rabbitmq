#!/usr/bin/env python

''' extract all msgs by machines '''
''' example: python extact_machines.py -f ../parse/test10.json '''

import json
from optparse import OptionParser
from pprint import pprint

def _msgparse(filename):
	json_data=open(filename)
	data = json.load(json_data)
	data_out = dict()
	for item in data:
		body = item["body"]
		bodydict = json.loads(body)
		msg = bodydict["oslo.message"]
		msgdict = json.loads(msg)
		bodydict["oslo.message"] = msgdict
		item["body"] = bodydict
		header = item["headers"]
		node = header['node']
		if data_out.has_key(node):
			data_out[node].append(item)
		else:
			data_out[node] = [item]
		
	json_data.close()
	return data_out

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	(options, args) = parser.parse_args()
	pprint(_msgparse(options.filename))

if __name__ == '__main__':
	main()
