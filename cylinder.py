import math

radius = int(input('Radius: '))
height = int(input('Height: '))

area = int(math.pi * radius * radius * 2 + height * radius * math.pi * 2)
volume = int((math.pi * radius * radius) * height)

print(f'The area is {area}. The volume is {volume}')
