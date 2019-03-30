import datetime, functools, time


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# @my_decorator		# it's just a way to say "say_whee = my_decorator(say_whee)"
def say_whee():
	print('Whee!')


def do_twice(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)		# the function wrapper should return nothing
	return wrapper


# @do_twice		# it's just a way to say "say_whee = do_twice(say_whee)"
def say_whee():
	print('Whee!')


def perf_timer(func):

	def wrapper(*args, **kwargs):

		# import datetime

		tik = datetime.datetime.now()

		function_result = func(*args, **kwargs)

		tok = datetime.datetime.now()

		print(f'Elapsed time: {tok - tik}')

		return function_result

	return wrapper


def timer(func):

	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):

		start_time = time.perf_counter()

		value = func(*args, **kwargs)

		end_time = time.perf_counter()

		run_time = end_time - start_time

		print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

		return value

	return wrapper_timer

# time.perf_counter()
"""
Return the value (in fractional seconds) of a performance counter, i.e. 
a clock with the highest available resolution to measure a short duration. 
It does include time elapsed during sleep and is system-wide. 
The reference point of the returned value is undefined, 
so that only the difference between the results of consecutive calls is valid.
"""