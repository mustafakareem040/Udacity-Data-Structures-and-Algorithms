# Problem 3

## Encoding

For encoding, firstly I used a counter to calculate the frequency of each character. Next, I tried to use sorted instead of creating a minimum heap tree since I thought sorting would take *O(n log n)* and pushing all nodes to min-heap would also take *O(n log n)* until I realized I have to keep pushing new items. So I thought about binary search and inserting to the array, but the insertion would take *O(n)* in all cases. Therefore, I used the heapq library, which has heappush and heappop functions, both of which are *O(log n)*. When I finished the tree by continually removing two minimum items and pushing the sum, I traversed through all the tree using Depth First Search *Pre Order* to create the binary codes in a hashmap, for example, *{'B': '0', 'B': '11'}*. Finally, I looped through the input data, taking each letter and looking it up in the hashmap, then storing it in a string. Lastly, I returned both the encoded data and the tree.

### Time Complexity

1. For creating the counter, it is *O(N)*, where N is the size of the data.
2. For building the min-heap tree, it should take *O(k⋅log k)*, where K is the size of the counter or unique characters.
3. For creating the Huffman tree, it should take *O(k⋅log k)* for pushing and *O(k⋅log k)* for popping from the min-heap, resulting in an overall complexity of *O(2k⋅log k)*.
4. For Depth First Search, it should be *O(k)*.

**The overall time complexity of the encoding function should be *O(6N⋅log N)* in the worst case, assuming K = N, where there are no unique characters.**

### Space Complexity

1. For creating the counter, it should be O(K) since I'm cleaning the counter while pushing to the min tree, it should still be O(K).
2. Creating the Huffman tree should take O(2k) since we are adding the sum as well, but we are also cleaning the min tree.
3. The table has a complexity of O(k).
4. The encoded data has a complexity of O(n⋅m), where m is the average length of the code, and n is the size of the input.

**The overall space complexity should be O(k⋅n⋅m)**

## Decoding

The decoding process is simple: just loop through the bits and traverse through the tree *(0 is left, and 1 is right)* until we reach the leaf, and we put the character in our decoded string.

### Time Complexity
It should be *O(n⋅h)*, where n is the number of characters, and h is the height of the tree.

### Space Complexity
*O(n)*, the result of the encoded data.