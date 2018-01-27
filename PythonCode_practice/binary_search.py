"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def recur_bsearch(arr,st, end, val):
    index = None
    if st == end:
        if arr[st] == val:
            index = st
        else:
            index = -1
    else:
        l = (st+end)/2
        mid = arr[l]

        if mid == val:
            index = l
        elif mid > val:
            end = l
        elif mid < val:
            st = l+1
    if index is None:
        index = recur_bsearch(arr,st,end,val)

    return index




def binary_search(input_array, value):
    start = 0
    end = len(input_array)-1
    index = recur_bsearch(input_array,start,end,value)

    return index

test_list = [1,3,9,11,15,19,29]
test_val1 = 0
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)