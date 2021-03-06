# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = {}
    total = []

    available_skus = ['A', 'B', 'C', 'D', 'E', 'F']

    for x in skus:
        if x not in available_skus:
            return -1
        else:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1

    if 'A' in counter.keys():
        count = counter['A']
        discount_1 = 5
        discount_2 = 3

        remainder_1 = count // discount_1
        total_1 = 200 * remainder_1

        new_count = count - (remainder_1 * discount_1)
        remainder_2 = new_count // discount_2
        total_2 = 130 * remainder_2

        final_count = new_count - (remainder_2 * discount_2)
        final_total = 50 * final_count

        total.append(total_1 + total_2 + final_total)

    if 'E' in counter.keys():
        count = counter['E']
        total.append(40 * count)

        discount_amt = count // 2

        try:
            if counter['B']:
                counter['B'] -= discount_amt
        except KeyError:
            pass

    if 'B' in counter.keys():
        count = counter['B']
        discount_amt = count // 2
        total.append((45 * discount_amt) + 30 * (count - (discount_amt * 2)))

    if 'C' in counter.keys():
        count = counter['C']
        total.append(20 * count)

    if 'D' in counter.keys():
        count = counter['D']
        total.append(15 * count)

    if 'F' in counter.keys():
        count = counter['F']
        discount_amt = count // 3
        counter['F'] -= discount_amt

        count = counter['F']
        total.append(10 * count)

    else:
        total.append(0)

    return sum(total)


test = 'FAFFAFEEFBBF'
test_sku = [char for char in test]


print(checkout(test_sku))
