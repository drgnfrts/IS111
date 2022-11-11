# Name:
# Email ID:

def compute_total_price(price_dict, item_list):
    total = 0.0
    for item in item_list:
        k, n = item
        if k in price_dict:
            total += n * price_dict[k]
    # Modify the code below.
    return total