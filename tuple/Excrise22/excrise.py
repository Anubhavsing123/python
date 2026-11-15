# Problem Statement: Write a recursive Python function to flatten a deeply nested tuple of tuples into a single flat tuple containing all the individual values.
nested = (1, (2, 3), (4, (5, (6, 7))))
def flatter(t):
    for item in t:
        if isinstance(item,tuple):
            yield from flatter(item)
        else:
            yield item
res=tuple(flatter(nested))
print(res)