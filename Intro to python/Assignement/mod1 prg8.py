def is_sublist(main_list, sub_list):
    main = len(main_list)
    sub = len(sub_list)

    if sub == 0:
        return True

    for i in range(main - sub + 1):
        if main_list[i:i + sub] == sub_list:
            return True
    return False

main_input = input("Enter the main list: ")
sub_input = input("Enter the sublist: ")

main_list = list(map(int, main_input.split()))
sub_list = list(map(int, sub_input.split()))

if is_sublist(main_list, sub_list):
    print("Sublist found!")
else:
    print("Sublist not found.")