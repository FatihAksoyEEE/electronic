import math

def calculate_power():
    """
    This function calculates power using different electrical laws based on user input.
    It allows calculations using Ohm's Law (P = V*I, P = I^2*R, P = V^2/R)
    and the general power formula (P = W/t).
    """
    print("Welcome to the Electrical Power Calculator!")
    print("Please choose the type of calculation you want to perform:")
    print("1. Calculate Power using Voltage and Current (P = V * I)")
    print("2. Calculate Power using Current and Resistance (P = I^2 * R)")
    print("3. Calculate Power using Voltage and Resistance (P = V^2 / R)")
    print("4. Calculate Power using Work and Time (P = W / t)")

    choice = input("Enter your choice (1-4): ")

    try:
        if choice == '1':
            voltage = float(input("Enter the Voltage (V) in Volts: "))
            current = float(input("Enter the Current (I) in Amperes: "))
            power = voltage * current
            print(f"The calculated Power (P) is: {power:.2f} Watts")
        elif choice == '2':
            current = float(input("Enter the Current (I) in Amperes: "))
            resistance = float(input("Enter the Resistance (R) in Ohms: "))
            power = current**2 * resistance
            print(f"The calculated Power (P) is: {power:.2f} Watts")
        elif choice == '3':
            voltage = float(input("Enter the Voltage (V) in Volts: "))
            resistance = float(input("Enter the Resistance (R) in Ohms: "))
            if resistance == 0:
                print("Error: Resistance cannot be zero for this calculation.")
            else:
                power = voltage**2 / resistance
                print(f"The calculated Power (P) is: {power:.2f} Watts")
        elif choice == '4':
            work = float(input("Enter the Work (W) in Joules: "))
            time = float(input("Enter the Time (t) in seconds: "))
            if time == 0:
                print("Error: Time cannot be zero for this calculation.")
            else:
                power = work / time
                print(f"The calculated Power (P) is: {power:.2f} Watts")

    except ValueError:
        print("Invalid input. Please enter numeric values for calculations.")

if __name__ == "__main__":
    calculate_power()