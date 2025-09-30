# Understanding Default Dict

from collections import defaultdict

# int as Default Dict

words = ["apple","orange","banana","apple","pear","guava","blueberries","orange"]

wordcount = defaultdict(int)
for word in words:
    wordcount[word] += 1

print("\ndefaultdict: ", dict(wordcount))

# set as default dict

uniqueitems = defaultdict(set)
purchases = [
    ("Alice","Apple"),
    ("Bob","Banana"),
    ("Charles","Cucumber"),
    ("Alice","Apple"),
    ("Bob","Berries")
]
for customer,item in purchases:
    uniqueitems[customer].add(item)
print("\nUnique Items",dict(uniqueitems))

# List as defaultdict

grouped = defaultdict(list)
pairs = [("fruit","apple"),("fruit","guava"),("veg","broccoli")]
for category,item in pairs:
    grouped[category].append(item)
print("\nGrouped: ", dict(grouped))

# Custom class as defaultdict

def default_student():
    return{"grade":0,"attendance":0}

classed = defaultdict(default_student)
classed["Alice"]["grade"] = 85
classed["Bob"]["attendance"] = 90
print("\nClassed: ",dict(classed))