#Exercise 20. Write a Python program to find the key associated with the smallest numerical value in a dictionary.
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
m=min(stock,key=stock.get)



print(m)
