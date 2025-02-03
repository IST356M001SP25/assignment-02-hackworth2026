colors = []

while True:
    color_base = input("Enter a color or enter 'quit' to quit: ")
    if color_base == 'quit':
        break
    elif color_base in colors:
        print("You have already Entered that color. Removing it.")
    else:
        colors.append(color_base)
    print(colors)
            
