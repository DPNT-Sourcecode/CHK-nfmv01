# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = {}
    total = []

    SKU_LIST = ['A', 'B', 'C', 'D']

    for x in skus:
        if x not in SKU_LIST:
            return -1
        else:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1

    for sku, count in counter.items():
        if sku == 'A':
            discount_amt = count // 3
            total.append((130 * discount_amt) + 50 * (count - (discount_amt * 3)))

        if sku == 'B':
            discount_amt = count // 2
            total.append((45 * discount_amt) + 30 * (count - (discount_amt * 2)))

        if sku == 'C':
            total.append(20)

        if sku == 'D':
            total.append(15)

        else:
            total.append(0)

    return sum(total)


skus = ['A', 'A', 'B', 'A', 'D', 'C', 'B', 'A', 'A']


print(checkout(skus))


'''
Some requests have failed (7/24). Here are some of them:
 - {"method":"checkout","params":["a"],"id":"CHK_R1_007"}, expected: -1, got: 0
 - {"method":"checkout","params":["-"],"id":"CHK_R1_008"}, expected: -1, got: 0
 - {"method":"checkout","params":["ABCa"],"id":"CHK_R1_009"}, expected: -1, got: 100
'''