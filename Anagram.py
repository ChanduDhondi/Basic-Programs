"""Anagram-Checking of the entered Word is Anagram or not"""

first_word = list(input("enter first word :"))
second_word = list(input("enter second word :"))

first_word.sort()
second_word.sort()
i = 0
if len(first_word) ==  len(second_word):
    while i < len(second_word):
       if first_word[i] == second_word[i]:
          i += 1
    print("Anagram")
else:
    print("Not and Anagram")


