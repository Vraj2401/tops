def find_second_smallest(l):
    if len(l) < 2:
        return "List must contain at least two unique elements."

    unique_numbers = list(set(l))

    if len(unique_numbers) < 2:
        return "No second smallest element (all elements are the same)."

    unique_numbers.sort()

    return unique_numbers[1]

user_input = input("Enter the list : ")
l = list(map(int, user_input.split()))

result = find_second_smallest(l)
print("Second smallest number:", result)