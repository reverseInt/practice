
from pick_numbers import read_file, find_numbers

def find_max(data = read_file()):
	l = len(data[0])

	max_result = 0;
	output = ()
	for m in range(0, l):
		for n in range(0, l):
			result = find_numbers(data, m, n, float("inf"))
			print len(result)
			if result and len(result) > max_result:
				max_result = len(result)
				output = (m, n)

	print max_result, output

if __name__ == '__main__':
	print find_max()
