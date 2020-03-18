def quicksort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        left = []
        right = []
        for i in data[1:]:
            if i <= pivot:
                left.append(i)
            else:
                right.append(i)
    return quicksort(left) + [pivot] + quicksort(right)


# Test
arr = [-4, 2, 4, 5, 1, -2, -15, 0, 12, 9, 6]
print(quicksort(arr))