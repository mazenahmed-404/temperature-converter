def main():
    # Getting input from the user
    temperature = input("Welcome! Please, Enter the temperature you got: ")
    initial_temp = float(temperature)
    input_unit = input("Excellent! Now, Enter the temperature unit (use c for Celsius, f for Fahrenheit, k for Kelvin): ")
    desired_unit = input("One final thing! Enter the desired temperature unit (use the same notation specified: )")

    # The main conversion logic
    if input_unit == "c" and desired_unit == "f":
        final_temp = c_to_f(initial_temp)
        print(f"The Converted Temperature value is: {final_temp:.3f} °F")
    elif input_unit == "c" and desired_unit == "k":
        final_temp = c_to_k(initial_temp)
        print(f"The Converted Temperature value is: {final_temp:.3f} K")
    elif input_unit == "f" and desired_unit == "c":
        final_temp = f_to_c(initial_temp)
        print(f"The Converted Temperature value is: {final_temp:.3f} °C")
    elif input_unit == "f" and desired_unit == "k":
        final_temp = f_to_k(initial_temp)
        print(f"The Converted Temperature value is: {final_temp:.3f} K")
    elif input_unit == "k" and desired_unit == "f" and initial_temp >= 0:
        final_temp = k_to_f(initial_temp)
        print(f"The Converted Temperature value is: {final_temp:.3f} °F")
    elif input_unit == "k" and desired_unit == "c" and initial_temp >= 0:
        final_temp = k_to_c(initial_temp)
        print(f"The Converted Temperature value is: {final_temp:.3f} °C")
    elif input_unit == "k" and desired_unit == "f" and initial_temp < 0:
        print("The Kelvin value can't be negative, buddy!")
    elif input_unit == "k" and desired_unit == "c" and initial_temp < 0:
        print("The Kelvin value can't be negative, buddy!")
    elif input_unit == "c" and desired_unit == "c":
        print(f"The Temperature value is: {initial_temp} °C")
    elif input_unit == "k" and desired_unit == "k" and initial_temp >= 0 :
        print(f"The Temperature value is: {initial_temp} K")
    elif input_unit == "k" and desired_unit == "k" and initial_temp < 0 :
        print("The Kelvin value can't be negative, buddy!")
    elif input_unit == "f" and desired_unit == "f":
        print(f"The Temperature value is: {initial_temp} °F")
    else:
        print("Please, Enter Valid Temperature units!")

def c_to_f(temperature):
    return (9/5 * temperature) + 32
def c_to_k(temperature):
    return temperature + 273.15
def f_to_c(temperature):
    return (5/9) * (temperature - 32)
def f_to_k(temperature):
    return ((5/9) * (temperature - 32)) + 273.15
def k_to_f(temperature):
    return (9/5) * (temperature - 273.15) + 32
def k_to_c(temperature):  
    return temperature - 273.15

main()
