print("Welcome to the Anagrams Program Checker:")
anagrams = []

userinput = input("Enter the first of two words: ").lower().strip()
userinput1 = input("Enter the second word: ").lower().strip()

if len(userinput) != len(userinput1):
    print("Not anagrams")
else:
    for letter in userinput:
        if letter in list(userinput1):
            anagrams.append(letter)
    if len(anagrams) == len(userinput1):
        print("Anagrams")
    else:
        print("Not anagrams")
    
# ANOTHER METHOD WOULD BE TO:

# str1 = input("Enter first text: ")    
# str2 = input("Enter second text: ")

# strx1 = ''.join(sorted(list(str1.upper().replace(' ',''))))
# print(strx1)
    
    







