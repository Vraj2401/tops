def sort_dict_by_value():
    my_dict = {}
    n = int(input("Enter the number of key-value pairs: "))

    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        value = int(input(f"Enter value for '{key}': "))
        my_dict[key] = value

    # Sort in ascending order
    ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    # Sort in descending order
    descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    print("\nOriginal Dictionary:", my_dict)
    print("Sorted in Ascending Order by Value:", ascending)
    print("Sorted in Descending Order by Value:", descending)

# Call the function
sort_dict_by_value()