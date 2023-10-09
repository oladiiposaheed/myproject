class Left:
    var = 'L'
    var_left = 'LL'
    def fun(self):
        return 'LEFT'

class Right:
    var = 'R'
    var_right = 'RR'
    def fun(self):
        return 'RIGHT'

class Sub(Right, Left):
    pass
obj = Sub()
print(obj.var)
print(obj.var_left)
print(obj.var_right)
print(obj.fun())
print(obj.var, obj.var_left, obj.var_right, obj.fun())