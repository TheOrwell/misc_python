import random

"""
This method generates a random number, and then doubles the odd indexes,
"""
def cc_gen():
    numbers = list(range(10))
    isValid = False

    while not isValid:
        array = []
        arr_sum = 0

        for i in range(1, 17):
            randNum = random.choice(numbers)
            array.append(randNum)

        #print(array)

        digitCount = 0
        index = 1  # tracking the index

        for i in range(len(array)):
            if index % 2 == 1:
                array[i] = array[i] * 2
                if array[i] >= 10:
                    doubleStr = str(array[i])
                    array[i] = int(doubleStr[0]) + int(doubleStr[1])
                else:
                    pass # number is not equal to or greater than 10, and does not need to be summed
            else:
                pass

            index += 1

        for num in array:
            arr_sum += num

        if arr_sum % 10 == 0:
            print(arr_sum)
            print(array)
            return array


def randReplace(arr):
    index_to_replace = random.randint(0, len(arr) - 1)
    arr[index_to_replace] = '?'
    return arr


def cc_Check(checkNums):
    digitCount = 0
    index = 1  # tracking the index

    for num in checkNums:
        # Checks to see if the number is odd.
        if index % 2 == 1:
            # print(str(num), end="")
            double = num * 2

            # If the result of double is equal to or exceeds 10, add the tens and the ones digit together.
            if double >= 10:
                doubleStr = str(double)  # convert the result of double into a string
                splitSum = int(doubleStr[0]) + int(doubleStr[1])  # cast each index of that string to an integer and add them
                print(splitSum, end="")
                digitCount += 1
                if digitCount % 4 == 0:
                    print(" ", end="")

            else:
                print(double, end="")
                digitCount += 1
                if digitCount % 4 == 0:
                    print(" ", end="")

        # All other checks failed. The number is even.
        else:
            print(str(num), end="")
            digitCount += 1
            if digitCount % 4 == 0:
                print(" ", end="")

        index += 1


def cc_LuhnCheck(checkNums):
    possible_num = 0
    arr_sum = 0

    index_ques = checkNums.index('?') + 1  # +1 is here so that every other indices from 0 will be treated as odd.

    checkNums[index_ques - 1] = possible_num  # assign a possible number to the unknown index. -1 here to adjust above indexing.

    # determine if the array index of ? is odd or even
    if index_ques % 2 == 1:
        checkNums[index_ques-1] *= 2

        # If it is, double it. If the result is greater than 10, subtract 9 from it, per Luhn's algorithm.
        if checkNums[index_ques-1] >= 10:
            checkNums[index_ques-1] -= 9

    # Add up the array
    for idx in checkNums:
        arr_sum += idx

    if arr_sum % 10 == 0:
        print("The missing number is: " + str(checkNums[index_ques]))
    else:
        while possible_num != 9:
            # update index and re-perform the calculations
            possible_num += 1
            arr_sum = 0

            checkNums[index_ques-1] = possible_num

            # determine if the array is odd or even
            if index_ques % 2 == 1:
                checkNums[index_ques-1] *= 2
                if checkNums[index_ques-1] >= 10:
                    checkNums[index_ques-1] -= 9

            # Add up the array again
            for idx in checkNums:
                arr_sum += idx

            if arr_sum % 10 == 0:
                print("The missing number is: " + str(checkNums[index_ques-1]))


cc_nums = cc_gen()

# print("Original Array: \n" + str(cc_nums))
# print("\nChecked number: ")
# cc_Check(cc_nums.copy())
print("\n\nRandomly Replaced index: ")
print(randReplace(cc_nums.copy()))
print(cc_LuhnCheck(randReplace(cc_nums.copy())))