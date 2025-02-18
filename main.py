# TASK: Write a function that converts between Celsius and Fahrenheit.

# Define a function that takes a float and a string parameter
def get_temp(temp: float, unit: str):
    while True:
    # If unit is 'C', convert to Fahrenheit
        if unit.upper()=="C":
            converted=(temp *(9/5)) + 32
            return converted,"F"    # If unit is 'F', convert to Celsius
        elif unit.upper()=="F":
            converted=(temp - 32) * (5/9)
            return converted,"C"
        else:
            return None
# Return a formatted string with the result
# Prompt the user for input and call the function
temperature=get_temp(float(input("enter temperature ")),input('enter C or F '))
# Display the converted temperature
print("your converted temperature is ", temperature)

