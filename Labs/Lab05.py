total = 0
choice = 0

while choice == 0:
    quant = int(input('Please Insert the quantity:\n'))
    price = int(input('Please Insert the price:\n'))
    calculator = quant * price
    total = total + calculator

    choice = int(input('Do you want to add more produts? \n0 - Yes \n1 - No \n'))
if choice == 0:
    print('')
else:
    print(f'Total cost = {total} ')
    
