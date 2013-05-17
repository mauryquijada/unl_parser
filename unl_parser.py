# unl_parser.py

# Author: Maury Quijada
# Created on May 10, 2013

# This program takes in a .unl file as outputted from an Informix UNLOAD
# database command and converts the data into a CSV file at a specified location.
# This programs can run with a command line parameter "-d" that allows the
# user to specify the delimiter used in the .unl file being passed.

import argparse
import csv

def main():
	# Accept given arguments using argparse in Python's std. library.
	parser = argparse.ArgumentParser(prog='unl_parser', \
		description='Converts a .unl file as outputted from Informix and' \
		' converts the data into a CSV file.')
	parser.add_argument('-d', default='|', \
		help="specify the delimiter used in the .unl file.")	
	parser.add_argument('givenFile', help="specify the .unl file to process")
	parser.add_argument('outputFile', help="specify the .csv file to output to")
	args =  parser.parse_args()

	# Open the supplied file and create the CSV writer.
	givenFile = open(args.givenFile, 'r')
	csvFile = csv.writer(open(args.outputFile, 'w'), delimiter=',', \
		quoting=csv.QUOTE_ALL)

	# Eliminate new lines that are within the delimiter.
	inputFile = givenFile.read()

	# Take the given file and convert it line-by-line into a CSV.
	for line in inputFile.split(args.d + "\r"):
		# Add the delimiter to the end of the line (removed in above step).
		line += args.d

		# Create an array representing each column and eliminate whitespace.
		splitLine = line.split(args.d)
		splitLine = ["" if val.isspace() else val.strip() for val in splitLine]
		
		# Remove the carriage return.
		splitLine.pop()

		# Finally, add to the csvFile.
		csvFile.writerow(splitLine)

if __name__ == "__main__":
	main()