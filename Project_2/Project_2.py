import string

name_file = input("Insert the name of the file:\n")
try:
    text = open(f"{name_file}", "r")
    dictionary = dict()

    for line in text:
        line = line.strip(" ")
        line = line.upper()

        line = line.translate(line.maketrans("", "", string.punctuation))

        words = line.split()

        for word in words:
            if word in dictionary:
                dictionary[word] = dictionary[word] + 1
            else:
                dictionary[word] = 1

    for key in list(sorted(dictionary.keys())):
        print(key.upper(), "->", dictionary[key])
except:
    print ("File not found")


