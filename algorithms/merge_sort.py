
def merge(left, right):
    """Merge sorted lists"""
    merged_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        print('left[i]: {} right[j]: {}'.format(left[i], right[j]))
        if left[i] <= right[j]:
            print('Appending {} to the merged_list'.format(left[i]))
            merged_list.append(left[i])
            print('merged_list now is {}'.format(merged_list))
            i += 1
            print('i now is {}'.format(i))
        else:
            print('Appending {} to the merged_list'.format(right[j]))
            merged_list.append(right[j])
            print('merged_list now is {}'.format(merged_list))
            j += 1
            print('j now is {}'.format(j))
    print('One of the list is exhausted. Adding the rest of one of the lists.')
    merged_list += left[i:]
    merged_list += right[j:]
    print('merged_list now is {}'.format(merged_list))
    return merged_list

def mergesort(some_list):
    """merge sort"""
    print('---')
    print('mergesort on {}'.format(some_list))
    if len(some_list) < 2:
        print('length is 1: returning the list withouth changing')
        return some_list
    middle = len(some_list) / 2
    print('calling mergesort on {}'.format(some_list[:middle]))
    left = mergesort(some_list[:middle])
    print('calling mergesort on {}'.format(some_list[middle:]))
    right = mergesort(some_list[middle:])
    print('Merging left: {} and right: {}'.format(left, right))
    out = merge(left, right)
    print('exiting mergesort on {}'.format(some_list))
    print('#---')
    return out
