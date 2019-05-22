math = int(input('Math: '))
science = int(input('Science:'))
physics =  int(input('Physics: '))

average = (math + science + physics) / 3


score = ''
if average >= 90:
  score = 'A'
elif average >= 80:
  score = 'B'
elif average >= 70:
  score = 'C'
elif average >= 60:
  score = 'D'
elif average >= 50:
  score = 'E'
else:
  score = 'F'

print('Average is {}. Score is {}'.format(average, score))
