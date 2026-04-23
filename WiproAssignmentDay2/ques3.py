colors = {"Red", "Blue", "Green", "Yellow", "Black"}
print("Initial:", colors)
colors.add("White")
colors.remove("Blue")
print("Updated:", colors)
set2 = {"Green", "Purple", "Black"}
print("Intersection:", colors & set2)
print("Union:", colors | set2)
print("Difference:", colors - set2)
print("Is Red present?", "Red" in colors)

fruits = ["Apple", "Banana", "Apple", "Mango"]
print("Unique fruits:", set(fruits))
