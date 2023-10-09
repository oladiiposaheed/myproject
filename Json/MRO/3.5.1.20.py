class Top:
    def m_top(self):
        print('Top')

class Middle(Top):
    def m_middle(self):
        print('Middle')

class Bottom(Top, Middle):
    def m_bottom(self):
        print('Bottom')

obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()