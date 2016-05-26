def simplest_decorator(func):
	print "Entering decorator: simplest_decorator"
	return func

#@simplest_decorator
def no_arguments():
	print "processing function without arguments"



if __name__ == '__main__':
	 #no_arguments()
	 simplest_decorator(no_arguments)()
	 with_arguments(1, 2)