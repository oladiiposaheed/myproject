try:
    x = int('12.5')
except BaseException as msg:
    print('Description Exception:', msg)
    print('Exception Raised:', msg.__class__.__name__)
    print('Exception Raised: ',msg.__class__)
    print('Exexception6'
          'ception Raised: ',type(msg).__name__)