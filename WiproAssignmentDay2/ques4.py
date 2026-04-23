data = {"name": "Jagadeesh", "age": 21, "hobby": "Coding"}
print("Initial:", data)
print("Name:", data["name"])
data["food"] = "Biryani"
data["hobby"] = "Gaming"
print("Updated:", data)
print("Keys:", data.keys())
print("Values:", data.values())
data.pop("age")
print("After removal:", data)
