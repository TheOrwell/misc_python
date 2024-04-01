# CITATION: Claude from Anthropic was consulted during the solving of this problem
# Using time module per Dr. Mumey's suggested strategy: Compare the functions performance @ runtime. (no paper required)
import time


# A function that loops for the specified amount of times and computes/counts the fibonacci numbers that many times.
# Runtime is of this method is calculated within this method.
def fib_loop(times):
    start_time = time.perf_counter()    # Save start time for method comparison.

    # Initialize variables and print initial values. (These are taken to be 0 and 1)
    i = 0
    num1 = 0
    num2 = 1
    print(num1, end=', ')
    print(num2, end=', ')

    # Main loop; iteratively adds the previous two numbers and prints the number in the sequence.
    while i < times:
        cur = num1 + num2
        print(cur, end=', ')
        num1 = num2
        num2 = cur
        i += 1
    print(" ... ∞")     # some dots and ALT + 236 for a lil razzle-dazzle.

    # Use start and end time to find the elapsed time; print results.
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # Converting to milliseconds
    print(f"Runtime with ({times}) input elements: {elapsed_time:5f} ms.\n")


# A recursive method that takes in 2 initial numbers (these should be 0 and 1) and the amount of times to compute/count
# the fibonacci sequence of numbers.
def fib_recursion(num1, num2, times):
    # Base case
    if times > 0:

        cur = num1 + num2
        print(cur, end=', ')    # Print the current Fibonacci number.

        # Recursive case
        fib_recursion(num2, cur, times - 1)
    else:
        return


# Testing functions with large numbers:

# --------------------- TEST 100 ELEMENTS ---------------------
print("\t\t---------------------")
print("First 100 fibonacci numbers using a loop:")
fib_loop(100)
print("First 100 fibonacci numbers using recursion:")

# Due to the nature of recursion, the time computations had to go on the outside of the method, unlike for the loop
recurs_times = 100
recurs_strt_time = time.perf_counter()
fib_recursion(0, 1, recurs_times)
print(" ... ∞") # some dots and ALT + 236 for a lil razzle-dazzle.
recurs_end_time = time.perf_counter()
elapsed_recurs_time = (recurs_end_time - recurs_strt_time) * 1000   # Converting to milliseconds
print(f"Runtime with ({recurs_times}) input elements: {elapsed_recurs_time:5f} ms.")


# --------------------- TEST 450 ELEMENTS ---------------------
print("\t\t---------------------")
print("First 450 fibonacci numbers using a loop:")
fib_loop(450)
print("First 450 fibonacci numbers using recursion:")

recurs_times = 450
recurs_strt_time = time.perf_counter()
fib_recursion(0, 1, recurs_times)
print(" ... ∞")
recurs_end_time = time.perf_counter()
elapsed_recurs_time = (recurs_end_time - recurs_strt_time) * 1000
print(f"Runtime with ({recurs_times}) input elements: {elapsed_recurs_time:5f} ms.")

# --------------------- TEST 950 ELEMENTS ---------------------
print("\t\t---------------------")
print("First 950 fibonacci numbers using a loop:")
fib_loop(950)
print("First 950 fibonacci numbers using recursion:")

recurs_times = 950
recurs_strt_time = time.perf_counter()
fib_recursion(0, 1, recurs_times)
print(" ... ∞")
recurs_end_time = time.perf_counter()
elapsed_recurs_time = (recurs_end_time - recurs_strt_time) * 1000
print(f"Runtime with ({recurs_times}) input elements: {elapsed_recurs_time:5f} ms.")
print("\t\t---------------------")
