def get_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

user_input = input("Enter the list : ")
input_list = list(map(int, user_input.split()))

unique_elements = get_unique_elements(input_list)

print("Original List:", input_list)
print("Unique Elements:", unique_elements)