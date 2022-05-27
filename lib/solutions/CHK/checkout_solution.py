# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # prices = []
    if all(isinstance(x, str) for x in skus):
        for x in skus:
            print(x.price)
    else:
        return -1

# skus_1 = ['a', 'g']
#
# checkout(skus_1)