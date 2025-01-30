total = 0
positive = 0
negative = 0

while True:
    raw = int(input(f"Enter a Positive or Negative Number and enter {0} to stop:"))
    if raw == 0:

        break

    total = total+1
    
    if raw > 0:
        positive +=1
        print(f"Positive Number: {raw}")

    elif raw < 0:
        negative +=1
        print(f"Negative Number: {raw} ")

print(f"\nYou entered {total} items in total.")
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")