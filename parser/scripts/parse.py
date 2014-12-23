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

def _recursive_parse(item):                                          
        if isinstance(item, unicode):                                
                try:                                                 
                        item_dict = json.loads(item)                 
                except ValueError,e:                                 
                        return item #string not in JSON format       
                else: #valid JSON string                             
                        for key, value in item_dict.items():         
                                print type(key), type(value)         
                                item_dict[key] = _recursive_parse(value)
                        return item_dict                             
        #elif array?    
        else: #not even a string                                     
                return item

def _msgparse(filename):
	json_data=open(filename)
	data = json.load(json_data)#load from file
	# detailed parse option
	for item in data:
		item_dict = _recursive_parse(item)		
		pprint(item_dict)

	json_data.close()

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('', '--filename', metavar='filename', help='json file to parse')
	(options, args) = parser.parse_args()
	_msgparse(options.filename)


if __name__ == '__main__':
	main()
