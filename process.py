import numpy as np
import product

## Data processing function


def process_data(products, words):
    # Nothing to process
    if products == []:
        return products
    # List of words in product title that indicate an accessory
    bad_words = ["case", "screen protector", "headphones", "power bank"]
    # Remove non-float prices (faulty data) before calculating average
    products = list(filter(lambda x: isinstance(x.price, float), products))
    # Remove suspiciously cheap products (likely accessories)
    average_price = np.average([x.price for x in products])
    products = list(filter(lambda x: (x.price >= average_price/4), products))
    for word in words:
        # Ensure correct device
        # E.g, filter out Iphone 13 for an Iphone 12 scrape as searches often yield similar devices
        products = list(filter(lambda x: word.lower() in x.name.lower(), products))
    for bad_word in bad_words:
        products = list(filter(lambda x: bad_word.lower() not in x.name.lower(), products))
    return products
