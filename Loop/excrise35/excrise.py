# Exercise 35. Perfect number check
n=7
d=0
for i in range(1,(n//2)+1):
    if n%i==0:
        d+=i
if d==n:
    print(f"prefect num {d}")
else:
    print(f"{d} is not prefect num")
