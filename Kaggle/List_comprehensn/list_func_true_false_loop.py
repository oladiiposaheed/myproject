def elementwise_greater_than(L, thresh):
    lst = []
    for l in L:
        if l > thresh:
            lst.append(l)
            print(True)
            #return True
    print(False)
    #return False
elementwise_greater_than([1, 2, 3, 4], 2)