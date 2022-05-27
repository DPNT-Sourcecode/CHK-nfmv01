# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = {}
    total = []

    if all(isinstance(x, str) for x in skus):
        for x in skus:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1

    else:
        return -1

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