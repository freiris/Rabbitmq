#!/usr/bin/env python

''' extract union/common/each keys in a json file and return a well-printed set '''
''' example: python extact_stack_keys.py -f ../test_verify_parsed.json '''

import json
from optparse import OptionParser
from pprint import pprint


def _run(filename):
	json_file = open(filename)
	data = json.load(json_file)
	json_file.close()
	keyval_domain = dict()
	#headers
	keyval_domain['headers'] = dict()
	keyval_domain['headers']['exchange_name'] = set()
	keyval_domain['headers']['node'] = set()
	keyval_domain['headers']['properties'] = dict()
	keyval_domain['headers']['properties']['content_encoding'] = set()
	keyval_domain['headers']['properties']['content_type'] = set()
	keyval_domain['headers']['properties']['delivery_mode'] = set()
	keyval_domain['headers']['properties']['priority'] = set()
	keyval_domain['headers']['routing_keys'] = set()
	#method
	keyval_domain['method'] = dict()
	keyval_domain['method']['consumer_tag'] = set()
	keyval_domain['method']['delivery_tag'] = set()
	keyval_domain['method']['exchange'] = set()
	keyval_domain['method']['redelivered'] = set()
	keyval_domain['method']['routing_key'] = set()
	#timestamp
	keyval_domain['timestamp'] = set()
	
	for item in data:
		# headers
		keyval_domain['headers']['exchange_name'].add(item['headers']['exchange_name']) 
		keyval_domain['headers']['node'].add(item['headers']['node'])
		keyval_domain['headers']['properties']['content_encoding'].add(item['headers']['properties']['content_encoding'])
		keyval_domain['headers']['properties']['content_type'].add(item['headers']['properties']['content_type'])
		keyval_domain['headers']['properties']['delivery_mode'].add(item['headers']['properties']['delivery_mode'])
		keyval_domain['headers']['properties']['priority'].add(item['headers']['properties']['priority'])	
		keyval_domain['headers']['routing_keys'] |= set(item['headers']['routing_keys']) #union
		# method
		keyval_domain['method']['consumer_tag'].add(item['method']['consumer_tag'])
#		keyval_domain['method']['delivery_tag'].add(item['method']['delivery_tag']) # too many
		keyval_domain['method']['exchange'].add(item['method']['exchange'])
		keyval_domain['method']['redelivered'].add(item['method']['redelivered'])
		keyval_domain['method']['routing_key'].add(item['method']['routing_key'])
		#timestamp
#		keyval_domain['timestamp'].add(item['timestamp']) # too many
	#convert set to sorted list, and then JOSN serializable
	# headers
	keyval_domain['headers']['exchange_name'] = sorted(keyval_domain['headers']['exchange_name'])
	keyval_domain['headers']['node'] = sorted(keyval_domain['headers']['node'])
	keyval_domain['headers']['properties']['content_encoding'] = sorted(keyval_domain['headers']['properties']['content_encoding'])
	keyval_domain['headers']['properties']['content_type'] = sorted(keyval_domain['headers']['properties']['content_type'])
	keyval_domain['headers']['properties']['delivery_mode'] = sorted(keyval_domain['headers']['properties']['delivery_mode'])
	keyval_domain['headers']['properties']['priority'] = sorted(keyval_domain['headers']['properties']['priority'])
	keyval_domain['headers']['routing_keys'] = sorted(keyval_domain['headers']['routing_keys'])
	# method
	keyval_domain['method']['consumer_tag'] = sorted(keyval_domain['method']['consumer_tag'])
	keyval_domain['method']['delivery_tag'] = sorted(keyval_domain['method']['delivery_tag'])
	keyval_domain['method']['exchange'] = sorted(keyval_domain['method']['exchange'])
	keyval_domain['method']['redelivered'] = sorted(keyval_domain['method']['redelivered'])
	keyval_domain['method']['routing_key'] = sorted(keyval_domain['method']['routing_key'])
	# timestamp
	keyval_domain['timestamp'] = sorted(keyval_domain['timestamp'])


	pprint(keyval_domain)

'''
# extract the union keys  
def _run(filename):
        json_file = open(filename)
        data = json.load(json_file)
       	json_file.close()
	union_keys = set() #all keys 
        for item in data:
                _extract(item, union_keys, "")
#        pprint(union_keys)
	print(json.dumps(sorted(union_keys), indent=4)) #sort the set, and return a list, note set is not JSON serializable

'''

'''
# extract keys for each record
def _run(filename):
        json_file = open(filename)
        data = json.load(json_file)
        json_file.close()
        for item in data:
                keys = set() # for each record
                _extract(item, keys, "")
#                pprint(keys)
		print(json.dumps(sorted(keys), indent=4) + ",")
'''

'''
# extract the common keys
def _run(filename):
	json_file = open(filename)
	data = json.load(json_file)
	json_file.close()
	common_keys = set()
	is_first = True 
	for item in data:
		keys = set() # for each record
		_extract(item, keys, "")
		# construct the intersection
		if is_first:
			common_keys = keys
			is_first = False
		else:
			common_keys = common_keys.intersection(keys)
		# check common_keys is empty or not
		if not common_keys: # empty
			break
	if common_keys:
#		pprint(common_keys)
		print(json.dumps(sorted(common_keys), indent=4))
	else:
		print "empty common_keys"
'''

def _extract(dict_in, keys, prefix):
	prefix_bkp = prefix 
	for key, value in dict_in.items():
		# 1.update prefix
		if prefix == "":
			prefix = key
		else:
			prefix = prefix + "." + key
		# 2.determine whether to recursively extract
		if isinstance(value, dict):
			_extract(value, keys, prefix)
		else:
			keys.add(prefix) #since we have included the current key 
		# restore prefix in each loop
		prefix = prefix_bkp


def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	(options, args) = parser.parse_args()
	_run(options.filename)

if __name__ == '__main__':
	main()
