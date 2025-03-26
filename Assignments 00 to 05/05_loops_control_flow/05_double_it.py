def main():
    curr_value = int(input("Enter a number: "))  # Get user input and convert to integer

    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")  # Print the new value on the same line

if __name__ == "__main__":
    main()
