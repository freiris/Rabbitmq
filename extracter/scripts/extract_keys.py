#!/usr/bin/env python

''' extract all keys in a json file and return a well-printed set '''
''' example: python extact_keys.py -f ../parse/test10.json '''

import json
from optparse import OptionParser
from pprint import pprint

def _msgparse(filename):
	json_data=open(filename)
	data = json.load(json_data)
	data_out = []
	for item in data:
		body = item["body"]
		bodydict = json.loads(body)
		msg = bodydict["oslo.message"]
		msgdict = json.loads(msg)
		bodydict["oslo.message"] = msgdict
		item["body"] = bodydict
		data_out.append(item)
	json_data.close()
	return data_out

def _extract(dict_in, keys):
	for key, value in dict_in.items():
		if isinstance(value, dict):
			_extract(value, keys)
		else:
			keys.add(key)

def _extract_keys(data_in):
	keys = set()
	for item in data_in:
		_extract(item, keys)
	return keys


def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	(options, args) = parser.parse_args()
	pprint(_extract_keys(_msgparse(options.filename)))

if __name__ == '__main__':
	main()
