def staircase(n):
    # Base Case - What holds true for minimum steps possible i.e., n == 1? Return the number of ways the child can climb one step.

    # Inductive Hypothesis - What holds true for n == 2 or n == 3? Return the number of ways to climb them.
    
    # Inductive Step (n > 3) - use Inductive Hypothesis to formulate a solution
    
    if n <= 2:
        return n
    if n == 3:
        return 4
    return staircase(n-3) + staircase(n-2) + staircase(n-1)

print(staircase(20))