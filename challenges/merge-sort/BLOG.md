## Merge Sort
Merge sort breaks a list up into the smaller arrays like dividing half until you get one element arrays than merges these arrays back together in order.

## Pseudocode

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

## Trace
Merge Sort is a stable sort which means that the same element in an array maintain their original positions with respect to each other.
Sorting an array with n elements using half divide steps, then the merge-sort algorithm is prociding 

If array has zero or one element, return array; it is already sorted. Otherwise array has at least two elements, divide array half and array1 and array2, each containing about half of the elements of array; that is, array1 contains the first [n/2] elements of array, and array2 contains the remaining [n/2] elements. Make this step until all arrays has only one element. Then recursively sort all arrays. Last step after sorting put back the all elements into array by merging the sorted.

## Big O 
* Time complexity Big O(nlogn)
* Space complexity Big O(n)

