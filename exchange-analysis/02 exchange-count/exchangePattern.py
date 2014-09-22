#!/usr/bin/env python

path = './trace-web-all-exchange.txt'
#path = '/Users/yongxiang/Desktop/exchange-pattern/trace-web-all-exchange.txt'
fd = open(path,'r')
referline = fd.readline()
count = 1 # 1st line
for line in fd:
	if line != referline:
		print "%d\t%s" %(count, referline),
		count = 0 # reset the count 
		referline = line # 
	count = count + 1 # increase either if or else 
fd.close()


