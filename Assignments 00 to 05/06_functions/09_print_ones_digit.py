def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def print_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)
    
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
