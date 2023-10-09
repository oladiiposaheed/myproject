# Demonstrating the list() function:
print(list("abcabc"))

print('abcacc'.count('b'))
print('abcabc'.count("d"))

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)

#print(chr(ord('character')) == 'character')

a = """
"""
print(a)
print(""" """)

for ch in "abc":
    print(chr(ord(ch) + 1), end='')

for od in 123:
    print(ord(chr(od)))