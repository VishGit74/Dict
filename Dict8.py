age = {
    "Vishal":52,
    "Ritu":50,
    "Ratnesh":81,
    "Sumita":75
}

sorted_by_name = dict(sorted(age.items()))
print(sorted_by_name)

sorted_by_value = dict(sorted(age.items(),key=lambda x:x[1]))
print(sorted_by_value)

sorted_by_key = dict(sorted(age.items(),key=lambda x:x[0]))
print(sorted_by_key)
