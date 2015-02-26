# Revised vowel caller program.
letters = "qwertyuiopasdfghjklzxcvbnm"

for i in letters:
    # check if i is a vowel
    if i in "aeiou":
        print i + " is a vowel"
    else:
        print i