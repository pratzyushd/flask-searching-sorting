def binarySearch(searchList, item):
    listLength = len(searchList)
    midIndex = listLength//2
    if searchList[midIndex] == item:
        return True
    elif listLength <= 2:
        if listLength == 2:
            return searchList[0] == item
        else:
            return False
    elif item < searchList[midIndex]:
        return binarySearch(searchList[:midIndex], item)
    else:
        return binarySearch(searchList[midIndex+1:], item)