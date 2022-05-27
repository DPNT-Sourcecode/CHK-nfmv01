# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if all(isinstance(x, str) for x in skus):
        print('success')
    else:
        return -1


skus = ['a', 'g', 1]

checkout(skus)

