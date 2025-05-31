def tuples_to_dict():
    n = int(input("Enter the number of key-value pairs: "))
    pairs = []

    for i in range(n):
        key = input(f"Enter key for pair {i+1}: ")
        value = input(f"Enter value for pair {i+1}: ")
        pairs.append((key, value))

    result_dict = dict(pairs)

    print("\nResulting Dictionary:", result_dict)

tuples_to_dict()