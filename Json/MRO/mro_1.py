class Top:
    def m_top(self):
        print('top')

class Middle(Top):
    def m_middle(self):
        print('middle')

class Bottom(Middle):
    def m_bottom(self):
        print('bottom')

obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()