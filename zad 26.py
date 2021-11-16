pin_code = "0805"
tries = 0
is_correct = False
while tries < 3:
    tries += 1;
    user_pin = input("Enter the PIN code: ")
    if user_pin == pin_code:
        is_correct = True
        print("Correct PIN")
        break
    else:
        print("Incorrect...")
        continue
if is_correct == False:
    print("Sorry, your payment card has been blocked.")
else:
    print("Success")