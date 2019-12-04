def insert_shift_array(arr, val):
    if len(arr) %2 == 1:
        mid = len(arr) //2 + 1
        new_arr = arr[:mid]+[val]+arr[mid:]
        return new_arr

    if len(arr) %2 == 0:
        mid = len(arr) // 2
        new_arr = arr[:mid]+[val]+arr[mid:]
        return new_arr
