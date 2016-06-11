import multiprocessing
import time

def worker(interval):
	n = 5
	while n > 0:
		print 'Time'
		time.sleep(interval)
		n -= 1