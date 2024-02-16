import random


def rand_card_num():
    arr = []
    numbers = list(range(10))  # numbers 0-9
    for i in range(1, 17):
        randNum = random.choice(numbers)
        arr.append(randNum)

    # Insert '?' at a random index
    rand_index = random.randint(0, len(arr) - 1)
    arr[rand_index] = '?'

    return arr


def cc_check(array):
    index = 1   # a custom index to track whether the index of the array is even or odd.
    arr_sum = 0     # a variable to hold the sum of the array.
    possible_num = 0    # a variable to hold the possible number.
    index_of_guess = array.index('?')   # an index of the possible guess.

    # Update the array with the first possible number, which will always be 0.
    array[index_of_guess] = possible_num

    # perform the sum doubling on the array
    for i in range(len(array)):
        if index % 2 == 1:  # if the array index is odd
            double = array[i] * 2
            array[i] = double  # update the array location

            if double >= 10:
                double = double % 10 + double // 10
                array[i] = double  # update the array location
        index += 1

    # sum the resulting array
    for num in array:
        arr_sum += num

    # check to see if the sum of the array, mod 10 = 0; if it does not, begin a while loop where the possible number is
    # updated until one is found.
    if arr_sum % 10 != 0:
        array[index_of_guess] = possible_num

        while arr_sum % 10 != 0:
            arr_sum = 0     # update the sum
            possible_num += 1   # increment the sum
            array[index_of_guess] = possible_num

            # account for if the location we are updating until we get a match is even or odd.
            if index_of_guess % 2 == 1:
                double = array[index_of_guess] * 2
                array[index_of_guess] = double  # update the array location.

                if double >= 10:
                    double = double % 10 + double // 10
                    array[index_of_guess] = double  # update the array location.

            # add everything in the array up again, after this, the check in the while loop will perform the
            # next mod 10 check.
            for num in array:
                arr_sum += num
    print("The missing number is: " + str(possible_num))
    return arr_sum % 10 == 0


credit_card_num = rand_card_num()
print("The credit card number: \n" + str(credit_card_num))
cc_check(credit_card_num.copy())
