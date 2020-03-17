# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arr, l, r ):
    # counter for arrA
    i = 0
    # counter for arrB
    j = 0
    # counter for arrC
    k = 0
    # Traverse the arrays
    while i < len(l) and j < len(r):
      # If element from left array is less than right
      if l[i] < r[j]:
        # Insert element from left array
        arr[k] = l[i]
        # Increment counters
        k += 1
        i += 1
      # If element from right array is less than left
      elif r[j] < l[i]:
        # Insert element from right array
        arr[k] = r[j]
        # Increment counters
        k += 1
        j += 1
    
    # Will still be missing elements because of how the
    # Counters are set up, add them here:
    while i < len(l):
      arr[k] = l[i]
      k += 1
      i += 1
    while j < len(r):
      arr[k] = r[j]
      k += 1
      j += 1
    return arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) > 1:
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]
        merge_sort(l)
        merge_sort(r)
        merge(arr, l, r)
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
