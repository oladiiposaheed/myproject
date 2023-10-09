str1 = "this is really a string is example....wow!!!"
str2 = "is"
print(str1.rfind(str2))
print(str1.rfind(str2, 0, 10))
print(str1.rfind(str2, 10, 0))
print('*****')
print(str1.find(str2))
print(str1.find(str2, 0, 10))
print(str1.find(str2, 0, 10))

word = 'geeks for geeks'
# Returns highest index of the substring
result = word.rfind('geeks')
print("Substring 'geeks' found at index :", result)
print(word.rfind('geeks', 2))

# Substring is searched in 's for g'
print(word.rfind('for ', 4, 11))

# finding substring using -ve indexing
print(word.rfind('geeks', -5))

print('******************************')
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
