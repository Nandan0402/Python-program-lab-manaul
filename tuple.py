# Tuple built-in function examples

# Original tuple
t = (1, 2, 3, 4, 2, 5)
print("Original Tuple:", t)

# Length of tuple
print("Length of tuple:", len(t))

# Count occurrences
print("Count of 2:", t.count(2))

# Index of element
print("Index of 3:", t.index(3))

# Checking membership
print("Is 4 in tuple?", 4 in t)
print("Is 10 not in tuple?", 10 not in t)

# Converting tuple to list to add items
l = list(t)
l.append(6)
print("After appending 6 to list:", l)

# Converting back to tuple
t = tuple(l)
print("Updated Tuple:", t)

# Min, Max, Sum
print("Minimum value:", min(t))
print("Maximum value:", max(t))
print("Sum of all elements:", sum(t))

# Sorting
print("Sorted tuple:", tuple(sorted(t)))

# Repetition
print("Tuple repeated 2 times:", t * 2)

# Slicing
print("Sliced tuple (first 4 elements):", t[:4])

# Tuple unpacking
a, b, c, d, e, f, g = t
print("Unpacked values:", a, b, c, d, e, f, g)
