def binary_search (lst, key):
    start = 0
    stop = len(lst)
    try:
        while True :
            middle = (start+stop) // 2
            if lst[middle] == key :
                return middle
            elif lst[middle] > key:
                stop = middle -1
            elif lst[middle] < key:
                start = middle + 1
    except:
        return -1
