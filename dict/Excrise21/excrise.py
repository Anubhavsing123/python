#Write a Python program to find the key associated with the highest numerical value in a dictionary.

scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
l=max(scores,key=scores.get)
print(l)

best_score = max(scores.values())
all_top = [k for k, v in scores.items() if v == best_score]
print("All top scorers:", all_top)