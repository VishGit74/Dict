# Program to create a shopping cart 

shoppingCart = {}

def addToCart(cart,item,amount,price):
    if item in cart:
        cart[item]["quantity"] += amount
    else:
        cart[item]= {"quantity":amount,"price":price}

addToCart(shoppingCart,"apple",5,0.5)
addToCart(shoppingCart,"banana",10,0.1)
addToCart(shoppingCart,"apple",7,0.5)

print(shoppingCart)

cart_total = 0

for item in shoppingCart.values():
    cart_total += item["quantity"]*item["price"]

print(cart_total)
print("Keys")
print(shoppingCart.keys())
print("Values")
print(shoppingCart.values())
print("Items")
print(shoppingCart.items())