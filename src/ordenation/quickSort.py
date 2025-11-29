# Quick Sort

arr = [3,6,4,5,1,7,2]

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        print(f"Pivot: {pivot}, \n Left: {left}, \n Middle: {middle}, \n Right: {right}")
        return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(arr))

