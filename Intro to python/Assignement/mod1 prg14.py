def top_three_values():
    my_dict = {}
    n = int(input("Enter the number of key-value pairs: "))

    for i in range(n):
        key = input(f"Enter key {i + 1}: ")
        value = int(input(f"Enter value for '{key}': "))
        my_dict[key] = value

    sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

    top_three = sorted_items[:3]

    print("\nTop 3 highest values with keys:")
    for key, value in top_three:
        print(f"{key}: {value}")


top_three_values()