colors = []

while True:
    colors = input("Enter a color or enter 'quit' to quit: ")
    if colors == "quit":
        break
    colors.append(colors)
    print(colors)
    
else:
    print("You have entered the following colors: {colors} ")
    
    
