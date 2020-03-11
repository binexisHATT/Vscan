#!/usr/bin/env python3

# ************************* COMMAND & CONTROL *********************************
# Author : Alexis Rodriguez
# Started : 2020-03-10
# Ended : 2020-03-

try:
  import parser
  import scanit
  import fileformat
  import hashlib
  import sys
  import os
  import json
except ImportError as err:
  print(f'Import Error: {err}')


# --------------------------------------
''' 
purpose: perform a single scan on a file
passed as an argument
param: name of the file to scan
'''
# --------------------------------------
def singleScan(filename, apikey):

	content = open(filename, 'rb').read()

	file_hash = genSha256(content)

	result = scanit.get_scan(file_hash, apikey)

	return result



# --------------------------------------
''' 
purpose: perform a mass scan on all
files contained within a single file
param: - file containing list of files
				to scan for viruses
				- VirusTotal API key
'''
# --------------------------------------
def masScan(filename, apikey, fileformat):

	# contains list of results for each
	# file that was scanned
	all_results = []
	# open file containing files to scan
	with open(filename, 'r') as allfiles:
		# this list will contain the data
		# from each scan and will be appended
		# to the all_results list
		result = []
		# loop through each file and perform
		# a scan on each one
		for file in allfiles:
				# read the files contents in bytes
				content = open(file, 'rb').read()

				# get the sha256 hash for the file
				file_hash = genSha256(content)

				# send the hash to get scanned
				result = scanit.get_scan(file_hash, apikey)

				# check if the user wanted the results
				# to be saved as a CSV file
				if fileformat == 'csv':
					result = forCsv(result)

				# check if the user wanted the results
				# to be saved as a jSON file
				elif fileformat == 'json'
					result = forJson(result)

				# check if the user wanted the results
				# to be saved as a normal text file
				elif fileformat == 'norm':
					result = forNorm(result)

				# if the user did not specify a fileformat option
				# print the raw data as json to the console
				else:
					toConsole(result)
				# append results from the scans to the all_results list
				# to format the data with respect to the format 
				# the user specified
				all_results.append(result)

	# return the list containting list of result
	return all_results



# --------------------------------------
''' 
purpose: parse data for JSON file
param: data returned from GET requests
'''
# --------------------------------------
def forJson(data):

	pass



# --------------------------------------
''' 
purpose: parse data for CSV file
param: data returned from GET requests
'''
# --------------------------------------
def forCsv(data):

	pass



# --------------------------------------
''' 
purpose: parse data for normal text file
param: data returned from GET requests
'''
# --------------------------------------
def forNorm(data):

	pass




def toConsole(data):

	print(data)



# --------------------------------------
''' 
purpose: generate sha256 hash to send
as to VirusTotal to be scanned
param: file contents read as bytes
'''
# --------------------------------------
def genSha256(file_content):

	# generating sha256 hash
	file_hash = hashlib.sha256(file_content).hexdigest()
	
	# return the hash
	return file_hash
	


def programName():
	print('''
██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗    ██╗   ██╗ ██╗    ██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║    ██║   ██║███║   ██╔═████╗
██║   ██║███████╗██║     ███████║██╔██╗ ██║    ██║   ██║╚██║   ██║██╔██║
╚██╗ ██╔╝╚════██║██║     ██╔══██║██║╚██╗██║    ╚██╗ ██╔╝ ██║   ████╔╝██║
 ╚████╔╝ ███████║╚██████╗██║  ██║██║ ╚████║     ╚████╔╝  ██║██╗╚██████╔╝
  ╚═══╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═══╝   ╚═╝╚═╝ ╚═════╝
''')



def main():
	# get arguments
  arguments = parser.ParseArgs()

  # dict containing values of arguments passed
  args_dict = {
  'single_file': arguments.single_file,
  'mass_file': arguments.mass_file,
  'csv': arguments.csv,
  'json': arguments.csv,
  'norm': arguments.norm,
  'output_file': arguments.output_file,
  'apikey': arguments.apikey
  }

  fileformat = ''

  # if file format is csv
  if args_dict['csv']:
  	fileformat = 'csv'

  # if file format is json
  elif args_dict['json']:
  	fileformat = 'json'

  # if fileformat is normal
  elif args_dict['norm']:
  	fileformat = 'norm'

  # if no file format argument was provided
  # which means display results to the 
  else:
  	fileformat = None

  """ initiating scans based on the file that was passed as an argument """

  # if the f argument was given
  if args_dict['single_file']:
  	scan_results = singleScan(args_dict['single_file'], args_dict['apikey'], fileformat)

  # if the m argument was given
  elif args_dict['mass_file']:
  	scan_results = masScan(args_dict['mass_scan'], args_dict['apikey'], fileformat)








if __name__ == '__main__':
	try:
		main()
	# handle keyboard interrupt (ctrl+?)
	except KeyboardInterrupt:
		try:
			print('The program has been interrupted.')
			sys.exit(0)
		except SystemExit:
			os._exit(0)
      