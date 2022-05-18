sum_num = 1
while sum_num < 2:
    list_number = []
    number = int(input('Insert the first number:\n'))
    list_number.append(number)
    number = int(input('Insert the second number:\n'))
    list_number.append(number)

    sum_num = sum(list_number)

    n = int(input('Size of your list: '))

def fibseq(n):
    for number in range(2, n):
        l = len(list_number)
        list_number.append(list_number[l-1] + list_number[l-2])
    return list_number
print (fibseq(n))
