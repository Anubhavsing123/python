# Reverse the order of words in a given sentence, but keep the characters within the words in their original order.
str1 = "Python is fun"
s2=str1.split(" ")
print(s2)
s2=s2[::-1]
print(" ".join(s2))