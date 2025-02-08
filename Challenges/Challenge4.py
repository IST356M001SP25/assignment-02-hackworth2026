grocery_list = []

while True:
    item = input("Enter an item or enter 'quit' to quit: ")
    if item == 'quit':
        break
    price = input("Enter the price or enter 'quit' to quit: ")
    if price == 'quit':
        break
    try:
        price = float(price)  
    except ValueError:
        print("Invalid price. Please enter a numerical value.")
        continue
    grocery_list.append({'item': item, 'price': price})

print(grocery_list)