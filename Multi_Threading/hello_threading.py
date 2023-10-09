import threading

def greet(n):
    print("Hello, how old are you?", n)

t1 = threading.Thread(target=greet, args=(18,))
t1.start()
t1.join()
#t2.start()
print('Thank You')