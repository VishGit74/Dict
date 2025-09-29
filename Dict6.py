def validate_fields(reqFields,studentRecord):
    missingFields = []
    for field in reqFields:
        if field not in studentRecord:
            missingFields.append(field)

    return len(missingFields) == 0, missingFields

record1 = {"name":"Vishal","age":52,"citizen":"SGP"}
record2 = {"name":"Rajesh","age":52,"email":"rajesh@gmail.com"}

requiredFields = ["name","age","email"]

valid1,missing1 = validate_fields(requiredFields,record1)
valid2,missing2 = validate_fields(requiredFields,record2)

print(f"User 1 valid: {valid1} and missing {missing1}")
print(f"User 2 valid: {valid2} and missing {missing2}")