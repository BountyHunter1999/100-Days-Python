def logging_decorator(func):
    def log(*args, **kwargs):
        name = func.__name__
        arguments = args
        output = func(*arguments)

        print(f"Function name: {name}\n"
              f"Arguments: {arguments}\n"
              f"Output: {output}")

    return log


@logging_decorator
def adder(*args):
    i = 0
    print(args)
    for i in args:
        i += i

    return i


adder(1, 2, 3, 4, 5)
