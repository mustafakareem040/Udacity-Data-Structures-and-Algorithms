# Approach

In set theory the union takes all the values of **A** and **B** and put them into new set without any duplications while intersection takes the values that exist both in **A** and **B**and put them into new set also without any duplications. The interesting thing is this is a linked list not a set so I had to figure out a way to deal with duplications I came with the following ideas.

# Union

Takes all the values *including duplications* that exist in **A** or **B**
I did some optimizations. instead of calling the append method each time would take *O^2* I accessed the head attribute in the new empty linked list and each time it adds a value it moves to the next node and that would make *O(1)* append.

# Intersection

Duplications are also allowed in intersection but for the minimum count in **A** or **B** for example [1, 3, 3, 5], [2, 3, 3, 3, 6] will create a list of [3, 3] two 3s not three.
The approach is as the following:
1. Creating a counter dictionary for the first list.
2. Iterating through the second list.
3. If the value exist in the dictionary and has item > 0 go to step 4 otherwise step 2.
4. substract counter[value] by 1.
5. Add the value to the linked list.

# Time Complexity
**Union**: O(n⋅m).
**Intersection**: O(n⋅m).
*where n is the size of first list and m of the second list.*

# Space Complexity
**Union**: O(n⋅m).
**Intersection**: O(2n) in worst case if list1 == list2.
