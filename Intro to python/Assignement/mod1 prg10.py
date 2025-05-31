def get_unique_values():
    user_input = input("Enter list : ")
    l = list(map(int, user_input.split()))
    unique_values = list(set(l))
    print("Unique values in the list:", unique_values)

get_unique_values()