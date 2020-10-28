#Original alogrithm that merges two sorted lists
def mergeSorted(aList,bList):
    a = 0
    b = 0
    newList = []
    while a < len(aList) and b < len(bList):
        if aList[a] < bList[b]:
            newList.append(aList[a])
            a += 1
        else:
            newList.append(bList[b])
            b += 1
    if a <len(aList):
        newList.extend(aList[a:])
    else:
        newList.extend(bList[b:])
    return newList

#NON - RECURSIVE subroutine
def mergeSort(toSort):
    multList = []
    for i in range(len(toSort)):
        multList.append([toSort[i]])

    while len(multList) != 1:
        location = 0
        #Calls the function "mergeSorted" on first every pair of lists
        while location < len(multList)-1:
            listTemp = mergeSorted(multList[location],multList[location+1])
            #Replaces first item with now sorted pair
            multList[location] = listTemp
            #Removes second item (unnecessary, already in the list as part of the first item)
            del multList[location+1]
            location += 1

    #The index is necessary to remove the double sqaure brackets
    return multList[0]
