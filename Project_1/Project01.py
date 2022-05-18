#Project 01 - Prime Number Check
#Luis Santos

n= 0
try:
    number = int(input('Please insert a number:\n'))
    if number < 1 or number > 500:
        print ('Invalid Value')
    elif number == 1:
        print ('1 is neither a prime or composite number.')
    else: 
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                n += 1

        if n == 2:
            print('This number is a Prime number')
        else:
            print('This number is a composite number')

except:
    print('Invalid Value')    
