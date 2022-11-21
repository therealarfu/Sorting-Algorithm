from sort import *

print(f"Sorting test\n{'='*20}")
while True:
    s = str(input('Insert a list ex:"4 5 2... >"'))
    a = s.split(" ")
    e = int(input(f"Insert the algorithm:\nQuickSort > 0\nMergeSort > 1\nInsertionSort > 2\nSelectionSort > 3\nBubbleSort > 4\n>>> "))
    print(f'{"=" * 20}\nYour list: {s}')
    z = ['quickSort(a)', 'mergeSort(a)', 'insertionSort(a)', 'selectionSort(a)', 'bubbleSort(a)']
    eval(z[e])
    print(f"Sorted list: {' '.join(a)}")
    print("=" * 20)
