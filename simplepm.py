#!/usr/bin/python

import sys, getopt
import os

def parse(filePath):
   lines = []
   file = open(filePath, 'r')
   for line in file:
      lines.append(line)
      print line
   file.close()   

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print 'simplepm.py -i <inputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'simplepm.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputPath = arg
   parse(inputPath)

if __name__ == "__main__":
   main(sys.argv[1:])
