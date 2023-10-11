# ------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------PROBLEM 2--------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------

# BIRTHDAY CAKE CANDLES
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    massimo = max(candles) # find the maximum height
    return len([candle for candle in candles if candle == massimo])# return the number of the candles with the max height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()


# NUMBER LINE JUMPS
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # some checks
    if x2 > x1 and v2 > v1: # if the second is ahead of the first and is faster, they can't reach the same spot at the same time
        return 'NO'
    elif x1 > x2 and v1 > v2: # if the first is ahead of the second and is faster, they can't reach the same spot at the same time
        return 'NO'
    elif x1 != x2 and v1 == v2: # if their starting position is different and they have different speed, they can't reach the same spot at the same time
        return 'NO'
    # this problem may be solved with the "Equation of Motion": x1 + t * v1 = x2 + t * v2
    t = (x2 - x1) / (v1 - v2) # if this division has an integer as result means that there is an instant where they reach the same spot
    if t.is_integer():
        return "YES"
    else:
        return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()


# RECURSIVE DIGIT SUM    
def superDigit(n, k):
    # Write your code here
    start = n * k # concatenate string 'n' per 'k' times
    sum_start = 0
    for num in start: # first iteration on the first concatenated number
        sum_start += int(num) # summation of all the number
    while sum_start >= 10: # while has at lest 2 digits
        aux = 0 # initialize auxiliar variable to zero
        for num in str(sum_start): # cast the number to string and iterate over the digits
            aux += int(num) # cast each digit to int and sum all of them
        sum_start = aux # update the variable
    return sum_start # at this point it'll be a single digit number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()


# VIRAL ADVERTISING
def viralAd_aux(n,d,like_lastday,cumulative): # auxiliar function to perform the recursion
    if d == n: # base case
        return cumulative
    like = math.floor((like_lastday * 3) / 2) # compute the number of likes of the day 'd', starting from the lst day's likes
    return viralAd_aux(n, d + 1, like, cumulative + like) # recursive call, updating the parameters 

def viralAdvertising(n):
    # Write your code here
    if n == 1: # base case, if is requested the first day, return the number
        return math.floor(5 / 2)
    else: #return the auxiliar function that has as parameter: n (requested day), d (current day), like_lastday (number of likes of the last day) and cumulative (total number of likes)
        return viralAd_aux(n, 1, math.floor(5 / 2), math.floor(5 / 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()



# INSERTION SORT #1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    last = arr[n - 1]
    arr[n - 1] = arr[n - 2] # first swap because the rightmost element isn't sorted
    i = n - 1 # iterate over the array right to left
    while i >= 0:
        if last < arr[i]: # check if the element to sort is loweer
            if i != 0: # if it's lower and we aren't scanning the position 0
                arr[i] = arr[i - 1] # swap the element
            else: # if i == 0
                arr[i] = last # the elem
                print(' '.join([str(c) for c in arr])) # print the list as string with .join() functione
                return
        if last > arr[i]: # if the element to sort is bigger than the oen we are analizing, we update the i-th element with last
            arr[i] = last
            print(' '.join([str(c) for c in arr])) # print the list as string with .join() functione
            return
        print(' '.join([str(c) for c in arr])) # print the list as string with .join() functione
        i -= 1 # decrement
    return
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)



# INSERTION SORT 2
def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n): # first for loop to iterate over 'arr', choose the element to analyze
        for j in range(i): # inside the first loop there is gonna be a loop from 0 to i, to iterate over the elements on the left of the one we are analyzing
            if arr[i] < arr[j]: # if the element we are analyzing is lower then the one we are comparing with
                aux = arr[i] # swap the element
                arr[i] = arr[j]
                arr[j] = aux
        print(' '.join([str(el) for el in arr])) # print the list as string with the .join() method

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////