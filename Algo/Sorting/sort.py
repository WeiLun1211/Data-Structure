def BubbleSort(arr):
    arr_length = len(arr)

    for i in range(arr_length):
        for j in range(0, arr_length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            print(arr)

def SelectionSort(arr):
    arr_length = len(arr)

    for i in range(arr_length):
        min = i

        print(arr)
        for j in range(i+1, arr_length):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


def InsertionSort(arr):
    arr_length = len(arr)

    for j in range(1, arr_length):
        key = arr[j]
        i = j-1

        while i >= 0 and key < arr[i]:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key

    print(arr)


def MergeSort(arr):
    return






def main(sort_type):
    match sort_type:
        case 1:
            arr = [-2, 45, 0, 11, -9]
            BubbleSort(arr)
        case 2:
            arr = [20, 12, 10, 15, 2]
            SelectionSort(arr)
        case 3:
            arr = [3, 5, 8, 1, 4, 2]
            InsertionSort(arr)
        case 4:
            arr = [3, 5, 8, 1, 4, 2]
            MergeSort(arr)
    return

print("=======================")
print("== Sorting Alogrithm ==")
print("=======================")

print("1: Bubble sort \n2: Selection sort \n3: Insertion Sort")

sort = int(input("\nSorting Alogo Choose: "))
main(sort)