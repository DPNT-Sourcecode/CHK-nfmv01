# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = {}
    total = []

    available_skus = ['A', 'B', 'C', 'D', 'E']

    for x in skus:
        if x not in available_skus:
            return -1
        else:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1

    for sku, count in counter.items():
        if sku == 'A':
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

        if sku == 'B':
            discount_amt = count // 2
            total.append((45 * discount_amt) + 30 * (count - (discount_amt * 2)))

        if sku == 'C':
            total.append(20 * count)

        if sku == 'D':
            total.append(15 * count)

        if sku == 'E':
            total.append(40 * count)

        else:
            total.append(0)

    return sum(total)


# test = 'AAABBAAACCAAADEED'
# test_sku = [char for char in test]
#
#
# print(checkout(test_sku))

