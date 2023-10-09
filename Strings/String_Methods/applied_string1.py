for ch in 'abCdEFgH123XYX':
    if ch.isalnum():
        print(ch.swapcase(), end='')
    elif ch.startswith('ab'):
        print(ch.title(), end='')
    elif ch.endswith('YX'):
        print(ch.lower(), end='')
    else:
        print(ch, end='')