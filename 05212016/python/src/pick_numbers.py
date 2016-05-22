import os
import argparse
from collections import Counter


def parse():
	parser = argparse.ArgumentParser()

	parser.add_argument('-m', type=int, default=2)
	parser.add_argument('-n', type=int, default=2)
	parser.add_argument('-p', type=int, default=5)

	args = parser.parse_args()
	return args

def read_file(filename = 'output/result.txt'):

	data = []
	with open(filename, 'r') as f:
		for line in f:
			data.append(map(lambda x: int(x), line.split(',')))

	return data


def check_neighbors(data, i, j):
	def check_sign(p, q):
		try:
			return data[p][q] > 0
		except:
			return None

	result = None
	for p in (-1, 1):
		for q in (-1, 1):
			if result is None:
				result = check_sign(i + p, j + q)
			else:
				if result != check_sign(i + p, j + 1):
					return False
	return True


def find_numbers(data, m, n, p):
	colum_stats = [Counter([row[col] for row in data]) for col in range(0, len(data[0]))]
	result = []
	for i in range(1, len(data) - 1):
		for j in range(1, len(data[i]) - 1):
			if check_neighbors(data, i, j):
				continue
			if data[i][j] > 0:
				if colum_stats[m][data[i][j]] < 50:
					continue

			if data[i][j] < 0:
				if colum_stats[n][data[i][j]] >= 10:
					continue

			if data[i][j] <= 50 and data[i][j] >= -50:
				continue

			if len(result) > p:
				break;

			result.append(data[i][j])

	return result


if __name__ == '__main__':
	data = read_file()
	args = parse()
	m, n, p = args.m, args.n, args.p
	print m, n 
	result = find_numbers(data, m, n, float('inf'))
	print (len(result))
	#print result if result else 'Not Exist'

