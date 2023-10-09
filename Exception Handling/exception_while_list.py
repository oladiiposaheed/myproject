the_list = [1, 222, 13, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
        if ix == 3:
            break
    except IndexError:
        do_it = False
print('Done')