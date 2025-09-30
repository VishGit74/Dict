items = [
    ("apple","fruit"),
    ("chillie","vegetable"),
    ("orange","fruit")
]

categories = {}

for item,category in items:
    categories.setdefault(category,[]).append(item)

print(categories)
