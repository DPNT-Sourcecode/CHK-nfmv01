# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) == str:
        return print('Hello, World!')
    else:
        raise TypeError('must pass str as argument')
