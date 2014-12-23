#!/usr/bin/env python

''' extract all keys in a json file and return a well-printed set '''
''' example: python extact_stack_keys.py -f ../parse/test10.json '''

import json
import sys 
from optparse import OptionParser
from pprint import pprint

def _run(infile, outfile):
	json_in = open(infile)
	data = json.load(json_in)
	if outfile == "sys.stdout":
		json_out = sys.stdout
	else:
		json_out = open(outfile, 'w')
	for item in data:
		flat_item = dict()
		_flaten(item, flat_item, "")
#		pprint(flat_item)
		print >> json_out, json.dumps(flat_item, indent=4) + ","
	json_in.close()
	json_out.close()

def _flaten(dict_in, dict_out, prefix):
	for key, value in dict_in.items():
		if isinstance(value, dict):
			if prefix == "":
				prefix = key
			else:
				prefix = prefix + "." + key
			_flaten(value, dict_out, prefix)
		else:
			new_key = prefix + "." + key
			dict_out[new_key] = value
'''
we can't deal with JSON array as following:
{
k:[
	{k1:v1},
	{k1:v2}
  ]
}
=> k.k1:v2 (since k.k1:v1 will be overwritten)
'''



def main():
        parser = OptionParser('usage: %prog')
        parser.add_option('', '--infile', metavar='infile', help='input json file')
        parser.add_option('', '--outfile', metavar='outfile', default='sys.stdout', help='output json file')
        (options, args) = parser.parse_args()
	_run(options.infile, options.outfile)	
	
if __name__ == '__main__':
	main()
