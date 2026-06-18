my_name = "Awongo Fahadi Rashid"
my_age = 21
my_info = "My name is {} and I am {} years old.".format(my_name, my_age)
print(my_info)


txt = "  Hello,                 Uganda!  "
words = txt.split()
print(words)
cleaned_txt = " ".join(words)
print(cleaned_txt)

print(cleaned_txt.upper())


y = "I am a proudly Ugandan"
# second, third and fourth characters without spaces considered
z = y.strip()
print(z[1:5])


# removing the double quotes from the string
x = 'All "Data scientists" are cool'
z = x.replace('"', '')
print(z)

