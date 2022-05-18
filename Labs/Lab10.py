original_word = 'home'
while True:
    next_word = input("Please insert the next word:\n")
    if len(next_word) == 4:
        counter = 0
        w1 = set(original_word)
        w2 = set(next_word)
        if len(w1 - w2) == 1:
            print("it is correct")
            original_word = next_word
        else:
            print("Game Over!")
    else:
        print("Game Over!")
        break