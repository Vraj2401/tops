n = int(input("Enter a positive integer: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"The sum of the first {n} positive integers is: {total}")