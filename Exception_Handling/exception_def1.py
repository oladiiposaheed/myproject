def f1():
    try:
        return 100
    except:
        return 200
    finally:
        a = 10
        b = 4
        return a**b, 40, 60, 'python'.title(), 12, 'data science'.istitle()
print(f1())