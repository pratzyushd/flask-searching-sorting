def binarySearch(searchList, item):
    givenList = searchList
    bottom = 0
    top = len(givenList) - 1
    found = False
    while bottom <= top:
        mid = (top + bottom) // 2
        if searchList[mid] == item:
            found = True
            bottom = mid + 1
        elif searchList[mid] < item:
            bottom = mid + 1
        elif searchList[mid] > item:
            top = mid - 1
    return found
