inventory = {"apples":50,"bananas":100,"oranges":100}

print(inventory["apples"])
print(inventory.get("apples",0))

for key,value in inventory.items():
    if value <= 75:
        print(f"{key} is low on stock")