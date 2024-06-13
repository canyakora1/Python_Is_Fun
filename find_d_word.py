first_word = input("Enter the first word: ").lower().strip()
second_word = input("Enter the second word: ").lower().strip()

found = True
start = 0

# Iterate all words from first word and use it on the second word
for x in first_word:
    position = second_word.find(x, start)
    if position < 0:
        found = False
        break
    start = position + 1
if found:
    print("Yes")
else:
    print("No")
            
                 