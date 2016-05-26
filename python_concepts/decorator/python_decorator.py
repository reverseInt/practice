import os
from functools import wraps


"""
Lets start by looking at the simplest possible case, when the function we want to decorate takes no argument
"""

###################


from functools import wraps
###############

def decorator_takes_arguments(*decorator_arguments):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print decorator_arguments
			return func(*args, **kwargs)

		return wrapper
	return decorator


@decorator_takes_arguments('something', 1)
def test_decorator_with_arguments():
	print "in test_decorator_with_arguements"


#####
class DecoratorClass(object):
	@classmethod
	def test(cls, func):
		print "in test"
		return func

	@classmethod
	def test_with_arguments(cls, *expected_args, **expected_kwargs):
		print 'in test_with_arguments', cls, expected_args, expected_kwargs

		def decorator(func):
			@wraps(func)
			def wrapper(*args, **kwrags):
				print expected_args, expected_kwargs
				return func(*args, **kwrags)
			return wrapper

		return decorator

@DecoratorClass.test
def test_class_decorator():
	print "In test_class_decorator"

@DecoratorClass.test_with_arguments(0.1, length=4)
def test_class_decorator_with_arguments():
	print 'In test_class_decorator_with_arguments'




if __name__ == '__main__':
	# with_arguments(1, kwarg1=2)
	# print with_arguments.__name__
	# print with_arguments.__doc__
	test_decorator_with_arguments()
	# test_class_decorator()
	#test_class_decorator_with_arguments()