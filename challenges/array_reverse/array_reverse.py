# def Reverse(arr):
#     return [i for i in reversed(arr)]


# arr = [1, 5, 8, 10]
# print(Reverse(arr))

# Above Method 1 : Using the reversed() built in function. I learnt it from geeksforgeeks.org


# def Reverse(arr):
#     arr.reverse()
#     return arr

# arr = [1, 5, 8, 10]
# print(Reverse(arr))

# Above Method 2 : Using the reverse() built in function. I learnt it from geeksforgeeks.org

def Reverse(arr):
    new_arr = arr[::-1]
    return new_arr

arr = [1, 5, 8, 10]
print(Reverse(arr))

# Above Method 3 : reversing an array using slicing tech. I learnt it from geeksforgeeks.org

