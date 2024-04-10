# Approach

For this problem  I changed self.users from list to set since each user is unique sets would be much better in this case because of the O(1) search

The function checks whetever the user is in the group if so it will return True otherwise it will traverse in its groups.

**Time complexity**
Should be O(M) in worst case where M is the total of all groups and subgroups.

**Space Complexity**
Recursion takes *O(D)* because it creates a stack where D is the deepest subgroup otherwise it is O(1).