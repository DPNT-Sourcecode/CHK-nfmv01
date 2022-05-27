# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) == str:
        return print('Hello, World!')
    else:
        return print(str(friend_name))

hello("MR X")