import copy

record1 = {"name":"Vishal","age":50,"weight":69,"height":174}
record2 = record1.copy()
print(record2)
record3 = dict.copy(record1)
print(record3)
record4 = {k:v for k,v in record1.items()}
print(record4)
record5 = copy.deepcopy(record1)
print(record5)
record5["name"] = "Ritu"
print(record1)
print(record5)