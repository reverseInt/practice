
def helper(curr, result):
	candidates = []
	for i in range(0, len(curr)):
		for j in range(1, len(curr)):
			diff = abs(curr[i] - curr[j])
			if diff > 0 and diff not in curr and diff not in candidates:
				candidates.append(diff)

	if not candidates:
		copy = list()
		copy[:] = curr
		result.append(copy)
		return

	for cand in candidates:
		curr.append(cand)
		helper(curr, result)
		curr.pop()


def find_all(nums):
	result = []
	helper(nums, result)

	return result


if __name__ == '__main__':
	print find_all([3, 21])
	print find_all([5, 20])



