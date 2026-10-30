#: Given a filename as a string, extract only the file extension (e.g., .png or .pdf).
file_name = "report_final_v2.pdf"
str1=file_name.split(".")
print(str1[-1])
str2=file_name.rfind(".")
str3=file_name[str2+1:]
print(str3)