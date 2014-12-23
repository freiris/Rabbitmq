#!/usr/bin/env python

''' extract non-oslo.message in a json file and return a well-format JSON '''
''' example: python extact_non_oslo_messages.py -f ./test_verify_parsed.json '''

import json
import string
from optparse import OptionParser
from pprint import pprint

def _run(filename):
	json_file = open(filename)
	data = json.load(json_file)
	json_file.close()

	for item in data:
		#withoutbody.oslo.message 
		if "oslo.message" not in item["body"].keys():
			 print(json.dumps(item, sort_keys=True, indent=4) + ",")
def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	(options, args) = parser.parse_args()
	_run(options.filename)
if __name__ == '__main__':
	main()
