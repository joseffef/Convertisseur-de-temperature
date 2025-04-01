unit = input("IS THIS TEMPERATURE IN CELSIUS OR FAHRENHEIT (c or f): ")
temp = float(input("ENTER THE TEMPERATURE : "))

if unit == "c":
    temp = round((9*temp) / 5 + 32, 1)
    print(f"THE TEMPERATURE IN FAHRENHEIT IS : {temp} °F")
elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"THE TEMPERATURE IN CELSIUS IS : {temp} °C")    
else :
    print(f"{unit} is an invalid unit of measurement") 


