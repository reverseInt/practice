def still_simple_decorator(func):
    print "Entering decorator: still_simple_decorator"

    def wrapper(*args, **kwargs):
        print 'Entering inner function wrapper'
        print args, kwargs
        func(*args, **kwargs)
        print 'Finished calling original function'

    return wrapper

@still_simple_decorator
def with_arguments(arg1, kwarg1):
	"""
	Some document goes here
	"""
	print "processing function with arguments"


from time import time


def time_it(func):
	def wrapper(*args, **kwargs):
		start_time = time()
		func(*args, **kwargs)
		print time() - start_time

	return wrapper


@time_it
def test_time_it():
	print 'something'

if __name__ == '__main__':
	test_time_it()