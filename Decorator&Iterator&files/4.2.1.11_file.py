import errno

try:
    s = open('c:/users/user/Desktop/file.txt', 'rt')
    s.close()

except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is: {}".format(exc.errno))