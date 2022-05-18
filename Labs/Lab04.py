print ('Grades Program\n')
grade = float (input('Please insert your grade (0-100):\n'))

# [90, 100]: A 
# [80, 90): B 
# [70, 80): C 
# [60, 70): D 
# [0, 60): F

if grade >= 0 and grade < 60:
    print ('Your Grade is F\n')
elif grade >= 60 and grade < 70:
    print ('Your Grade is D\n')
elif grade >= 70 and grade < 80:
    print ('Your Grade is C\n')
elif grade >= 80 and grade < 90:
    print ('Your Grade is B\n')
elif grade >= 90 and grade <= 100:
    print ('Your Grade is A\n')
else:
    print ('Invalid Value')


