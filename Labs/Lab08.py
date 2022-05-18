list = []

while True:
    list_el = input('Please insert a record, press enter key without any value to finish:\n')
    if list_el == "":
        break
    else:
        list.append(list_el)

list = sorted(list)

print ('Here is the first list')
print (list)

duplicated_elements = []

for x in list:
    if list.count(x) > 1:
        duplicated_elements.append(x)

print ('Here is the list - duplicated records')

print (set(sorted(duplicated_elements)))

unique_elements = []

for x in list:
    if list.count(x) == 1:
        unique_elements.append(x)

print ('Here is the list - unique records')

print (set(sorted(unique_elements)))

print ('Here is the list – all elements without duplication:')

print (set(sorted(list)))

