# Singly Linked List

Utulizing the single responsibility principle to a Linked List.

## Challenge
Challenge7
Functionality Instantiate an empty linked list
Functionality Insert into the linked list
The head property pinting to first node in the linked list
Insert multiple Nodes into linked list
Return True when finding an existing value within the linked list
Return False when a nonexisting value searched in the linked list
Return a collection of all values that exists in the linked list


## Approach & Efficiency

Insert, includes and to_string methods are used O(n) for big O time and big Ospace complexities.

## API

The linked list class has an attribute head, insert adds a node to in front of head attribute and makes it new head, includes search a node whether it is in linked list or not and to_string returns a string result.



## Solution
![picture](./assets/linked-list-2.jpg)

# Kth Value From the End
## Challenge
Create a method that takes in an index and returns the value of the node at that position. If the position is outside of the bounds of the list the function prints the exception,

## Approach & Efficiency
Function to get the kth node from the last of a linked list, then use a temporary variable, then use count module check if entered location greather than linked list if yes, it is an exception and if not , use for loop to get the node value. 
#### kth_from_end:
O(n) for big O time and big Ospace complexities.

## APIs
kth_from_end: 
k <= len(ll) output: `node value' 
k > len(ll) output : 'Expection'


## Solution
![picture](./assets/ll-kth-from-end.jpg)

