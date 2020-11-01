inputList = [1, 100, 2, 56, 7, 95]

def bubbleSort(toSort):
    swaps = 1
    listLength = len(toSort)
    passes = 0
    while swaps != 0 and passes < listLength:
        swaps = 0
        for i in range(listLength-passes-1):
            if toSort[i] > toSort[i+1]:
                toSort[i],toSort[i+1] = toSort[i+1],toSort[i]
                swaps += 1
        passes += 1
    return toSort
