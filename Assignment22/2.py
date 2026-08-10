"""
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
"""
s = input("Enter headline: ")

words = s.split()

max_word = ""
max_count = 0

for word in words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        max_word = word

print(max_word)

      