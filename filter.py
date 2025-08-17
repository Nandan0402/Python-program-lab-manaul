# Take input as a space-separated string of numbers
n = list(map(int, input("Enter the numbers separated by space: ").split()))

# Filter even numbers
even = list(filter(lambda x: x % 2 == 0, n))
print("Even numbers:", even)

# Filter odd numbers
odd = list(filter(lambda x: x % 2 != 0, n))
print("Odd numbers:", odd)
