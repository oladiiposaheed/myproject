def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s
#print(two_digits(3))
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__hours) + ':' + two_digits(self.__minutes) + ':' + two_digits(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23
timer = Timer(2, 5, 37)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)