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

