import math
while True: 
    try:
        r = float(input("Enter the radius r = "))
        if r > 0: 
             print(f"The area of the circle is: {math.pi * r ** 2:.2f}")
             print(f"The circumference of the circle is {math.pi * 2 * r:.2f}")
             break
        else: 
             print("The radius must be greater than 0. Please try again.\n")
    except ValueError:
         print("Invalid input. Please enter a valid number for the radius.\n")