
cities = ("Paris", "London", "Tokyo")
print("Tuple:", cities)
print("First:", cities[0])
print("Last:", cities[-1])
more = ("New York", "Sydney")
result = cities + more
print("Concatenated:", result)
try:
    cities[0] = "Dubai"
except TypeError as e:
    print("Error:", e)
a, b, c = cities
print("Unpacked:", a, b, c)
