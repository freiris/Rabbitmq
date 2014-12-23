#!/usr/bin/env python

''' extract failure+INFO+ERROR in a json file and return a well-format JSON '''
''' example: python extact_failure_INFO_ERROR_message.py -f ./test_verify_parsed.json '''

import json
import string
from optparse import OptionParser
from pprint import pprint

def _run(filename):
	json_file = open(filename)
	data = json.load(json_file)
	json_file.close()
	for item in data:
		# INFO and ERROR messages are without oslo.message  
		if "oslo.message" not in item["body"].keys():
			if "_context_user_identity" in item["body"].keys():
				if item["body"]["_context_user_id"] == "ed9bb20ad8a94d319a62e23a0d0f094a" and \
					item["body"]["_context_project_id"] == "9d3f2e98e25547998547a937642d06c6": # find correlated ERROR+INFO pair					
					print(json.dumps(item, sort_keys=True, indent=4) + ",") 
					
		# failure message
		'''	
		if "oslo.message" in item["body"].keys():
                        if "failure" in item["body"]["oslo.message"].keys():
                                if item["body"]["oslo.message"]["failure"] is not None:
					 print(json.dumps(item, sort_keys=True, indent=4) + ",")
		'''
def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	(options, args) = parser.parse_args()
	_run(options.filename)

if __name__ == '__main__':
	main()