import csv
def calc_avg_price(phones_data, brands_list):
    avg_prices = {}

    for brand in brands_list:
        total = 0
        count = 0

        for phone in phones_data:
            if phone["brand"] == brand:
                total += phone["price"]
                count += 1

        avg_prices[brand] = round(total / count, 2) if count > 0 else 0

    return avg_prices

