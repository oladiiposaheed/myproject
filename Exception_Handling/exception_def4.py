def cal():
    try:
        return 'python is simple'
    except:
        return 200
    finally:
        u = 12
        t = 4.7
        g = 10
        h = u*t + 0.5*g*t**2
        return 'The maximum height of the object = {}m'.format(h)
print(cal())