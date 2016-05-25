from itertools import izip_longest

class BigInt(object):

	@property
	def val(self):
		return self._value[::-1]

	@val.setter
	def val(self, value):
		if not isinstance(value, str):
			raise TypeError('Input value must be string type')

		self._value = value[::-1]
	

	def __init__(self, value):
		if not isinstance(value, str):
			raise TypeError('Input value must be string type')
		self._value = value[::-1]

	def __repr__(self):
		return ''.join(self._value[::-1])

	@staticmethod
	def add_int(*args):
		for arg in args:
			if int(arg) >= 10 or int(arg) < 0:
				raise Exception('Something is wrong with add_int input')

		result = 0
		for arg in args:
			result += int(arg)

		return result/10, result % 10

	@staticmethod
	def sub_int(left, *args):
		if int(left) >= 10 or int(left) < 0:
			raise Exception('Something is wrong with add_int input')
		for arg in args:
			if int(arg) >= 10 or int(arg) < 0:
				raise Exception('Something is wrong with sub_int input')

		result = int(left)

		for arg in args:
			result -= int(arg)

		return 1 if result < 0 else 0, result + 10 if result < 0 else result


	def __add__(self, other):
		"""
		Add two positive integers
		"""
		if self.is_pos() and not other.is_pos():
			return self - (-other)

		if not self.is_pos() and other.is_pos():
			return other - (-self)

		if not self.is_pos() and not other.is_pos():
			return -(-self + (-other))

		zipped = izip_longest(self._value, other._value, fillvalue='0')

		result = []
		carry = 0
		for i, j in zipped:
			carry, ret = self.add_int(i, j, carry)
			result.append(str(ret))

		if carry > 0:
			result.append(str(carry))

		return BigInt(''.join(reversed(result)))

	def __sub__(self, other):
		"""
		always substract smaller one from bigger one
		"""
		if not self.is_pos() and not other.is_pos():
			return  -other - (-self)

		if self.is_pos() and not other.is_pos():
			return self + (-other)

		if not self.is_pos() and other.is_pos():
			return self + (-other)

		zipped = izip_longest(self._value, other._value, fillvalue='0')

		borrow = 0
		result = []
		for i, j in zipped:
			borrow, ret = self.sub_int(i, borrow, j)
			result.append(str(ret))

		if borrow != 0: # a big number - a small number will always get a positive number
			return -(other - self)

		return BigInt(''.join(reversed(result)))


	def is_pos(self):
		return '-' not in self._value

	def __neg__(self):
		result = self._value[:-1] if '-' in self._value else self._value + '-'
		return BigInt(result[::-1])


if __name__ == '__main__':
	a1 = BigInt('5321')
	a2 = BigInt('43590')
	a3 = BigInt('-9802')
	a4 = BigInt('-1')
	a5 = BigInt('0')

	print 5321 + 43590
	print a1 + a2
	print 
	print 5321 - 43590
	print a1 - a2
	print a2 - a1
	print 
	print -a3
	print 5321-9802
	print a1 + a3

	print -1 - 9802
	print a4 + a3

	print -1 + 9802
	print a4 - a3
	print
	print 1 + 9802
	print -a4 - a3
	print
	print -1 - 5321
	print a4 - a1




