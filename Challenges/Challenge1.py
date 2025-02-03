attempt = 0

while True:
    passcode = input("Type in your password:")
    if passcode == "secret":
        print("Access Granted")

        break

    else:
        attempt +=1
        print(f"The Password {passcode} is incorrect")
        print(f"Attempt amounts left {5-attempt}")

    if attempt >=5:
        print("Your account is now Locked")

    
