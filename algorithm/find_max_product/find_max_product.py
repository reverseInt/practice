"""
Given an array, find 3 numbers that their product produced max number
"""

class Solution(object):
	def find_max_product(self, nums):
		if len(nums) < 3:
			raise Excpetion('input array should have size larger or equal than 3')

		"""
		Possibilities:
		1) all +
		2) 2 - and 1 +
		~~~ below if no positive ~~~
		3) 0
		4) smallest negative either all negative or 2 + and 1 -
		"""

		pos = sorted([i for i in nums if i > 0])
		neg = sorted([i for i in nums if i < 0])
		zeros = sorted([i for i in nums if i == 0])

		assert(len(pos) + len(neg) + len(zeros) == len(nums))

		max_num = -float('inf')
		# check 1)
		
		if len(pos) >= 3:
			max_num = max(max_num, pos[-1] * pos[-2] * pos[-3])

		# check 2)
		if len(pos) >= 1 and len(neg) >= 2:
			max_num = max(max_num, pos[-1] * neg[0] * neg[1])

		# check 3)
		if zeros:
			max_num = max(max_num, 0)

		# check 4)
		if len(pos) >= 2 and len(neg) >= 1:
			max_num = max(max_num, pos[0] * pos[1] * neg[-1])

		if len(neg) >= 3:
			max_num = max(max_num, neg[-1] * neg[-2] * neg[-3])

		return max_num



if __name__ == '__main__':
	s = Solution()

	nums = [1, 2, 3, 6, 9]
	print s.find_max_product(nums)
	nums = [-10, 0, -2, -20, 0, 0]
	print s.find_max_product(nums)
	nums = [1, -1, -2]
	print s.find_max_product(nums)
	nums = [-20, -1, -2, -100, -2]
	print s.find_max_product(nums)

