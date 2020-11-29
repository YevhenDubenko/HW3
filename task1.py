my_string = input("Enter something:")
x = len(my_string)
if x > 2:
    First_lust = my_string[:2] + my_string[-2:]
    print(First_lust)
elif x < 2:
    print("Very few signs, baby")
else:
    print(my_string * 2)
