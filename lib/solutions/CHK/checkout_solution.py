# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = {}
    total = []

    available_skus = ['A', 'B', 'C', 'D']

    for x in skus:
        if x not in available_skus:
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
            total.append(20 * count)

        if sku == 'D':
            total.append(15 * count)

        else:
            total.append(0)

    return sum(total)


skus = ['A', 'A', 'B', 'A', 'D', 'C', 'B', 'A', 'A']
skus_2 = ["ABCDABCD"]


print(checkout(skus_2))

'''
Some requests have failed (3/24). Here are some of them:
 - {"method":"checkout","params":["ABCDABCD"],"id":"CHK_R1_022"}, expected: 215, got: 180
 - {"method":"checkout","params":["BABDDCAC"],"id":"CHK_R1_023"}, expected: 215, got: 180
 - {"method":"checkout","params":["ABCDCBAABCABBAAA"],"id":"CHK_R1_001"}, expected: 505, got: 465
'''
