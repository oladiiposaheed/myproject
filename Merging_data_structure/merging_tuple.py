l1 = (10, -12, 'Python', 20, 30)
l2 = (54, 'Data Science', 23, 1, 90)
#l3 = l1 + l2
l3 = (*l1, *l2)
print(l3)