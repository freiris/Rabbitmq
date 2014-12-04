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
# recursively parse a unicode JSON string into a Python dictionary                                          	
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

def _msgparse(filename):
	json_file=open(filename)
	json_data = json.load(json_file)#load from file
	# detailed parse option
	for item in json_data:
		body = item["body"]
		item["body"] = _recursive_parse(body)		
		pprint(item)
		print "," # to seperate each item
		'''
		itemu = json.dumps(item,ensure_ascii=False, encoding='utf-8')
		item_dict = _recursive_parse(itemu) #parse from the outer-most
		pprint(item_dict)
		'''
	json_file.close()

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('', '--filename', metavar='filename', help='json file to parse')
	(options, args) = parser.parse_args()
	_msgparse(options.filename)


if __name__ == '__main__':
	main()
