temp_type = input("Enter your type of temperature (C/F/K): ").strip().upper()

if temp_type in ["C", "F", "K"]:
    temp = float(input(f"Enter the temperature in {temp_type}: "))

    if temp_type == "C":
        c_val = temp
    elif temp_type == "F":
        c_val = (temp - 32) * 5/9
    else:  # K
        c_val = temp - 273.15

    # Tính toán Fahrenheit và Kelvin dựa trên Celsius đã chuẩn hóa
    f_val = c_val * 9/5 + 32
    k_val = c_val + 273.15

    # In kết quả tùy thuộc đơn vị gốc
    if temp_type != "F":
        print(f"The temperature in Fahrenheit is: {f_val:.2f} °F")
    if temp_type != "C":
        print(f"The temperature in Celsius is: {c_val:.2f} °C")
    if temp_type != "K":
        print(f"The temperature in Kelvin is: {k_val:.2f} K")
else:
    print("Invalid temperature type! Please enter C, F, or K.")