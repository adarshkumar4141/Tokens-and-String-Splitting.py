# Tokens in Python:
# Tokens are the smallest individual units of a Python program that have meaning to the Python interpreter.
# In simple words, when we write Python code, it is divided into small parts called tokens.

# age=20
# print(age)

# To see all Python keywords:

# import keyword
# print(keyword.kwlist)

# text="Python is easy"
# tokens=text.split()
# print(tokens)
# print(len(tokens))

# Split():-
# The split() method in Python is used to divide a string into smaller parts and convert those parts into a list.
# It is a built-in string method.
# text="  Python is easy  "
# print(text.split())

# text="apple,banana,mango"
# print(text.split(","))
# print(text.split())

# date="20-10-2026"
# print(date.split("-"))

# a="I am Aditya Raj"
# print(a)
# print(type(a))
# b=a.split()
# print(b)
# print(type(b)) split always gives list data type.

# print("2027-10-30".split("-"))
# print("one|two|three".split("|"))
# print("Name:Rahul".split(":"))

# k="a,,b,"
# print(k.split(","))

# p="a  b"
# # print(p.split())
# print(p.split(" "))

# split with Maxsplit:
# k="Rajputana is come from Rajasthan"
# print(k.split())
# print(k.split(" ",1))

# text="Python is very easy"
# print(text.split(" ",1))
# print(text.split(" ",2))
# print(text.split(" ",3))
# print(text.split(" ",4))

# a="I am Adarsh Singh"
# print(a.split())
# print (a.split(" ",1))
# print(a.split(" ",2))

# rsplit() in Python:
# rsplit() means Right Split.
# It splits a string starting from the right side (end).

# a="banana,mango,guava,papaya"
# print(a.rsplit(",",1))
# print(a.rsplit(",",2))
# print(a.rsplit(",",3))
# print(a.rsplit(",",0))

# a = "apple,banana,mango,orange"
# print(a.rsplit(",", 2))

# text="one-two-three-four"
# print(text.rsplit("-",1))
# print(text.rsplit("-",2))
# print(text.rsplit("-",3))

# filename="AdarshResume.pdf"
# a=filename.rsplit(".",1)
# print(a)
# print(a[1])

# splitlines() in Python:
# splitlines() is a Python string method used to split a string into a list of lines.
# It splits the string wherever a line break occurs.

# a="Hello\nPython\nJava"
# print(a.splitlines())

# a="""Apple
# Mango
# Banana
# pineapple"""
# print(a.splitlines())


# strip in python:
# The strip() method in Python is a string method used to remove 
# unwanted characters (especially spaces) from the beginning and end of a string.

# name="  Adarsh  "
# print(name.strip())

# a="  Hello  "
# print(a.strip())

# text="xypythonyx"
# print(text.strip("xy"))

# text="   Hello python   "
# print(text.strip())

# text="wwHelloIndianww"
# print(text.strip("ww"))

# print("banana".strip("an"))
# print("www.python.org".strip("w.org"))

# lstrip() – Removes from the left side
# a="  QuadAi  "
# print(a.strip())
# print(a.lstrip())

# text="   Python   "
# print(repr(text.lstrip()))


# k="kkAdarshchauhankk"
# print(k.strip("kk"))
# print(k.lstrip("kk"))

# 3. rstrip() – Removes from the right side
# a = "   Hello   "
# print(a.strip())
# print(a.rstrip())

# text="   Python   "
# print(repr(text.rstrip()))

# b="hhIndianCrickethh"
# print(b.strip("hh"))
# print(b.lstrip("hh"))

# text = "\n\t  Python  \t\n"
# print(repr(text.strip()))

# Replace Method:
# The replace() method is a Python string method used to replace one character or word with another character or word in a string.

# a="I like python"
# print(a.replace("python","java"))

# k="banana"
# print(k.replace("a","o"))

# a="Apple Gauva strawberry"
# print(a.replace("Gauva","Mango"))

# a = "apple apple apple"
# print(a.replace("apple", "mango", 2))

# k="Adarsh singh Chauhan"
# print(k.replace("Adarsh","Ayush",1))

# Partition Method:
# The partition() method is used to divide a string into exactly three parts based on a separator.
# It returns a tuple containing three elements:
# a="Hello World"
# print(a.partition(" "))

# k="Python-Programming"
# print(k.partition("-"))

# a = "Hello World"
# print(a.partition("-"))

# rpartition() Method:
# In simple words, it searches for the separator from the right side and divides the string at its last occurrence.

# a="apple-mango-grapes"
# print(a.partition("-"))
# print(a.rpartition("-"))

# a = "Python-is-a-programming-language"
# print(a.rpartition("-"))
# print(a.partition("-"))

# student = "Rahul:20:BCA"
# name,separator,details = student.partition(":")
# print(name)
# print(separator)
# print(details)

# Some more methods:-

# text="python"
# print(text.startswith("py"))
# text="Adarsh"
# print(text.endswith("sh"))




