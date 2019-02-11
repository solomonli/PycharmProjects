def foo(x, *args, **kwargs):
    new_args = args + ('extra', )
    kwargs[name] = 'Alice'
    bar(x, *new_args, **kwargs)


