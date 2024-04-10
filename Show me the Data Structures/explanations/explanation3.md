# Encoding

For encoding firstly I used counter to calculate the frequency of each character. Next I tried to use sorted instead of creating minimum heap tree since I thought sorting will take *O(n log n)* and pushing all nodes to min-heap will also take *O(n log n)* until I realized I have to keep pushing new items so I thought about binary search and inserting to the array but the inseration will take *O(n)* in all cases. So I used heapq library which have a heappush and heappop functions both are *O(log n)*. When I finished the tree by keeping removing two minimum items and pushing the sum I traverse through all the tree using Depth First Search *Pre Order* to create the binary codes in hashmap for example *{'B': '0', 'B': '11'}* and finally looping through the input data taking each letter and look up in the hashmap and then store it in the string, finally I return both encoded data and the tree.

**Time Complexity**

1. For creating the counter it is *O(N)* where N is the size of data.
2. For building the min-heap tree it should take *O(k⋅log k)* where where K is the size of counter or unique characters.
3. For creating the huffman tree it should take *O(k⋅log k)* of pushing and *O(k⋅log k)* of popping from min-heap the overall is *O(2k⋅log k)*.
4. For Deapth First Search it should be *O(k)*.
**The overall time complexity of encoding function should be *O(6N⋅log N)* in worst case assuming K = N where there is no unique characters.**

**Space Complexity**
1. For creating the counter it should be O(K) since I'm cleaning the counter while pushing to the min tree it should still O(K).
2. Creating the Huffman tree should take O(2k) since we are adding the sum as well but we are also cleaning the min tree.
3. The table has complexity of O(k).
4. The encoded data has complexity of O(n⋅m) where m is the average length of code and n is the size of input.
**The overall space complexity should be O(knm)**

# Decoding

The decoding process is simple just looping through bits and traversing through the tree *(0 is left and 1 is right)* until we reach the leaf and we put the character in our decoded string.
**Time Complexity**
It should be *O(n⋅h)* where n is the number of characters  and h is the height of the tree.

**Space Complexity**
*O(n)* the result of encoded data.