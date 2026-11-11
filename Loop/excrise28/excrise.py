# Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.
scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60} 
threshold = 75
p={}
for k,v in scores.items():
    if v>=threshold:
        p[k]=v
print(f"passing {p}")