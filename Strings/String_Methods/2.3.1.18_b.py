def mysplit(strng):
    #
    # put your code here
    #
    lst = []
    if strng == '':
        return lst
    else:
        for i in strng:
            lst.append(i)
            return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))