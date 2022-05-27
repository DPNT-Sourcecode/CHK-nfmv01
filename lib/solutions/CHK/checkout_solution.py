# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if all(isinstance(x, str) for x in skus):
        print('success')
    else:
        print('fail')

skus_1 = ['a', 'g']

checkout(skus_1)

