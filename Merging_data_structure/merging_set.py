s1 = [10, -12, 'Python', 20, 30]
s2 = (54, 'Data Science', 23, 1, 90)
s3 = {'We', 'Django'}
#l3 = l1 + l2
s4 = (*s1, *s2, *s3)
lst = [*s1, *s2, *s3]
print(s4)
print(lst)