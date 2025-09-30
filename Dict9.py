temp_f = {
    "Monday":85,
    "Tuesday":90,
    "Wednesday":91
}

temp_c = {
    day:round((temp-32)*5/9) for day,temp in temp_f.items()
}

print(temp_c)