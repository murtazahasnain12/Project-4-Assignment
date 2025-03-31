import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generate a list of N_NUMBERS random integers between MIN_VALUE and MAX_VALUE
    and print them.
    """
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print("Generated numbers:", random_numbers)

if __name__ == '__main__':
    main()
