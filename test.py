list1 = [0, 83, 73, 24, 4, 53, 0, 6, 23, 16, 83, 40, 91, 69, 95, 50, 72, 44, 53, 33, 87]
total = len(list1) - 1


def heap_adjust(n, i, array: list):
    while 2 * i <= n:
        left = 2 * i
        max_child_index = left
        if n > left and array[left + 1] > array[left]:
            max_child_index = left + 1
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:
            break


def sort(total, array: list):
    while total > 1:
        array[1], array[total] = array[total], array[1]
        total -= 1
        if total == 2 and array[total] >= array[total - 1]:
            break
        heap_adjust(total, 1, array)
    return array


sort(total, list1)
print(list1)
