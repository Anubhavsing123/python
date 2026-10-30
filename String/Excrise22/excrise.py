# Given a list of strings, remove any empty strings or None values from it.
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res = []

for ch in str_list:
    if ch != "" and ch is not None:
        res.append(ch)

print(res)

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str_list = [ch for ch in str_list if ch is not None and ch != ""]

print(str_list)
#filter 
tr_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original list of strings:", str_list)

# use filter() to remove None and empty strings
# filter(None, sequence) removes all falsy values
new_str_list = list(filter(None, str_list))

print("After removing empty strings:", new_str_list)