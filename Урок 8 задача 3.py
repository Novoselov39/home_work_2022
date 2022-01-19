from functools import wraps

def type_logger(callback):
    @wraps(callback)
    def wraper(*args):
        result = callback.__name__ + '('
        for a in args:
            result = result + str(a) + ': ' + str(type(a)) + ', '
        a = result.strip(', ')+')'
        print(a)
        return callback(*args)
    return wraper


@type_logger
def calc_cube(x,y):
    return x * y

print(calc_cube(3, 4))

