# Problem 1

## Approach

I basically had to create the LRU Cache get and set operations as efficient as possible. The idea of creating a hash map was pretty straightforward, where I just created a Node with a `next_bucket` property to manage conflicts. Also, I created a simple hash function where, for integers, it is the number itself modulo the size of the LRU Cache. For strings, I used the first character only. The problems began when I had to manage the least recently used value. Should I create a counter, an array, another hashmap, or a pipe?

So, I came up with the idea of creating a pipe, which is a Double Stack, where both append and pop operations are *O(1)*, and accessing the head and tail are *O(1)* as well. It was easy to manage the least recently used case, where it simply changes the link of nodes, so the complexity is *O(1)* here as well.

## Time Complexity

- **set**: *O(1)* as the average case. *O(n)* is the worst case, same as the get reason.
- **get**: *O(1)* as the average case. *O(n)* in the worst case if all values are stored in one bucket. For example, if the size is 10 and we stored 10, 20, 30, ... 100 numbers, they all would be stored in the first bucket only.
- **Creating LRU Cache**: *O(n)* where n is the capacity.

## Space Complexity

*O(1)* for all operations except the LRU Cache itself. It would be *O(2n)* as the worst case, where n is the capacity, both for `self.sequence` and `self.arr`.
