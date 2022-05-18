#A
from math import sqrt

print('Lets calculate de sides of a triangle with the Pythagorean Calculator')

wanted_side = input('Which side do you want to calculate ? (A, B or C)\n')

if wanted_side == 'c':
    side_a = int(input('What is the size of A ?\n'))
    side_b = int(input('What is the size of B ?\n'))

    side_c = sqrt((side_a ** 2) + (side_b ** 2))
    print(f'The size of side C is {side_c}')

elif wanted_side == 'b':
    side_a = int(input('What is the size of A ?\n'))
    side_c = int(input('What is the size of C ?\n'))

    side_b = sqrt((side_a ** 2) + (side_c ** 2))
    print(f'The size of side B is {side_b}')

elif wanted_side == 'a':
    side_b = int(input('What is the size of B ?\n'))
    side_c = int(input('What is the size of C ?\n'))

    side_a = sqrt((side_b ** 2) + (side_c ** 2))
    print(f'The size of side A is {side_a}')

else:
    print('Invalide Values, please try again.')

######################################################################################################
#B

from math import sqrt

print('QUADRATIC EQUATIONS CALCULATOR\n\n')

a = float(input('Inser the value of A\n'))
b = float(input('Inser the value of B\n'))
c = float(input('Inser the value of C\n'))

delta = (b ** 2) - 4 * a * c

if delta > 0:
    x = (-b + sqrt(delta)) / 2 * a
elif delta < 0:
    print('there is no real value for this equation')
else: #For delta < 0
    x = (-b / 2 * a)

print(f'O valor de x é {x}')

#######################################################################################################
#C

a = int(input('First side value:\n'))
b = int(input('Second side value:\n'))
c = int(input('Third side value:\n'))

perimeter = (a + b + c) / 2

#Existence conditions for a triangle
if a+b>=c and b+c>=a and c+a>=b:
    print ('You have a real triangle, now lets calculate its area')
    area = (perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c) )
    print (f'The area of the triangle is {area}')
else:
    print('Invalide Triangle')

###########################################################################################################
#D

g = float(9.8)
t = float(3)

d = (1/2) * g * t ** 2

print(f'The distance is {d}')

##############################################################################################################
#E

m = float(0.0000005)
c = float(299792458)

e =  m * c ** 2

print (f'Distace: {e}')
    
