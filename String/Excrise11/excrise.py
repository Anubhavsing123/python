#Check if a given URL starts with “https” and ends with “.com”.
def check(url):
    if url.startswith("https") and url.endswith(".com"):
        return True
    else:
        return False
c=check("hgoogle.com")
print(c)
