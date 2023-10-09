from datetime import time

t = time(14, 53, 20, 100000)

print('Time:', t)
print('Hour:', t.hour)
print('Minute:', t.minute)
print('Second:', t.second)
print('Microsecond:', t.microsecond/60)