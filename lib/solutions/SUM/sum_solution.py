# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x == type(int) and y == type(int):
        return x + y
    else:
        return print('Cannot compute this sum - must be between integers between 0-100')