#!/usr/bin/env python

''' extract union/common/each keys in a json file and return a well-printed set '''
''' example: python extact_stack_keys.py -f ../test_verify_parsed.json '''

import json
from optparse import OptionParser
from pprint import pprint


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
