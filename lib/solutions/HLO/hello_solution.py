

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) == str:
        return friend_name
    else:
        friend_name = str(friend_name)
        return friend_name



