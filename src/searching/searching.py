# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
  
  low = 0
  high = len(arr)-1

  while low <= high:

    mid_index = (high - low) // 2
    if arr[mid_index] == target:
      return mid_index
    elif arr[mid_index] < target:
      low = mid_index
    elif arr[mid_index] > target:
      high = mid_index 

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  
  if arr[middle] == target:
    return middle
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle, high)
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle)
  else:
    return -1
