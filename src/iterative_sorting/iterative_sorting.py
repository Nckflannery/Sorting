# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    le = len(arr)
    # loop through n-1 elements
    # le - 1 because the last element SHOULD be in place by the time
    # we get there based on the previous sorting
    for i in range(le - 1):
        # cur_index = i  # THIS CAN BE 1 LINE
        # smallest_index = cur_index
        smallest_index = i
        # range(i, le) to only iterate on items not sorted yet
        for x in range(i, le):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# Is this a select sort?
def select_sort_ish(arr):
    new = []
    # Copy array to avoid removing items from original later
    old = arr.copy()
    for _ in range(len(old)):
        i = min(old)
        new.append(i)
        old.remove(i)
    return new

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    le = len(arr)
    # Loop through all indices
    for i in range(le):
        # len - i because we are "moving" through the list
        # i.e. if le = 6 and we are at index 4 only 2 items remain
        # then -1 because x+1 on last element will be out of range 
        for x in range(le - i - 1):
            # If left element is greater than right element
            if arr[x] > arr[x+1]:
                # swap
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr ):
    if arr == []:
        return []
    for i in arr:
        if i < 0:
            return 'Error, negative numbers not allowed in Count Sort'
    # First, find largest element
    largest = max(arr)
    # Create array of 0's that is largest + 1 in size
    output = [0] * (largest+1)
    # Create array for counts of each element in arr
    counter = [0] * (largest+1)
    # Count number of times each element appears
    for i in range(len(arr)):
      counter[arr[i]] += 1
    # Cumulative sum of counts of elements
    for i in range(1, len(counter)):
      counter[i] += counter[i-1]
    # Start from right inserting elements based on count    
    i = len(arr) - 1
    while i >= 0:
      # Place highest number at right most end of output
      output[counter[arr[i]] - 1] = arr[i]
      # Remove 1 from the count of that number
      counter[arr[i]] -= 1
      # 1 item down, reduce i by 1
      i -= 1
    # Now output has sorted list but also has 0's from 
    # numbers that were not used so....
    output = [output[i] for i in range(len(arr))]
    return output