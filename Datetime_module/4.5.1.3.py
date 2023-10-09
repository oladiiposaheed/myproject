from datetime import date
import time

timestamp = time.time()
print('Timestamp:', timestamp, 'seconds')

d = fromtimestamp(timestamp)
print('Date:', d)