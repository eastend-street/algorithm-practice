degrees_type = input('Enter C or F: ')
degrees = int(input('Enter degrees: '))
result = 0

if degrees_type == "C":
    str_degrees_type = "Celsius"
    result = (degrees * 9/5) + 32
elif degrees_type == "F":
    str_degrees_type = "Fahrenheit"
    result = (degrees - 32) * 5/9
else:
    print('Please enter C or F. Try it again.')
    exit()

print(('{} is {}.').format(str_degrees_type, result))
