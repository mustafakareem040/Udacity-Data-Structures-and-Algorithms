# Problem 1

# Approach

I basically had to create the LRU Cache get and set operations as efficent as possible the idea of creating hash map was pretty straightforward where I just created a Node with next_bucket property to manage conflictions. Also I created a simple hash function where for integers it is the number itself modular size of LRU Cache, for strings I used first character only. The problems began when I had to manage the least recently used value, should I create a counter, an array, another hashmap or pipe?
So I came with the idea of creating pipe which is Double Stack where both append and pop are *O(1)* and access the head and tail are *O(1)* as well. It was easy to manage the least recently used case where it simply changes the link of nodes so the compleixty is *O(1)* here as well.

# Time Complexity

**set**: *O(1)* as average case *O(n)* is worst case same as get reason.
**get**: *O(1)* as average case *O(n)* in worst case if all values are stored in one bucket for example if the size is 10, and we stored 10, 20, 30, ... 100 numbers the all would be stored in first bucket only.
**Creating LRU Cache**: *O(n)* where n is the capacity.

# Space Complexity

*O(1)* for all operations except the LRU_Cache it self it would be O(2n) as worst case where n is the capacity both for self.sequence and self.arr.