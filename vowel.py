# ask for user input (their name)
name = str(input("Please enter your name: "))
def vowel(name): # define(def) function
    for x in name.lower():
        for letter in ['a', 'e', 'i', 'o', 'u']:
            if x == letter:
                return "Your name has a vowel"
    return "Your name does not have a vowel"
print(vowel(name))

# made and called a function to say if user's name has a vowel or not
