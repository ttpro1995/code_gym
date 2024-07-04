"""

Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array

  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

"""


def kadane(arr):
    max_so_far = -999999
    max_ending_here = 0
    for e in arr:
        max_ending_here = max_ending_here + e
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

if __name__ == "__main__":
    x1 = [-2,-3,4,-1,-2,1,5,-3]
    x2 = [5,4,1,7,8]

    print(kadane(x1))
    print(kadane(x2))