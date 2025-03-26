def get_last_element(lst):
    """Prints the last element of the provided list."""
    print(lst[-1])  # Accessing last element using negative indexing


def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst


def main():
    lst = get_lst()  # Get user-inputted list
    get_last_element(lst)  # Print the last element


# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
