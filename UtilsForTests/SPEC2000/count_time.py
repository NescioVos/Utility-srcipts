#!/usr/bin/python
#PYTHON_ARGCOMPLETE_OK

#Count time values for measured build runs

import sys

if len(sys.argv) <=2:
  print("Usage: time_count.py [time_log_file] [name_of_test]\n")
  sys.exit(1)

fname = sys.argv[1]
test_name = sys.argv[2]
LogFile = open(fname, 'r')
stringList = LogFile.readlines()
LogFile.close()

listOfValues = []
counter = 0
AvgVal = 0
for line in stringList:
  if len(line) < 4 or line[:4] != 'real':
    continue
  valStr = line.split()
  formatedTime = valStr[1].split('m')
  tVal = ((int)(formatedTime[0]))*60+(float)(formatedTime[1][:-1])
  AvgVal += tVal
  counter += 1

if counter == 0:
  print("error: No data")
  sys.exit(1)

AvgVal /= counter

print("Time test for test %s for %d runs = %f" % (test_name, counter, AvgVal))

    

