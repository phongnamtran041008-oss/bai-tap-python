import cmath 
a = float(input("Enter the real part a = "))
b = float(input("Enter the imaginary part b = "))
so_phuc = complex(a, b)
z = cmath.sqrt(so_phuc)
print(f"z = {z:.0f}")