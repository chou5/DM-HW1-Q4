#!/usr/bin/python

import sys
import simplejson
import numpy as np
import random
from itertools import combinations

def cal_rk(n, iter):
  rk = []
  for k in range(1,101):
    average = []  
    for i in range(iter):   
	  distance = []
	  setOfPoint = []
	  for i in range(n):
	    point = []
	    for i in range(k):
	      point.append(random.uniform(0,1))
	    setOfPoint.append(point)
	  point_list = np.array(setOfPoint) 
	  for A,B in combinations(point_list, 2):
	    distance.append(np.sqrt(np.sum((A-B)**2)))
	  average.append(np.log10((max(distance) - min(distance)) / min(distance)))
    rk.append(np.mean(average))
  return rk
  

if __name__=="__main__":
  if len(sys.argv) != 5:
	print "USAGE: python HW1_q4.py -n [number of three different value(100/1000/10000)] -i [iterator]"
	exit(-1)
  if sys.argv[1] == "-n":
	num = sys.argv[2]
  else:
	print "USAGE: python HW1_q4.py -n [number of three different value(100/1000/10000)] -i [iterator]"
	exit(-1)
  if sys.argv[3] == "-i":
    i = sys.argv[4]
  else:
	print "USAGE: python HW1_q4.py -n [number of three different value(100/1000/10000)] -i [iterator]"
	exit(-1)

  n = int(num)
  iter = int(i)
  
  if n == 100:
	rk = cal_rk(n, iter)
	print "Read output100.txt file!"
	f = open('output100.txt', 'w')
	simplejson.dump(rk,f)
	f.close()
  elif n == 1000:
	rk = cal_rk(n, iter)
	print "Read output1000.txt file!"
	f = open('output1000.txt', 'w')
	simplejson.dump(rk,f)
	f.close()
  elif n == 10000:
	rk = cal_rk(n, iter)
	print "Read output10000.txt file!"
	f = open('output10000.txt', 'w')
	simplejson.dump(rk,f)
	f.close()
  else:
    print "N should either 100, 1000 or 10000!"
