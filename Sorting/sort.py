#Sort Algorithm Module by Arfur


def quickSort(list, init=0, end=None):
    if end is None: end = len(list) - 1
    if init < end:
        pivot = list[end]
        i = init
        for j in range(init, end):
            if list[j] <= pivot:
                list[j], list[i] = list[i], list[j]
                i += 1
        list[i], list[end] = list[end], list[i]
        pivot = i
        quickSort(list, init, pivot - 1)
        quickSort(list, pivot + 1, end)


def mergeSort(list, init=0, end=None):
    if end is None: end = len(list)
    if end - init > 1:
        pivot = (end + init) // 2
        mergeSort(list, init, pivot)
        mergeSort(list, pivot, end)
        left, right = list[init:pivot], list[pivot:end]
        y1, y2 = 0, 0
        for i in range(init, end):
            if y1 >= len(left):
                list[i] = right[y2]
                y2 += 1
            elif y2 >= len(right):
                list[i] = left[y1]
                y1 += 1
            elif left[y1] < right[y2]:
                list[i] = left[y1]
                y1 += 1
            else:
                list[i] = right[y2]
                y2 += 1


def bubbleSort(list, init=0, end=None):
    if end is None: end = len(list)
    if init < end:
        for i in range(init, end):
            for c in range(init, end - 1):
                if list[c] > list[c + 1]: list[c], list[c + 1] = list[c + 1], list[c]


def insertionSort(list, end=None):
    init = 1
    if end is None: end = len(list)
    if init < end:
        for i in range(init, end):
            for c in range(i, 0, -1):
                if list[c] < list[c-1]: list[c], list[c-1] = list[c-1], list[c]


def selectionSort(list, init=0, end=None):
    mini = j = 0
    i = init
    if end is None: end = len(list)
    if init < end:
        for c in range(init, end):
            for v in range(i, end):
                if list[v] < mini or v == i:
                    mini = list[v]
                    j = v
            list[j], list[c] = list[c], list[j]
            i += 1



