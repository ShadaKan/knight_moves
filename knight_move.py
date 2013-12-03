#!/usr/bin/python

from __future__ import division
from random import choice
import sys


start = int(sys.argv[1])
total = int(sys.argv[2])

print 'starting simulation with starting at :', start ,' and total trials: ', total


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
while(iCount < total):
 iCount = iCount + 1
 #print 'Move:',start
 start = choice(move_set[start])
 move_count[start] = move_count[start] + 1

 '''
 if(iCount % 1000 == 0):
  i = 1
  print '\n Iteration : ',iCount
  while(i <= 16):
   #print i,':',move_count[i], '\t', i,':', move_count[(i+1)], '\t', i,':', move_count[(i+2)]
   x = round(move_count[i] / total, 3)
   y = round(move_count[(i+1)] / total, 3)
   z = round(move_count[(i+2)] / total, 3)
   z2 = round(move_count[(i+3)] / total, 3)
   print move_count[i],'(',x,')', '\t', move_count[(i+1)],'(',y,')', '\t', move_count[(i+2)],'(',z,')','\t', move_count[(i+3)],'(',z2,')'
   i = i + 4
 '''


'''
print 'Simulation completed starting at :', start ,' and total trials: ', total
i = 1
string = ""
while(i <= 16):
 #print i,':',move_count[i], '\t', i,':', move_count[(i+1)], '\t', i,':', move_count[(i+2)]
 x = round(move_count[i] / total, 3)
 string = string + str(move_count[i]) + '(' + str(x) + ')' + '\t'
 i = i + 1
print string
'''


print 'Simulation completed starting at :', start ,' and total trials: ', total
i = 1
while(i <= 16):
 #print i,':',move_count[i], '\t', i,':', move_count[(i+1)], '\t', i,':', move_count[(i+2)]
 x = round(move_count[i] / total, 4)
 y = round(move_count[(i+1)] / total, 4)
 z = round(move_count[(i+2)] / total, 4)
 z2 = round(move_count[(i+3)] / total, 4)
 print move_count[i],'(',x,')', '\t', move_count[(i+1)],'(',y,')', '\t', move_count[(i+2)],'(',z,')','\t', move_count[(i+3)],'(',z2,')'
 i = i + 4
