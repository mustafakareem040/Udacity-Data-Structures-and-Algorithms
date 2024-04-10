# Problem 2

## Approach

I used os module to list directories and simplify stuff. I also used recursion instead of nested loop because the code would be more readable and because the problem is called "File Recursion".

## Time Complexity

O(n+m) where n is the number of all files and m is for directories where they exist in the directory and subfolders.

## Space Complexity

O(n) for the saving results paths. (n for all files at the worst case since the approach should never get directory in the result)
