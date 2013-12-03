#!/usr/bin/python
from __future__ import division
from random import choice
import os
import sys

def print_state(move_count, total):
	i = 1
	string = ""
	while(i <= 16):
		#print i,':',move_count[i], '\t', i,':', move_count[(i+1)], '\t', i,':', move_count[(i+2)]
		x = round(move_count[i] / total, 4)
		#string = string + str(move_count[i]) + '\t' + str(x) + '\t'
		string = string + str(x) + '\t'
		i = i + 1
	print string

def get_values(start, total):


	move_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0 }

	move_set = {
		1 : [7, 10],
		2 : [8, 9, 11],
		3 : [5, 10, 12],
		4 : [6, 11],
		5 : [3, 11, 14],
		6 : [4, 12, 13, 15],
		7 : [1, 9, 14, 16],
		8 : [2, 10, 15],
		9 : [2, 7, 15],
		10 : [1, 3, 8, 16],
		11 : [2, 4, 5, 13],
		12 : [3, 6, 14],
		13 : [6, 11],
		14 : [5, 7, 12],
		15 : [6, 8, 9],
		16 : [7, 10]
	}


	iCount = 0
	header = ""
	for j in range(1,17) :
		#header = header + "Cell"+str(j) + '\t' + 'P(' + str(j) +')'+'\t'
		header = header + 'P(' + str(j) +')'+'\t'
	print header

	while(iCount < total):
		iCount = iCount + 1
		move_count[start] = move_count[start] + 1
		start = choice(move_set[start])
		
		if( (iCount % 10) == 0):
			print_state(move_count, iCount)


st = choice(range(1,17))
print 'starting at :',st
get_values(st, 99999)

