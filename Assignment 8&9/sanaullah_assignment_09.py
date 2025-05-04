def climb_stairs(n):
    """
    Calculates the number of distinct ways to climb to the top of a staircase.

    Args:
        n: The number of steps in the staircase.

    Returns:
        The number of distinct ways to climb to the top.
    """
    #-1 if n is 1 or 2 return n directly
    if n<=2:
        return n
    #-2 Initilize base cases for fibonacci like approach
    first = 1  # f(1)
    second = 2 # f(2)

    #-3 Start calculating from 3 to step n
    for i in range(3,n+1):
        third = first + second  # f(n) = f(n-1) + f(n-2) #-first and second represent previous two Fibonacci values.
        first = second         # update f(n-2) to previous f(n-1)
        second = third         # update f(n-1) to new f(n)  #-In each iteration, we update them step-by-step so that second always holds the latest result.
    #-4 Return the total number of distinct ways
    return second   #-At the end, second holds f(n), which is our final answer — that’s why we return it."


# Example Usage
n1 = 2
n2 = 3
n3 = 5
n4 = 10

#-4 calling a function and print result
print(f"Number of ways to climb {n1} stairs:{climb_stairs(n1)}")
print(f"Number of ways to climb {n2} stairs:{climb_stairs(n2)}")
print(f"Number of ways to climb {n3} stairs:{climb_stairs(n3)}")
print(f"Number of ways to climb {n4} stairs:{climb_stairs(n4)}")
        
    
    