# -*- coding: utf-8 -*-
#1
def reverse (sentence, reverse_word):
    try:
        r_word = int(reverse_word)
        print("Invalid input")
    except:
        if sentence.count(reverse_word) > 0:
            reverse_word1 = reverse_word[::-1]
            place1 = sentence.find(reverse_word)
            lw = len(reverse_word)
            new_sen = (sentence[:place1] + reverse_word1 + sentence[place1+lw:])
            return print(new_sen)
        else:
            return print("No match word found")




