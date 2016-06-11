
class HashHeap(object):
	class Node(object):
		def __init__(self, id, num):
			self.id = id
			self.num = num

		def __init__(self, now):
			self.id = now.id
			self.num = now.num

	def __init__(self, mode='min'):
		self.data = []
		self.mode = mode
		self.hash = dict()
		self.size = 0

	def add(self, val):
		heapq.heappush(self.data, val)

	def poll(self):
		return heapq.heappop(self.data)





if __name__ == '__main__':
	data = [1, 5, 7, 2, 0]
	hp = HashHeap(data)

	print [hp.pop() for _ in range(len(data))]

