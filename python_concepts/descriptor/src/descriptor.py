
class CustomizedProperty(object):

	def __init__(self, name, val):
		self.name = '_' + str(name)
		self.val = val

	def __get__(self, obj, type=None):
		print "Getting " + str(self.name)
		return self.name

	def __set__(self, obj, val):
		print "Updating " + str(self.name) + " from " + str(self.val) + " to " + str(val)

		self.val = val

	def __delete__(self, obj):
		print 'Property ' + obj.sample


class TypedProperty(object):

	def __init__(self, name, type, val):
		if not isinstance(name, str):
			raise Exception('name has to be type str')
		self.name = name
		self.val = val if val else type()
		self.type = type

	def __get__(self, obj, type=None):
		return self.val

	def __set__(self, obj, val):
		if not isinstance(val, self.type):
			raise TypeError('Must be a {}'.format(self.type))

		setattr(obj, self.name, val)

	def __delete__(self, instance):
		raise AttributeError('Can\'t delete attribute')

class TestCustomrzed(object):
	key = TypedProperty('key', int, 5)

if __name__ == '__main__':
	t = TestCustomrzed()
	t.key = '45'

