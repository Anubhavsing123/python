# Write a program to find the longest word in a given sentence. If there is a tie, return the first one found.
str1 = "The quick brown fox jumps over the lazy dog"
word =str1.split(" ")
s=""
print(word)
for w in word:
    
    if len(w)>len(s):
        s=w
print(s)