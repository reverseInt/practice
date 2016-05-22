# -*- coding: utf-8 -*-
"""
1. write a program that write to a file: each line has 5 fields, fields are separate by comma, each field is a random int [-9999, 9999], there are total of 5k lines
2. Write a program that takes 3 command line arguments m, n, p, the program will print out a list of up to p numbers from the previously generated file, each number satisfy the following:
The up/down/left/right neighbors are either all positive or all negative, 0 is neither positive nor negative
Must appear at least 50 times in column m if it is positive
Can’t appear more than 10 times in column n if it is negative
The number can't be in [-50, 50]
If there are more than p numbers satisfying these, only print the first p numbers, print “not exist” if there are no such numbers
3. Write a program that finds out what m and n values will maximize the number of unique numbers meeting requirements a)-d)
"""

import random
import os

def write_to_file(total_lines):
	if not os.path.isdir('output'):
		os.mkdir('output')

	with open('output/result.txt', 'w') as f:
		for index in range(0, total_lines):
			line = ','.join([str(random.randint(-9999, 9999)) for _ in range(0, 5)])
			f.write(line + '\n')	

if __name__ == '__main__':
	write_to_file(5000)
		

