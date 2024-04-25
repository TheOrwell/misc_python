"""
CITATION: Consulted Claude from Anthropic to ensure that we were approaching the solving of this right.
"""
import random


def randSelect(arr, i):
    n = len(arr)    # Get the length of the array
    if n == 1:
        return arr[0]

    # Choose x ∈ {1, ..., n} randomly
    x = random.randint(0, n - 1)

    """
    Creates a new array called y by iterating over the original array, by 
    checking if the current element is less than the element randomly at the xth index.
    """
    losers = [y for y in arr if y < arr[x]]

    """
    Similar to the logic above, but in this case saves all the elements that are greater than the element at 
    the randomly selected xth index. This effectively breaks one array down into two smaller ones, until
    the desired value is found.
    """
    winners = [y for y in arr if y > arr[x]]

    if i < len(losers) + 1:     # The desired element's index is less than or equal to the length of the losers array
        return randSelect(losers, i)    # recursive call to keep looking
    elif i == len(losers) + 1:  # The desired element is found.
        return arr[x]
    else:
        return randSelect(winners, i - len(losers) - 1)     # not found. Keep recursing until element is found.


# Generating a large array of random ints
large_array = [random.randint(1, 1000000) for _ in range(1000000)]

# Save data points to values and insert into main method
n = len(large_array)
median_index = n // 2 + 1   # Index for median
median = randSelect(large_array, median_index)


print(f"The median value of an array of the large array is: {median}")

