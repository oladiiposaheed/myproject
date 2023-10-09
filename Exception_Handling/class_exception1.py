class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg

age = int(input('Old Old Are You: '))
if age > 60:
    raise TooYoungException('Too Old to marry')
elif age < 18:
    raise TooOldException('Too Young to marry')
else:
    print('You will get match details by email soon')