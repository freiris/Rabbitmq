#!/usr/bin/env python
'''
note: put the keylist in a string 
'''

import ast
import json
import string
from optparse import OptionParser
from pprint import pprint

def _run(filename, keylist):
	json_file = open(filename)
	data = json.load(json_file)
	json_file.close()

	keylist = ast.literal_eval(keylist)
	
	group_by = dict()
	for item in data:
		val = item
		for key in keylist:
			try: 
				val = val[key]
			except:
				print key + ' unrecognized'
				val = 'not_group'	
				break
		try:
			group_by[val].append(item) # add to existing list
		except:
			group_by[val] = list() # allocate a list for the first item
			group_by[val].append(item)

#	pprint(group_by)
	for key in group_by.keys():
		print '--------------------------------------------------------------------',
		print "check_key",
		print '--------------------------------------------------------------------'
#		print key		
#		print type(group_by[key])

		for item in group_by[key]:
			print(json.dumps(item, sort_keys=True, indent=4) + ",")

	
def main():
	parser = OptionParser('usage: %prog')
	parser.add_option('-f', '--filename', metavar='filename')
	parser.add_option('-k', '--keylist', metavar='keylist')
	(options, args) = parser.parse_args()
	_run(options.filename, options.keylist)

if __name__ == '__main__':
	main()
