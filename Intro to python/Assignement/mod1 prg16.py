def count_frequencies(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

user_input = input("Enter numbers : ")

numbers = list(map(int, user_input.split()))

frequencies = count_frequencies(numbers)

print(", ".join([f"{number} : {count}" for number, count in sorted(frequencies.items())]))