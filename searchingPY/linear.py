def linearSearch(listOfItems,itemToFind,inOrder = False):
    for i in listOfItems:
        if i == itemToFind:
            return True
        elif inOrder:
            if itemToFind < i:
                return False
    return False