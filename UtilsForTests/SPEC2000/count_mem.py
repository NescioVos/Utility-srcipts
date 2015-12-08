#!/usr/bin/python
#PYTHON_ARGCOMPLETE_OK

# Memory utilization visualiser script.
# Visualise your vmstat output by this script.
#
# How to run your program with vmstat:
# vmstat 1 > memusage.log & ./my_program ; sleep 2

# author: unerkannt@ispras.ru



#from pylab import *
import sys

if len(sys.argv) < 4 or sys.argv[1] == "-h":
  print("Memory utilization visualizer script usage:\n")
  print("    vmstat_visualizer.py FILE [FREQUENCY] [TEST NAME]\n")
  print("FILE:        file where vmstat output was logged.")
  print("FREQUENCY:   frequency of vmstat run in seconds. 2 by default.")
  print("OUTPUT FILE: image file of PNG format where plot will be saved. 'memUtil.png' by default\n")
  print("Note, you have to run your program with vmstat tool before and log it to file!")
  print("  example:    $ vmstat 1 > memusage.log & ./my_program ; sleep 2")
  sys.exit(1)

name = sys.argv[1]
freq = 2
#outname='memUtil.png'


freq = (int)(sys.argv[2])
testName = sys.argv[3]

#print("Plot vmstat log '%s' with frequency %d to the image file '%s'." % (name, freq, outname) )

MUFile = open(name, 'r')
stringList = MUFile.readlines()
MUFile.close()

firstValueStr = stringList[2].split()
firstValue = (int)(firstValueStr[3])
listOfValues = []

MAX = 0
AVG = 0
SZ = 0
for line in stringList:
  if line[0] == 'p' or line[1] == 'r':
    continue
  valStr = line.split()
  val = firstValue - (int)(valStr[3])
  if val > MAX:
    MAX = val
  AVG += val
  SZ += 1
#  listOfValues.append(val)
if SZ == 0:
  print("Error: No data")
  sys.exit(1)

AVG /= SZ

print("Test memory usage for test %s:\n MAX = %d   AVG = %f" % (testName, MAX, AVG))

#listLen2 = len(listOfValues)
#plotX = [ x*freq for x in range(0, listLen2) ]

#plot(plotX, listOfValues, 'b-')
#savefig(outname)
#show()
