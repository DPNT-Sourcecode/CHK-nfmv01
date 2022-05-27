# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if 0 <= x <= 100 and 0 <= y <= 100 and type(x) == int and type(y) == int:
        return x + y
    else:
        raise ValueError('x and y must be integers between 0 and 100')