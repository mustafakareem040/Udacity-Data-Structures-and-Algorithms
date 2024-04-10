# Problem 5

## Approach
For this problem, I added a `next` attribute to the link for the **previous** block. Since it is a synchronous program, I created the hash based on the timestamp.
For the LinkedList, the head value starts with 0 (which can be considered as null). For the `append` method, I replaced `self.head` with a new Block. For the previous hash, I added `self.head` and `self.head.hash` as arguments, which means if `self.head` is 0, then the previous hash is 0; otherwise, it is the current block hash.

## Time Complexity
The `append` method should take *O(1)*.

## Space Complexity
The `append` method should take *O(1)*, and the LinkedList *O(n)*.