# Method 1 - direct creation - prints as-is with braces
student1 = {
    "name":"Alice",
    "age":20,
    "grade":"A"
}

print("Method 1:", student1)

# Method 2 - Using dict 
student2 = dict(name = "Alice",age = 20,grade = "A")
print("Method 2:", student2)

# Method 3 - Using Tuples 
student3 = ["Physics", "Chemistry", "Biology"]
scores = dict.fromkeys(student3,0)
print("Method 3:", scores)

