freshman =int(input('Pleas insert the quantity of Freshman students:\n'))

sophmore =int(input('Pleas insert the quantity of Sophmore students:\n'))

junior =int(input('Pleas insert the quantity of Junior students:\n'))

senior =int(input('Pleas insert the quantity of Senior students:\n'))

total = freshman + sophmore + junior + senior

print(f'According to the provided information, there are {total} students')

print (f'From all students there are {(freshman/total) *100}% Freshmans, {(sophmore/total) *100}% Sophmore, {(junior/total) *100}% Juniors and {(senior/total) * 100}% Seniors')