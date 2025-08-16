l = [10, 20, 30, 40, 50]
print("Original:", l)

l.append(60)
print("append:", l)

l.extend([70, 80])
print("extend:", l)

l.insert(2, 25)
print("insert:", l)

l.remove(40)
print("remove:", l)

print("pop:", l.pop())
print("after pop:", l)

print("index of 30:", l.index(30))

print("count of 20:", l.count(20))

l.sort()
print("sort:", l)

l.reverse()
print("reverse:", l)

l2 = l.copy()
print("copy:", l2)

l.clear()
print("clear:", l)
