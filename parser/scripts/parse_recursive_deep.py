#!/usr/bin/env python
'''
rabbitmq message trace parser

usage:
	$ python parse_recursive.py --filename input.json
'''

import json
from pprint import pprint
from optparse import OptionParser


__AUTHOR__ = 'yongxiang'
__VERSION__ = '1.3'

def _recursive_parse(data):
	if isinstance(data, dict): # dictionary
		for key, value in data.items():
			data[key] = _recursive_parse(value)
		return data
	elif isinstance(data, list): # list
		for i in range(len(data)):
			data[i] = _recursive_parse(data[i])
		return data
	elif isinstance(data, unicode): # unicode/string
		try: # test whether a JSON string or not
			new_data = json.loads(data)# new_data can be dict, list, unicode...
		except: # ordinary string, not in JSON format
			return data
		else: # valid JSON string
			return _recursive_parse(new_data)
	else: # other primary types, i.e. int,long,float,True, False, None 
		return data

def _msgparse(filename):
	json_file=open(filename)
	json_data = json.load(json_file)#load from file
	#for small input 
#	result = _recursive_parse(json_data)
#	pprint(result)
	for item in json_data:
		new_item = _recursive_parse(item)
#		pprint(new_item)
		print(json.dumps(new_item, sort_keys=True, indent=6) + ",")
	json_file.close()

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('', '--filename', metavar='filename', help='json file to parse')
	(options, args) = parser.parse_args()
	_msgparse(options.filename)

if __name__ == '__main__':
	main()
