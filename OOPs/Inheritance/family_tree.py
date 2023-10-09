class Father:
    pass

class Mother(Father):
    pass

class Child(Mother):
    pass

for family1 in [Father, Mother, Child]:
    for family2 in [Father, Mother, Child]:
        print(issubclass(family1, family2), end='\t')
   
