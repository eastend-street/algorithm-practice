degree_type = input('Enter C or F: ').upper()
degree = int(input('Enter degree: '))
result_degree = 0
result_degree_type = ""

if degree_type == "C":
    result_degree_type = "Fahrenheit"
    result_degree = (degree * 9 / 5) + 32
elif degree_type == "F":
    result_degree_type = "Celsius"
    result_degree = (degree - 32) * 5 / 9
else:
    print('Please enter C or F. Try it again.')
    exit()

print(f'{result_degree_type} is {result_degree}.')
# print(('{} is {}.').format(result_degree_type, result_degree))
