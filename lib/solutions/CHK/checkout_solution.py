# noinspection PyUnusedLocal
# skus = unicode string

products = {'A': [50, '3A-130', '5A-200'],
            'B': [30, '2B-45'],
            'C': [20],
            'D': [15],
            'E': [40, '2E-FREE-B'],
            'F': [10, '2F-FREE-F'],
            'G': [20],
            'H': [10, '5H-45', '10H-80'],
            'I': [35],
            'J': [60],
            'K': [80, '2K-150'],
            'L': [90],
            'M': [15],
            'N': [40, '3N-FREE-M'],
            'O': [10],
            'P': [50, '5P-200'],
            'Q': [30, '3Q-80'],
            'R': [50, '3R-FREE-Q'],
            'S': [30],
            'T': [20],
            'U': [40, '3U-FREE-U'],
            'V': [50, '2V-90', '3V-130'],
            'W': [20],
            'X': [90],
            'Y': [10],
            'Z': [50]}


#FUNCTION TO HANDLE ALL SPECIAL OFFERS WITH FREE PRODUCTS
def free_product_offer_calc(counter):
    totals = []
    for key, value in counter.items():
        try:
            if 'FREE' in products[key][1]:
                base_price = products[key][0]
                offer = products[key][1]
                offer = offer.split('-')
                quantity = int(offer[0][:-1])
                free_product = offer[-1]

                if free_product == key:
                    count = counter[key]
                    discount_quantity = count // (quantity + 1)
                    counter[key] -= discount_quantity

                    count = counter[key]
                    totals.append(base_price * count)

                else:
                    count = counter[key]
                    totals.append(base_price * count)
                    discount_quantity = count // quantity

                    try:
                        if counter[free_product]:
                            counter[free_product] -= discount_quantity
                    except KeyError:
                        pass

        except IndexError:
            pass

    return sum(totals), counter


#FUNCTION TO HANDLE ALL REMAINING PRODUCTS
def final_calc(counter):
    totals = []
    for key, count in counter.items():
        try:
            offers = products[key][1:]
            base_price = products[key][0]

            for offer in reversed(offers):
                offer = offer.split('-')
                quantity = int(offer[0][:-1])
                price = int(offer[1])

                remainder = count // quantity
                total = price * remainder
                totals.append(total)

                count = count - (remainder * quantity)

            total_base = base_price * count
            totals.append(total_base)

        except ValueError:
            pass

    return sum(totals)


def checkout(skus):
    counter = {}

    for x in skus:
        if x not in products.keys():
            return -1
        else:
            if x not in counter:
                counter[x] = 0
            counter[x] += 1

    free_product_sum, updated_counter = free_product_offer_calc(counter)
    remaining_sum = final_calc(updated_counter)

    return (free_product_sum + remaining_sum)


test = 'FAFFAFEEFBBF'
test_sku = [char for char in test]


print(checkout(test_sku))

