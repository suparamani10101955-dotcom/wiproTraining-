text = "banana"

count = sum(1 for i, ch in enumerate(text) if ch == 'a')
print(count)