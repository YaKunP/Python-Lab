# The function for sorting elements in ascending order
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimun in the list[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i

    for j in range(i + 1, len(lst)):
        if currentMin > list[j]:
            currentMin = lst[j]
            currentMinIndex = j

    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
        lst[currentMinIndex] = lst[i]
        lst[i] = currentMin

