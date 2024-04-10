# Problem 4

## Approach

For this problem, I changed `self.users` from a list to a set since each user is unique. Sets would be much better in this case because of the O(1) search.

The function checks whether the user is in the group. If so, it will return True; otherwise, it will traverse its groups.

## Time Complexity
Should be O(M) in the worst case, where M is the total of all groups and subgroups.

## Space Complexity
Recursion takes *O(D)*, where D is the deepest subgroup, because it creates a stack. Otherwise, it is O(1).