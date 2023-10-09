# Python code to clone or copy a list
# Using list comprehension
lst = [4, 8, 2, 10, 15, 18]
li_copy = [i for a,i in enumerate(lst)]
print("Original List:", lst)
print("After Cloning:", li_copy)