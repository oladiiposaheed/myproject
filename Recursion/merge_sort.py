def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #Merge
        i = 0  #initialize left array index
        j = 0  #initialize right array index
        k = 0  #merge array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:   # check if left array element is less than the right array element
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[i]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 9, -3, 6, -8, 10]
merge_sort(arr)
print(arr)