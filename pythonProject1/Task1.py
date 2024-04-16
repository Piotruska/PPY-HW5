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

def save(slist, filename):
    with open(filename, 'w') as file:
        for product, quantity in slist.items():
            file.write(f"{product}\t{quantity}\n")

def add(slist, product, quantity):
    if product in slist:
        slist[product] += quantity
    else:
        slist[product] = quantity

def remove(slist, product):
    if product in slist:
        del slist[product]


    if choice == "1":
        product = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        add(shopping_list, product, quantity)
        print(f"Added {quantity} of {product} to the shopping list.")

    elif choice == "2":
        product = input("Enter the product name to remove: ")
        remove(shopping_list, product)
        print(f"Removed {product} from the shopping list.")

    elif choice == "3":
        print("\nCurrent Shopping List:")
        display(shopping_list)

    elif choice == "4":
        save(shopping_list, filename)
        print("Shopping list saved. Exiting program.")
        break

    else:
        print("Invalid choice, please choose from 1 to 4.")