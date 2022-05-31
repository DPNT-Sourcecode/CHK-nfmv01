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
            'K': [70, '2K-120'],
            'L': [90],
            'M': [15],
            'N': [40, '3N-FREE-M'],
            'O': [10],
            'P': [50, '5P-200'],
            'Q': [30, '3Q-80'],
            'R': [50, '3R-FREE-Q'],
            'S': [20, '3-(S,T,X,Y,Z)-45'],
            'T': [20, '3-(S,T,X,Y,Z)-45'],
            'U': [40, '3U-FREE-U'],
            'V': [50, '2V-90', '3V-130'],
            'W': [20],
            'X': [17, '3-(S,T,X,Y,Z)-45'],
            'Y': [20, '3-(S,T,X,Y,Z)-45'],
            'Z': [21, '3-(S,T,X,Y,Z)-45']}


#FUNCTION TO HANDLE GROUP OFFERS
def group_offer(counter):
    group_discounts_list = []
    for key, value in counter.items():
        #indicator that group offer is present
        group_signal = '('

        try:
            if group_signal in products[key][1]:
                group_discounts_list.append(key)
        except IndexError:
            pass

    if group_discounts_list:
        x = products[group_discounts_list[0]][1]
        x = x.split('-')
        quantity = int(x[0])
        price = int(x[2])
        group_count = sum([counter[key] for key in group_discounts_list])

        remainder = group_count // quantity

        #total cost of group offers
        total_included = price * remainder

        #number of items not included in group offering
        not_included = group_count - (quantity * remainder)

        temp_dict = {sku: products[sku][0] for sku in group_discounts_list}
        sorted_count_dict = {k: v for k,v in sorted(temp_dict.items(), key=lambda item: item[1])}

        #total cost of items not included in group offering
        total_leftover = []
        while not_included != 0:
            for key, value in sorted_count_dict.items():
                try:
                    if counter[key] >= not_included:
                        total_leftover.append(not_included * value)
                        not_included = 0

                    else:
                        total_leftover.append(counter[key] * value)
                        not_included = not_included - counter[key]
                        counter[key] -= not_included

                except KeyError:
                    pass

        return sum(total_leftover) + total_included

    else:
        return 0



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

    group_offer_sum = group_offer(counter)
    free_product_sum, updated_counter = free_product_offer_calc(counter)
    remaining_sum = final_calc(updated_counter)

    return group_offer_sum + free_product_sum + remaining_sum


# test = 'CXYZYZC'
# test_sku = [char for char in test]
#
# 
# print(checkout(test_sku))

'''
Some requests have failed (1/149). Here are some of them:
 - {"method":"checkout","params":["CXYZYZC"],"id":"CHK_R5_001"}, expected: 122, got: 119
'''

