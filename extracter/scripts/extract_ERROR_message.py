#!/usr/bin/env python

''' extract all keys in a json file and return a well-printed set '''
''' example: python extact_stack_keys.py -f ../parse/test10.json '''

import json
import string
from optparse import OptionParser
from pprint import pprint

def _run(filename):
	json_file = open(filename)
	data = json.load(json_file)
	json_file.close()

	for item in data:
		'''
		#body.payload.error_message
		if "payload" in item["body"].keys():
			if "error_message" in item["body"]["payload"].keys():
				 print(json.dumps(item, sort_keys=True, indent=4) + ",")
		'''
		if "priority" in item["body"].keys():
			if item["body"]["priority"] == "ERROR":
				print(json.dumps(item, sort_keys=True, indent=4) + ",")
def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	(options, args) = parser.parse_args()
	_run(options.filename)

if __name__ == '__main__':
	main()
