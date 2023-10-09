f1 = open('img.png', 'rb')
f2 = open('newImg.png', 'wb')
data = f1.read()
f2.write(data)