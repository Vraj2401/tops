def unzip_tuples():
    n = int(input("Enter the number of tuples: "))
    pairs = []

    for i in range(n):
        # Split and convert each tuple input
        a, b = input(f"Enter elements of tuple {i+1} : ").split()
        pairs.append((a, b))

    first_elements, second_elements = zip(*pairs)

    print("First list:", list(first_elements))
    print("Second list:", list(second_elements))

unzip_tuples()