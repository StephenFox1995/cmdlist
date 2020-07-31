#!/usr/bin/env python 

import os

if __name__ == "__main__":
	path_env = os.environ['PATH']
	paths = path_env.split(":")
	for path in paths:
		files = os.listdir(path)
		for file in files:
			print(file)

