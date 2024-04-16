import os

def load_list(filename):
    slist = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # make sure there's something there
                    product, quantity = line.strip().split('\t')
                    slist[product] = int(quantity)
    return slist
