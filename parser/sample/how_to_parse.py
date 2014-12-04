#!/usr/bin/env python

import json
from pprint import pprint 

level1 = json.dumps({"a1":1, "b1":2, "c1":3}, indent=4)
level2 = json.dumps({"a2":4, "b2":level1}, indent=4)
level3 = json.dumps({"a3":5, "b3":level2}, indent=4)

print level3
level3u = unicode(level3)
# how to parse level3?
'''
level3_dict = json.loads(level3)
for key3, val3 in level3_dict.items():
	if isinstance(val3, unicode):
		try:
			val3_dict = json.loads(val3)
			level3_dict[key3] = val3_dict
		except ValueError, e:
			pass #invalid json
		else:
			pass #valid json 
#	print type(key3), type(val3)
#	print key3, val3
pprint(level3_dict)
'''
print "*********************************************************\n"
#pprint level3_dict
def _recursive_parse(item):
	if isinstance(item, int):
		return item
	if isinstance(item, str) or isinstance(item, unicode):
		item = str(item)
		try:
#			print "item = %s \n" % item
			item_dict = json.loads(item)
#			print "item_dict = %s \n" % item_dict
		except ValueError,e:
			return item #string not in JSON format
		else: #valid JSON string
			for key, value in item_dict.items():
#				print type(key), type(value)
				item_dict[key] = _recursive_parse(value)
			return item_dict
	#elif array?
	else: #not even a string
		return item

level3_dict2 = _recursive_parse(level3)
pprint(level3_dict2)

