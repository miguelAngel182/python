"""
pseudocode

start is_palindrome(word)
    reverse_word = word[::-1]
    if(reverse_word == word)
        return True
    else
        return False
end

ask for word
print(is_palindrome(word))
"""

def is_palindrome(word):
    reverse_word = word[::-1]
    if(reverse_word == word):
        return True
    else:
        return False

word = str(input("Enter a word: "))
print(is_palindrome(word))