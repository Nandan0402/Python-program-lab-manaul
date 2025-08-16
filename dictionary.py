s = {"name": "Bob",
     "age": 19,
     "course": "BCA"
     }

print("Dictionary:", s.items())

# Accessing values
print("Name:", s["name"])
print("Course:", s.get("course"))

# Updating
s["age"] = 20
print("Updated age:", s["age"])

# Length
print("Length of Dictionary:", len(s))

# Built-in dictionary functions
print("Keys:", s.keys())         # Returns all keys
print("Values:", s.values())     # Returns all values
print("Items:", s.items())       # Returns key-value pairs

# Adding new key-value
s["college"] = "Ramaiah"
print("After Adding College:", s)

# pop() → remove item by key
s.pop("course")
print("After pop:", s)

# popitem() → removes last inserted
s.popitem()
print("After popitem:", s)

# setdefault()
print("Setdefault Example:", s.setdefault("gender", "Male"))

# update()
s.update({"city": "Bangalore", "age": 21})
print("After update:", s)

# copy()
s_copy = s.copy()
print("Copied Dictionary:", s_copy)

# fromkeys()
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys Example:", new_dict)

# clear()
s_copy.clear()
print("After clear (empty copy):", s_copy)
