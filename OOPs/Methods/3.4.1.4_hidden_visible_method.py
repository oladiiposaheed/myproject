class Classy:
    def visible(self):
        print('Visible')

    def __hidden(self):
        print('Hidden')

obj = Classy()
obj.visible()
#obj._Classy__hidden()
try:
    obj.__hidden()
except:
    print('Failed')

obj._Classy__hidden()