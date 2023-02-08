def consecutive_vowels(s):
    vowels = 'aeiouAEIOU'
    for i in range(len(s) - 1):
        if s[i] in vowels and s[i + 1] in vowels:
            return 'Positive'
    return 'Negative'

while True:
    s = input("Please enter a string: ")
    print(consecutive_vowels(s))
    repeat = input("Do you want to check another string? (yes/no) ")
    if repeat.lower() == "no":
        break