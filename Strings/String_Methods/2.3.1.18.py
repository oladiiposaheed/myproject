def mysplit(strng):
    #
    # put your code here
    #
    lst = []
    if strng == '':
        return lst
    else:
        return strng.split()


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))