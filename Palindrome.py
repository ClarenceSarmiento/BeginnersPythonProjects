# Palindrome

""" A string or number is called a palindrome when its reverse
is the same as the original one, for example '9009'. """

word = str(input(":: ")).lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
