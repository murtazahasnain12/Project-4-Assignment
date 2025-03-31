# Constant for Mars gravity relative to Earth
MARS_MULTIPLE = 0.378  

def main():
    # Prompt user for weight on Earth
    earth_weight_str = input("Enter a weight on Earth: ")

    # Convert input to a float
    earth_weight = float(earth_weight_str)

    # Calculate weight on Mars
    mars_weight = earth_weight * MARS_MULTIPLE

    # Round to 2 decimal places
    rounded_mars_weight = round(mars_weight, 2)

    # Display the result
    print("The equivalent weight on Mars: " + str(rounded_mars_weight))

# Standard Python entry point
if __name__ == "__main__":
    main()



# Constants for gravitational multipliers of planets relative to Earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Prompt user for weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt user for a planet name
    planet = input("Enter a planet: ")

    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("Invalid planet name!")
        return  # Exit the function if the planet name is incorrect

    # Calculate weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    # Display the result
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")

# Standard Python entry point
if __name__ == "__main__":
    main()
