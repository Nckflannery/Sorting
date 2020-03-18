# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge( arr, l, r ):
#     # counter for arrA
#     i = 0
#     # counter for arrB
#     j = 0
#     # counter for arrC
#     k = 0
#     # Traverse the arrays
#     while i < len(l) and j < len(r):
#       # If element from left array is less than right
#       if l[i] < r[j]:
#         # Insert element from left array
#         arr[k] = l[i]
#         # Increment counters
#         k += 1
#         i += 1
#       # If element from right array is less than left
#       elif r[j] < l[i]:
#         # Insert element from right array
#         arr[k] = r[j]
#         # Increment counters
#         k += 1
#         j += 1
    
#     # Will still be missing elements because of how the
#     # Counters are set up, add them here:
#     while i < len(l):
#       arr[k] = l[i]
#       k += 1
#       i += 1
#     while j < len(r):
#       arr[k] = r[j]
#       k += 1
#       j += 1
#     return arr

## BETTER VERSION
def merge(arrA, arrB):
    i, j = 0, 0
    output = []
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            output.append(arrA[i])
            i += 1
        else:
            output.append(arrB[j])
            j += 1
    output += arrA[i:]
    output += arrB[j:]
    return output

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) > 1:
      m = len(arr) // 2
      l = merge_sort(arr[:m])
      r = merge_sort(arr[m:])
      return merge(l, r)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    arr2_start = mid + 1; 
  
    if arr[mid] <= arr[arr2_start]: 
        return
      
    while start <= mid and arr2_start <= end: 
  
        if arr[start] <= arr[arr2_start]: 
            start += 1; 
        else: 
            value = arr[arr2_start]; 
            index = arr2_start; 
  
            while index != start: 
                arr[index] = arr[index - 1]; 
                index -= 1; 
              
            arr[start] = value; 

            start += 1; 
            mid += 1; 
            arr2_start += 1; 
     

def merge_sort_in_place(arr, l, r): 
    
    if l < r:
      m = (l + r)//2
      merge_sort_in_place(arr, l, m)
      merge_sort_in_place(arr, m+1, r)
      merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
