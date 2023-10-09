def merge_sort(arr):
    if len(arr) <= 1:
        return 1
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b, arr):
    len_a = len(a)
    len_b = len(b)

    while i < len_a and j < len_b:
        if a[i] <= b[j]


arr = [32, 3, 4, -100, 0, -5, 3, 99, 5, 2, 7, 4, 10]