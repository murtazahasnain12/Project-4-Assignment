# Index Game Solution
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end]  # Slicing does not raise an IndexError

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

# List Practice Solution
def main():
    # Create a list called fruit_list
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    lst_length = len(fruit_lst)
    print("Length of list:", lst_length)

    # Add 'mango' at the end of the list.
    fruit_lst.append('mango')

    # Print the updated list.
    print("Updated list:", fruit_lst)

if __name__ == "__main__":
    main()
    index_game()
