intro = int(input('Intro: '))
algorithm = int(input('Algorithm: '))
java = int(input('Java: '))

average = (intro + algorithm + java) // 3

if average >= 70:
    print(f'Your average is {average}. Pass')
else:
    print(f'Your average is {average}. Fail')
