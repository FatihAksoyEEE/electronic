from typing import Union

valid_colors: list= [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
    "gold",
    "silver"
]

significant_colors: dict[ str, int ]= {
    "black": 0,
    "brown": 1, 
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
multiplier_colors: dict[ str, float ]= {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1_000,
    "yellow": 10_000,
    "green": 100_000,
    "blue": 1_000_000,
    "violet": 10_000_000,
    "grey": 100_000_000,
    "white": 1_000_000_000
}
tolerance_colors: dict[ str, float ]= {
    "brown": 1,
    "red": 2,
    "green": 0.5,
    "blue": 0.25,
    "violet": 0.1,
    "grey": 0.05,
    "gold": 5,
    "silver": 10
}

temparature_coefficient_colors: dict[ str, int ]= {
    "black": 250,
    "brown": 100,
    "red": 50,
    "orange": 15,
    "yellow": 25,
    "green": 20,
    "blue": 10,
    "violet": 5,
    "grey": 1,
    "white": 0,
}

band_types: dict[ int, dict[str, int] ]= {
    3: {"significant": 2, "multiplier": 1, "tolerance": 0, "temparature_coefficient": 0},
    4: {"significant": 2, "multiplier": 1, "tolerance": 1, "temparature_coefficient": 0},
    5: {"significant": 3, "multiplier": 1, "tolerance": 1, "temparature_coefficient": 0},
    6: {"significant": 3, "multiplier": 1, "tolerance": 1, "temparature_coefficient": 1},
}   

def get_significant_digit(colors: list[str]) -> str:
    digit = ""
    for color in colors:
        if color not in significant_colors:
            msg= f"{color} is not a valid significant figure color"
            raise ValueError(msg)
        digit += str(significant_colors[color])
    return str(digit)

def get_multiplier(color: str) -> float:
    if color not in multiplier_colors:
        msg= f"{color} is not a valid multiplier color"
        raise ValueError(msg)
    return multiplier_colors[color]
def get_tolerance(color: str) -> float:
    if color not in tolerance_colors:
        msg= f"{color} is not a valid tolerance color"
        raise ValueError(msg)
    return tolerance_colors[color]
def get_temparature_coefficient(color: str) -> int:
    if color not in temparature_coefficient_colors:
        msg= f"{color} is not a valid temparature coefficient color"
        raise ValueError(msg)
    return temparature_coefficient_colors[color]

def validate_colors(colors: list[str]) -> None:
    for color in colors:
        if color not in valid_colors:
            msg= f"{color} is not a valid color"
            raise ValueError(msg)   
def decode_resistor_colors(colors: list[str]) -> dict[str, Union[float, int]]:
    validate_colors(colors)
    band_count= len(colors)
    if band_count not in band_types:
        msg= f"{band_count} bands is not supported"
        raise ValueError(msg)
    
    band_info = band_types[band_count]
    current_index = 0
    
    significant_digits_str = get_significant_digit(colors[current_index : current_index + band_info["significant"]])
    current_index += band_info["significant"]
    
    multiplier = get_multiplier(colors[current_index])
    current_index += band_info["multiplier"]
    
    tolerance = None
    if band_info["tolerance"] > 0:
        tolerance = get_tolerance(colors[current_index])
        current_index += band_info["tolerance"]
        
    temparature_coefficient = None # Corrected typo: temparature -> temperature
    if band_info["temparature_coefficient"] > 0:
        temparature_coefficient = get_temparature_coefficient(colors[current_index])
        current_index += band_info["temparature_coefficient"]
    
    resistance_value = int(significant_digits_str) * multiplier
    result: dict[str, Union[float, int]] = {"resistance_value": resistance_value}
    if tolerance is not None:
        result["tolerance"]= tolerance
    if temparature_coefficient is not None:
        result["temparature_coefficient"]= temparature_coefficient
    return result

def main():
    print("Welcome to the Resistor Color Code Decoder!")
    print("Please enter the resistor band colors, separated by commas.")
    print("Example: red,violet,orange,gold (for a 4-band resistor)")
    print("Supported colors:", ", ".join(valid_colors))

    while True:
        user_input = input("Enter colors (or 'exit' to quit): ").lower()
        if user_input == 'exit':
            break
        
        colors = [color.strip() for color in user_input.split(',')]
        try:
            result = decode_resistor_colors(colors)
            print("\n--- Resistor Properties ---")
            print(f"Resistance Value: {result['resistance_value']} Ohms")
            if 'tolerance' in result:
                print(f"Tolerance: ±{result['tolerance']}%")
            if 'temparature_coefficient' in result:
                print(f"Temperature Coefficient: {result['temparature_coefficient']} ppm/K")
            print("---------------------------\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
