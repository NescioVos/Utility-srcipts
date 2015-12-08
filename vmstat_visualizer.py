#!/usr/bin/python
#PYTHON_ARGCOMPLETE_OK

# Memory utilization visualiser script.
# Visualise your vmstat output by this script.
#
# How to run your program with vmstat:
# vmstat 1 > memusage.log & ./my_program ; sleep 2

# author: unerkannt@ispras.ru



from pylab import *
import sys

if len(sys.argv) <= 1 or sys.argv[1] == "-h":
  print("Memory utilization visualizer script usage:\n")
  print("    vmstat_visualizer.py FILE [FREQUENCY] [OUTPUT FILE]\n")
  print("FILE:        file where vmstat output was logged.")
  print("FREQUENCY:   frequency of vmstat run in seconds. 2 by default.")
  print("OUTPUT FILE: image file of PNG format where plot will be saved. 'memUtil.png' by default\n")
  print("Note, you have to run your program with vmstat tool before and log it to file!")
  print("  example:    $ vmstat 1 > memusage.log & ./my_program ; sleep 2")
  sys.exit(1)

name = sys.argv[1]
freq = 2
outname='memUtil.png'

if len(sys.argv) > 2:
  freq = (int)(sys.argv[2])
  if len(sys.argv) > 3:
    outname = sys.argv[3]

print("Plot vmstat log '%s' with frequency %d to the image file '%s'." % (name, freq, outname) )

MUFile = open(name, 'r')
stringList = MUFile.readlines()
MUFile.close()

firstValueStr = stringList[2].split()
firstValue = (int)(firstValueStr[3])
listOfValues = []

for line in stringList:
  if line[0] == 'p' or line[1] == 'r':
    continue
  valStr = line.split()
  val = firstValue - (int)(valStr[3])
  listOfValues.append(val)

listLen2 = len(listOfValues)
plotX = [ x*freq for x in range(0, listLen2) ]

plot(plotX, listOfValues, 'b-')
savefig(outname)
show()
