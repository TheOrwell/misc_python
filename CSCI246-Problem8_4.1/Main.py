import random

numbers = list(range(10))


def cc_gen():
    array = []
    for i in range(1, 17):
        randNum = random.choice(numbers)
        array.append(randNum)
    print(array)
    return array


def cc_Check(checkNums):
    digitCount = 0
    index = 1  # tracking the index

    for num in checkNums:
        # This skips over the first 'None' element.
        if num is None:
            continue

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


def luhnDoubling(arrNums):
    # Double the value of every digit.
    for i in range(len(arrNums)):
        if arrNums[i] != '?':
            arrNums[i] *= 2

            # If the result of the doubling is greater than 9, subtract 9 from it
            if arrNums[i] >= 9:
                arrNums[i] -= 9


def cc_LuhnCheck(checkNums):

    # randomly replace one digit in the array.
    replaceIdx = random.randint(0, len(checkNums) - 1)
    checkNums[replaceIdx] = '?'

    luhnDoubling(checkNums)

    print(checkNums.copy())  # Debugging

    possible_int = 1
    for i in range(9):
        for j in range(len(checkNums)):
            if checkNums[j] == '?':
                checkNums[j] = possible_int * 2

                if checkNums[j] > 9:
                    checkNums[j] -= 9

        # Mod 10 check
        total_sum = 0
        for num in checkNums:
            total_sum += num

        if total_sum % 10 == 0:
            print("The missing number is: " + str(possible_int))
            break
        else:
            possible_int += 1
    print("\n the correct number was not found")


cc_nums = cc_gen()

cc_Check(cc_nums.copy())
print("\n")
cc_LuhnCheck(cc_nums.copy())
