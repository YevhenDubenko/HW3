phone_number = input("Enter your phone number for verification:")
x = len(phone_number)
if phone_number.isdigit() and x == 10:
    print("Good boy,thank you ☺ ")
else:
    print("Please check the number of entered characters(phone number must be 10 digits)")
