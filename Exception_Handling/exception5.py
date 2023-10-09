try:
    print(10/0)
except ZeroDivisionError as msg:
    print('Description Exception:', msg)
    print('Exception Raised:', msg.__class__.__name__)
    print('Exception Raised: ',msg.__class__)
    print('Exception Raised: ',type(msg).__name__)