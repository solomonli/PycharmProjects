def my_decorator(func):
	def wrapper():
		print('Before the func is called')
		func()
		print('After the func is called')
	return wrapper


# @my_decorator		# it's just a way to say "say_whee = my_decorator(say_whee)"
def say_whee():
	print('Whee!')


def do_twice(func):
	def wrapper():
		func()
		func()
	return wrapper


# @do_twice		# it's just a way to say "say_whee = do_twice(say_whee)"
def say_whee():
	print('Whee!')


def perf_timer(func):

	def wrapper(*args, **kwargs):

		import datetime

		tik = datetime.datetime.now()

		function_result = func(*args, **kwargs)

		tok = datetime.datetime.now()

		print(f'Elapsed time: {tok - tik}')

		return function_result

	return wrapper


# @perf_timer		# it's just a way to say "say_whee = perf_timer(say_whee)"
def say_whee():
	print('Whee!')


# say_whee()
