#!/usr/bin/env python
'''
rabbitmq message trace parser

usage:
	$ python parse.py --infile --outfile
'''

import json
import sys
from pprint import pprint
from optparse import OptionParser


__AUTHOR__ = 'yongxiang'
__VERSION__ = '1.1'

def _recursive_parse(item):# recursively parse a unicode JSON string into a Python dictionary                                          	
	if isinstance(item, unicode):                                
                try:   
                        item_dict = json.loads(item)
	 	except ValueError,e:                                 
                        return item #string not in JSON format       
                else: #valid JSON string 
			if isinstance(item_dict, dict): #json.loads may produce a prime type, i.e. float                             
                        	for key, value in item_dict.items():         
					item_dict[key] = _recursive_parse(value)
                        return item_dict                             
        #elif array?    
        else: #not even a string                                     
                return item

def _msgparse(infile, outfile):
	json_in = open(infile)
	json_data = json.load(json_in)#load input
	if outfile == "sys.stdout":
		json_out = sys.stdout
	else:
		json_out = open(outfile, 'w')
	for item in json_data:
		body = item["body"]
		item["body"] = _recursive_parse(body)		
		print >> json_out, json.dumps(item, indent=4) + ","
	json_in.close()
	json_out.close()

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('', '--infile', metavar='infile', help='input json file')
	parser.add_option('', '--outfile', metavar='outfile', default='sys.stdout', help='output json file')
	(options, args) = parser.parse_args()
	_msgparse(options.infile, options.outfile)


if __name__ == '__main__':
	main()
