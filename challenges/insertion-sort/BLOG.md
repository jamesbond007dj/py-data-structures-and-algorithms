## Insertion Sort
Insertion sort is a type of sorting algorithm. We compare values of each indexes of an array and  then first we swap the the smallest value with the value of first index[0]. Then we compare values of each indexes but now we start to check from index[1] and we swap the smallest value with index[1]. We make this process until last index of array is completed and it means whole array is sorted. 

## Pseudocode

 InsertionSort(int[] lst)

    For i = 1 to len(lst)

      int j <-- i - 1
      int temp <-- lst[i]

      While j >= 0 AND temp < lst[j]
        lst[j + 1] <-- lst[j]
        j <-- j - 1
      lst[j + 1] <-- temp

## Trace
#### arr = [8, 2, 10, 9, 12]

### First attemp 

The smallest value is 2 and we swap it with index0

temp1 = [2,8,10,9,12]

### Second attemp
Now we are comparing the values starting from index[1]
The smallest value is 8 and smallest is index1 we swap it with itself technically 

temp2 = [2,8,10,9,12]

### Third attemp
Now we are comparing the values starting from index[2]
The smallest value is 9 and smallest is index1 and we swap it with index2

temp3 = [2,8,9,10,12]

### Forth attemp
Now we are comparing the values starting from index[3]
The smallest value is 10 and smallest is index1 we swap it with itself technically 

temp4 = [2,8,9,10,12]

### Fifth attemp
Now we are comparing the values starting from index[4]
The smallest value is 10 and smallest is index1 we swap it with itself technically 

temp5 = [2,8,9,10,12]

#### Sorted array: [2,8,9,10,12]
Actually we get the sorted array in third attemp in this example , however our function will do the process as the length of array. 

## Big O 
* Time complexity Big O(n^2)
* Space complexity Big O(1)

