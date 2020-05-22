#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime would be O(n^c) due to the multiplication of n in the conditions of the while loop (n^3). The nultiplication of n^2 inside the while loop would help negate some of the exoponential increase in runtime complexity, but not all of it.


b) The runtime would be O(n log n). It linearly loops through the range of n but then has a while loop inside the for loop where the conditional value doubles it self until it's value equals or surpases the input n.


c) The runtime for this would be O(n). It scales linearly with the input value of 'bunnies'. For each added 'bunny' the recursive function would be called one more time.

## Exercise II

    My proposed algorithm would be based on a binary search. I would create a list of floors based off of the n stories which would be sorted.

    # possible_f = [i+1 for i in range(n)]

    From there I would implement a binary search, starting at the mid point

    # mid point = len(possible_f) // 2

    I would then check if the mid point breaks the egg, if it does I would discard the right side of the list and focus left. making the start_point = 0 and the end point = mid_point. else I would move right in the list.
    
    From there I would repeat this process until the start point does not break the egg and the endpoint does break the egg. At that point we know that f = end_point.

    This would have O(log n) runtime due to the constant halving of the stories and would be the most efficient way to find breakpoint floor.




