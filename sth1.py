print("y = 2^x +3x +4 if x>= 1\n y = 3^x +2x +1 if x< 1")
while True:
    try:
        x = float(input("Enter a number x ="))

        if x >= 1:
            print(f" y = {2**x +3*x +4:.2f}")
        else:
            print(f" y = {3**x +2*x + 1:.2f}")
        break
    except ValueError:
        print("Please enter a valid number.")
