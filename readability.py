# TODO
# Count the number of letters
# spaces should count as a word
# FORMULA : 0.0588 * L - 0.296 * S - 15.8
# L is the average number of letters per 100 words
# S is sentences per 100 words
# Count the number of lowercase and uppercase letters in text ++
# Count the total letters ++ 
# Count the words in input ++
# Words means any seperated with whitespace ++
# Calculate the L
# Calculate the S
from cs50 import get_string

text = get_string("Text: ")
countlower = 0
countupper = 0
countspace = 0
countsentence = 0

for i in text:
    if i.islower():            # kucuk harfleri hesapliyor
        countlower += 1
    elif(i.isupper()):
        countupper += 1          # buyuk harfleri hesapliyor
    elif i == " ":
        countspace += 1          # bosluklari hesapliyor 
    elif i == "." or i == "!" or i == "?":
        countsentence +=1


totalLetters = countlower + countupper
totalWords = 1 + countspace     # bosluk sayisinin 1 fazlasi mantiken cumledeki kelime sayisini verecektir

L = 100 * totalLetters / totalWords
S = 100 * countsentence /totalWords
result = round((0.0588 * L) - (0.296 * S) - 15.8)

if result > 16:
    print("Grade: 16+")
elif result < 1:
    print("Before Grade 1")
else:
    print(f"Grade: {result}")