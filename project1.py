# Function to convert Celsius to Fahrenheit and Kelvin
def from_celsius(temp):
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    return fahrenheit, kelvin

# Function to convert Fahrenheit to Celsius and Kelvin
def from_fahrenheit(temp):
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert Kelvin to Celsius and Fahrenheit
def from_kelvin(temp):
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Main function
def convert_temperature():
    print("Welcome to the Temperature Converter!")
    
    # Get temperature value and original unit from the user
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    
    if unit == 'C':
        fahrenheit, kelvin = from_celsius(temp)
        print(f"{temp}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f} K.")
    elif unit == 'F':
        celsius, kelvin = from_fahrenheit(temp)
        print(f"{temp}°F is equal to {celsius:.2f}°C and {kelvin:.2f} K.")
    elif unit == 'K':
        celsius, fahrenheit = from_kelvin(temp)
        print(f"{temp} K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
    else:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

# Run the program
convert_temperature()
