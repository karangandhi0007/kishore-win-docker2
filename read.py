import json

import subprocess 


import argparse
from os import walk

def main():
	
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--file", "-f", type=str, required=True)
	args = parser.parse_args()
	
	file = args.file
	'''
	f = []
	for (dirpath, dirnames, filenames) in walk(folder):
		f.extend(filenames)
	
		for conf in filenames:
	'''
	with open(file) as json_file:
		json_data = json.load(json_file)

	for k,v in json_data.items():
		subprocess.call(['setx', k, v], shell=True)
		
	
if __name__ == '__main__':
	main()