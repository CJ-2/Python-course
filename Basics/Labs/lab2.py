def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    try:
        # Get user input for temperature and conversion type
        temperature = float(input("Enter the temperature: "))
        conversion_type = int(input("Choose conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n"))
        
        if conversion_type == 1:
            # Convert Celsius to Fahrenheit
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is equal to {result} degrees Fahrenheit.")
        elif conversion_type == 2:
            # Convert Fahrenheit to Celsius
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature} degrees Fahrenheit is equal to {result} degrees Celsius.")
        else:
            print("Invalid conversion type. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")

# Test the program with valid Celsius to Fahrenheit conversion
temperature_converter()

# Test the program with valid Fahrenheit to Celsius conversion
temperature_converter()

# Test the program with non-numeric input
temperature_converter()
