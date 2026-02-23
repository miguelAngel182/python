"""
pseudocode

start vowels(word)
    counter = 0
    for i in range(0,len(word))
        if (word[i] in "aeiou")
            counter += 1
    return counter
end

ask(word)
print(vowels(word))
"""
# X
# def vowels(word):
#     counter = 0
#     for i in range(0, len(word)):
#         if (word[i] == ("a" or "e" or "i" or "o" or "u")): #El operador or retorna el primer valor verdadero. Por lo tanto, este codigo no funciona
#             counter += 1
#     return counter

#✓
# word = str(input("enter a word: "))
# print(vowels(word))

# def vowels(word):
#     counter = 0
#     for i in range(0, len(word)):
#         if (word[i] in "aeiou"):
#             counter += 1
#     return f"number of vowels in {word}: {counter}"

# word = str(input("enter a word: "))
# print(vowels(word))

# Function to count vowels in a string
#The for loop for i in range(0, len(string)) goes through each character in the string, including letters, spaces, and punctuation marks.
def count_vowels(text):
    counter = 0
    for i in range(len(text)):
        if text[i] in "aeiou":
            counter += 1
    return f"Number of vowels in '{text}': {counter}"

text = input("Enter a string: ")
print(count_vowels(text))