birthday = input("Enter your birthday in this format, YYYYMMDD, or YYYYDDMM, or MMDDYYYY:\n").strip()
birthday1 = 0
answer = 0
if len(birthday) != 8 or not birthday.isdigit():
    print(f"Your date of {birthday} is invalid!")
else:
    for num in birthday:
        birthday1 += int(num)
    if birthday1 > 10:
        for x in str(birthday1):
            answer = answer + int(x)
        print(f"Your digit of life is: {answer}")
    else:
        print(f"Your digit of life is: {birthday1}")
        
