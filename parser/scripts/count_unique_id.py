#!/usr/bin/env python

import json
from pprint import pprint
from optparse import OptionParser

def _count(filename):
	json_file = open(filename)
	json_data = json.load(json_file)
	json_file.close()
	json_data.sort() # O(nlgn) 
	count = dict()
	uid = json_data[0];
	count[uid] = 0
	for i in range(len(json_data)): # O(n)
		if json_data[i] == uid: # repeated uid
			count[uid] += 1
		else: # new uid
			uid = json_data[i]
			count[uid] = 1	
#       pprint(count)
	print("[" + json.dumps(count, indent=4) + ",")

# 	find all the max values, put in a new dictionary  
#	print max(count, key=count.get) # get the key with max value
	maxdict = dict()
	maxkey = count.iterkeys().next() # first key
#	maxvalue = count.itervalues().next() # first value
	maxvalue = count[maxkey]
	maxdict[maxkey] = maxvalue 		
	for key, value in count.items():
		'''
		if value > maxvalue:	
			maxvalue = value
			maxdict.clear() # clear previous max items 
			maxdict[key] = value # add the new max item 
		elif value == maxvalue:
			maxdict[key] = value # add a new item
		else:
			continue
		'''
		# better practice
		if value < maxvalue:
			continue
		elif value > maxvalue:
			maxvalue = value
			maxdict.clear() # clear the previous max items
		maxdict[key] = value # >= both add a new item

#	pprint(maxdict)
	print(json.dumps(maxdict, indent=4) + "]")
		

def main():
        parser = OptionParser('usage: %prog')
        parser.add_option('', '--filename', metavar='filename', help='json file to parse')
        (options, args) = parser.parse_args()
        _count(options.filename)


if __name__ == '__main__':
        main()

