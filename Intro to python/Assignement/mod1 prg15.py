def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci_series(n)