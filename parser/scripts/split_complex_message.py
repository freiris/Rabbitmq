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

def _split(infile, outfile1, outfile2):
	json_in = open(infile)
	json_data = json.load(json_in)#load input
	json_out1 = open(outfile1, 'w')
	json_out2 = open(outfile2, 'w')

	for item in json_data:
		if "oslo.message" in item["body"].keys():
			print >> json_out1, json.dumps(item, indent=4) + ","
		else:
			print >> json_out2, json.dumps(item, indent=4) + ","
	json_in.close()
	json_out1.close()
	json_out2.close()

def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('', '--infile', metavar='infile', help='input json file')
	parser.add_option('', '--outfile1', metavar='outfile1', default='message.json', help='message json file')
	parser.add_option('', '--outfile2', metavar='outfile2', default='non-message.json', help='non-message json file')
	(options, args) = parser.parse_args()
	_split(options.infile, options.outfile1, options.outfile2)


if __name__ == '__main__':
	main()
