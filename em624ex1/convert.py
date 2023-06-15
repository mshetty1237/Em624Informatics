print("\n This program is run by Mohit Shetty")
while True:
    c = input("Enter the temperature in Celsius: ")
    if c == 'done':
        break
    else:
        f = float(c) * 1.8 + 32
        print()
        print("The temparature in farenheit is", f)




