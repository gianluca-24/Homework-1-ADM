# ------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------PROBLEM 1--------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------
import math
import os
import random
import re
import sys
import numpy

# --------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------INTRODUCTION----------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

#PYTHON IF ELSE
if __name__ == '__main__':
    n = int(input().strip())
    if n >= 1 and n <= 100: # if n is odd, print Weird
        if n % 2 != 0:
            print('Weird')
        elif n % 2 == 0: # if n is even
            
            if n >= 2 and n <= 5 or n > 20: # in the inclusive range of 2 to 20 or greater then 20, print Not Weird
                print('Not Weird')
            else: # If  is even and in the inclusive range of 6 to 20, print Weird
                print('Weird')

# ARITHMETIC OPERATORS
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a >= 1 and b >= 1 and a <= 10 ** 10 and b <= 10 ** 10:
        print(a + b) #sum  
        print(a - b) #difference
        print(a * b) #product

#PYTHON: DIVISION
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b) # integer division
    print(a / b) #float division

#LOOPS
if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <= 20: # constraints
        i = 0
        while i < n: # for each i print the square of i 
            print(i ** 2)
            i += 1

#WRITE A FUNCTION
def is_leap(year):
    leap = False # initialize a boolean to return
    # Write your logic here
    if year % 4 == 0 and year >= 1900 and year <= 10 ** 5: # check if the year can be evenly divided by 4, is a leap year, unless
        leap = True
        if year % 100 == 0: # the year can be evenly divided by 100, it is NOT a leap year, unles
            leap = False
            if year % 400 == 0: # The year is also evenly divisible by 400
                leap = True # so it is leap
    return leap

#PRINT FUNCTION
if __name__ == '__main__':
    n = int(input())
    
    if n >= 1 and n <= 150: # constraints
        
        string = '' # initialize empty string
        for i in range(n):
            #Print the list of integers from 1 through n as a string, without spaces
            string += str(i + 1)
    print(string)


# ------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------DATA TYPES----------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# LIST COMPREHENSIONS
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # create a list of lists iterating through the three ranges (x + 1, y + 1, z + 1)
    # and select only the list which sum isn't n
    output = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
    print(output)

# NESTED LIST
if __name__ == '__main__':
    list = [] # initialize empty list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append((name,score))# insert into the liste the touples (name,score)
    if len(list) >= 2 and len(list) <= 5:
        minimo = min([y[1] for y in list]) # find the minimum value y[1] (minimum score)
        list_scores = [x[1] for x in list if x[1] != minimo] # create through a comprehensiona new list of values without the minimum
        names = [x[0] for x in list if x[1] == min(list_scores)] #create a list with the names of the students having the second lowest grade
        names.sort()  # sort in alphabetical order
        for i in names:
            print(i)

# FIND THE RUNNER-UP SCORE
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) #initialize an array of int from a list given in input
    if n >= 2 and n <= 10:
        arr = list(arr) # cast needed because otherwise i couldn't perform the next line
        runner = max([x for x in arr if x != max(arr)]) # Through a list comprehension i created a list of element without the maximum, and then from this one I took and returned the max
        print(runner)

# FINDING THE PERCENTAGE
if __name__ == '__main__':
    n = int(input())
    # given code
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if n >= 2 and n <= 10: # check constraints
        mean = sum([x for x in student_marks[query_name]]) / 3 # compute the mean dividing the sum of the elements of a list created through a comprehension for 3
        decimal_mean = f"{mean:.2f}" # right format for returning, 2 decimals
        print(decimal_mean)
         

# LISTS
if __name__ == '__main__':
    N = int(input())
    i = 0
    lista = [] # I'm gonna operate on this list
    while i < N:
        command = str(input()) # read the command
        cmd_list = command.split()
        # with this sequence of if-else we check which command has been given in input and it'll be performed on lista
        if cmd_list[0] == 'insert':
            lista.insert(int(cmd_list[1]), int(cmd_list[2]))
        elif cmd_list[0] == 'print':
            print(lista)
        elif cmd_list[0] == 'remove':
            lista.remove(int(cmd_list[1]))
        elif cmd_list[0] == 'append':
            lista.append(int(cmd_list[1]))
        elif cmd_list[0] == 'sort':
            lista.sort()
        elif cmd_list[0] == 'pop':
            lista.pop()
        elif cmd_list[0] == 'reverse':
            lista.reverse()
        i += 1

# TUPLES
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla = () # initialize a tuple
    for i in integer_list:
        tupla += (i, )
    print(hash(tupla)) # perform hashing on the tuple


# ---------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------STRINGS----------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------
# SWAP CASE
def swap_case(s):
    swap = '' # auxiliar string initialized to the empty string ''
    for c in s: # iterate over the string 's'
        if c.isupper(): # if the char is upper, add the same char but lowercase
            swap += c.lower()
        else: # otherwise, if the char is lower, add that char but uppercase
            swap += c.upper()
    return swap # return the swapped string

# STRING SPLIT AND JOIN
def split_and_join(line):
    # write your code here
    line = line.split() # split on the ' ' char
    line = '-'.join(line) # create a string from the list obtained from .split()
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# WHAT'S YOUR NAME
def print_full_name(first, last):
    # Write your code here
    print('Hello '+ first + ' ' + last +'! You just delved into python.')

# MUTATIONS
def mutate_string(string, position, character):
    list_str = list(string) #create a list from the given string
    list_str[position] = character # put 'character' in the given 'position'
    return ''.join(list_str) # return a string obtained through the .join(..) method

# FIND A STRING
def count_substring(string, sub_string):
    length = len(string)
    if length < 1 or length >200: # check constraints
        return
    sub_length = len(sub_string)
    count = 0 # initialize count, will be returned at the end 
    for i in range(length - sub_length + 1):
        if sub_string == string[i : i + sub_length]: # check if 'sub_string' is equals to a slice 'string' of the same length as 'sub_string'
            count += 1  # count the substring found
    return count

# STRING VALIDATORS
if __name__ == '__main__':
    s = input()
    length = len(s)
    if length > 0 and length < 1000: # check constraints
        is_alnum = False # initialize boolean value that will be printed
        is_alpha = False
        is_digit = False
        is_lower = False
        is_upper = False
        for x in s: # iterate over the string 's' and check each case: .isalnum(), .isalpha(), .isdigit(), .islower() and .isupper()
            if x.isalnum() == True:
                is_alnum = True
            if x.isalpha() == True:
                is_alpha = True
            if x.isdigit() == True:
                is_digit = True
            if x.islower() == True:
                is_lower = True
            if x.isupper() == True:
                is_upper = True
        print(is_alnum) # print all the results
        print(is_alpha)
        print(is_digit)
        print(is_lower)
        print(is_upper)

# TEXT ALIGNEMENT
thickness = int(input()) #This must be an odd number
c = 'H' 
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# TEXT WRAP
def wrap(string, max_width):
    length = len(string) 
    if length < 0 or length >= 1000 or max_width < 0 or max_width > length: # check constraints
        return
    # initialize auxiliar variables
    i = 0
    lista = []
    while i < length: # while 'i' is lower than the length of the string
        if i + max_width <= length: # if the sum of 'i' and the given width 'max_width' is lower or equal than the 'string' length it appends to 'lista' a slice of string of length 'max_width'
            lista.append(string[i:i + max_width])
        else: # else append the remained part of the string
            lista.append(string[i:])
       
        i += max_width # each loop I increment 'i' of 'max_width'
    return '\n'.join(lista) # return a string from the previous list

# DESIGNER DOOR MAT
nm = input().strip().split()
n = int(nm[0])
m = int(nm[1])
# print the first half of the mat
for i in range(math.floor(n / 2)): # loop from 0 to n/2
    dash = '-' * math.floor((m - (3 + 6 * i)) / 2) # I found the pattern to count how many '-' per line
    dot_line = '.|.' * i # I found the pattern to count how many '.|.' per line
    print(dash + dot_line + '.|.' + dot_line + dash)
# print the middle line with the 'welcome' word
print('-' * math.floor((m - 6) / 2) + 'WELCOME' + '-' * math.floor((m - 6) / 2))
# print the second half of the mat
for i in range(math.floor(n / 2) - 1, -1, -1): # inverse loop
    dash = '-' * math.floor((m - (3 + 6 * i)) / 2) # same as the previous loop
    dot_line = '.|.' * i # same as the previous loop
    print(dash + dot_line + '.|.' + dot_line + dash)


# STRING FORMATTING
def print_formatted(number):
    # your code goes here
    num_spaces = len(str(bin(number))[2:]) # Consider the number from the position 2 to get the effective number, removing the '0x'
    i = 1 # loop will start from 1 because is requested from the input
    while i <= number:
        print(f'{i:>{num_spaces}} {oct(i)[2:]:>{num_spaces}} {hex(i)[2:].upper():>{num_spaces}} {bin(i)[2:]:>{num_spaces}}') # use this particular format to get the expected output well formatted
        i += 1

# ALPHABET RANGOLI
def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha = alphabet[:size] # cut the alphabet to the given size
    length = len(alpha)
    for i in range(size):
        first_alpha = '' # these two strings are used to draw each line
        second_alpha = ''
        dash = '-' * math.floor((4 * size - 4)/2 - 2 * i) # function that defines how many dash in line 'i'
        if i > 0:
            for j in range(i): #loop to print the right char in alphabetical order (will be printed only the chars from 0 to i)
                first_alpha += alpha[length - 1 - j] + '-' # print the characters in the first alpha
                second_alpha = '-' + alpha[length - 1 - j] + second_alpha # print the characters in the second half
        print(dash + first_alpha + alpha[length - 1 - i] + second_alpha + dash) # print the line combining the parts
    # the second loop is the same as the previous one but it's inverse
    for i in range(size - 2, -1, -1):
        first_alpha = ''
        second_alpha = ''
        dash = '-' * math.floor((4 * size - 4)/2 - 2 * i) # dashes per line
        if i > 0:
            for j in range(i): #loop for printing chars in alphabet order but divided by dashes
                first_alpha += alpha[length - 1 - j] + '-'
                second_alpha = '-' + alpha[length - 1 - j] + second_alpha
        print(dash + first_alpha + alpha[length - 1 - i] + second_alpha + dash) # final line
    

# CAPITALIZE
def solve(s):
    # split the function using a pattern
    string = re.split(r'(\s+)',s)
    return ''.join([w.capitalize() if w.strip() else w for w in string]) # return the string using .join() and passing as parameter a list obtained from a list comprehension that applies capitalize() method to each word of string

# MERGE THE TOOLS TODO
# THE MINION GAME TODO

# ------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------SETS----------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# INTRODUCTION TO SETS
def average(array):
    # your code goes here
    # create the new set
    ins = set(array)
    #print the average
    return sum(ins) / len(ins)

# NO IDEA!
happiness = 0
numbers = input().strip().split() # intialize n and m
n = int(numbers[0])
m = int(numbers[1])
lista = list(map(int,input().strip().split())) # first list, casted to int eith map
set_a = set(map(int,input().strip().split())) # set a of int given as input
set_b = set(map(int,input().strip().split())) # set b of int given as input
for i in range(n):
    if lista[i] in set_a:
        happiness += 1 # increase happiness if the element lista[i] is in set_a
    if lista[i] in set_b:
        happiness -= 1 # reduce happiness if the element lista[i] is in set_b
print(happiness) # print the happiness


# SYMMETRIC DIFFERENCE
#set_a
size_a = int(input())
set_a = set(map(int, input().strip().split())) # initialize set_a casting (with the map() function) to int the element of the input
#set_b
size_b = int(input())
set_b = set(map(int, input().strip().split()))# initialize set_b casting (with the map() function) to int the element of the input
sym = set(sorted(set_a.symmetric_difference(set_b)))# create a new set sorting the symmetric_differnce between set_a and set_b
for el in sym: # print the set
    print(el)


# SET .add()
n = int(input())

if n > 0 and n < 1000:# check constraints
    i = 0
    set_country = set() # initalize set
    while i < n:
        string = str(input())
        set_country.add(string) # add the input string to the set
        i+=1# increment 'i'
    print(len(set_country)) # return the length of the set


# SET .discard(), .remove(), AND .pop()
n = int(input())# number of elements in the set 
s = set(map(int, input().split()))# create new set from the input
N = int(input())# number of commands
for _ in range(N):
    cmd = input().strip().split()
    # this sequence of if-else check which kind of command has been given from input.
    # After a command is recognised, apply the relative method to the set    
    if cmd[0] == 'pop':
        if len(s) > 0:
            s.pop()
    elif cmd[0] == 'discard':
        if len(s) > 0:
            s.discard(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
print(sum(s))

        
# SET .union() OPERATION
en = int(input()) # number of students subscribed to engilsh newspaper
set_en = set(input().strip().split())# are given 'en' roll of students to initialize the set
fr = int(input())# number of students subscribed to french newspaper
set_fr = set(input().strip().split())# are given 'fr' roll of students to initialize the set
# use the union function to perform the union between the students who have subscribed to the french newspaper and the students who have subscribed to the english one
print(len(set_en.union(set_fr)))

# SET .intersection() OPERATION
en = int(input()) # number of students subscribed to engilsh newspaper
set_en = set(input().strip().split())# are given 'en' roll of students to initialize the set
fr = int(input())# number of students subscribed to french newspaper
set_fr = set(input().strip().split())# are given 'fr' roll of students to initialize the set
# use the function intersection to perform the intersection between the students who have subscribed to the french newspaper and the students who have subscribed to the english one
print(len(set_en.intersection(set_fr)))

# SET .difference() OPERATION
en = int(input()) # number of students subscribed to engilsh newspaper
set_en = set(input().strip().split())# are given 'en' roll of students to initialize the set
fr = int(input())# number of students subscribed to french newspaper
set_fr = set(input().strip().split())# are given 'fr' roll of students to initialize the set
# use the function difference to perform the difference between the students who have subscribed to the french newspaper and the students who have subscribed to the english one
print(len(set_en.difference(set_fr)))


# SET .symmetric_difference() OPERATION
en = int(input()) # number of students subscribed to engilsh newspaper
set_en = set(input().strip().split())# are given 'en' roll of students to initialize the set
fr = int(input())# number of students subscribed to french newspaper
set_fr = set(input().strip().split())# are given 'fr' roll of students to initialize the set
# use the function difference to perform the difference between the students who have subscribed to the french newspaper and the students who have subscribed to the english one
print(len(set_en.symmetric_difference(set_fr)))


# SET MUTATIONS
size_a = int(input())# size of set a
insieme_a = set(map(int, input().strip().split()))# initialize set a
n = int(input())
# will receive from input 2*n lines divided into n parts. For each part:
# - The first line of each part contains the space separated entries of the operation name and the length of the other set.
# - The second line of each part contains space separated list of elements in the other set.
for _ in range(n):
    cmd = input().strip().split()
    # First check which command is given from input, then operate the command using the methods .intersetion_update(), .update(),
    # .symmetric_difference_update() or _difference update() between 'insieme_a' and the set given from input
    if cmd[0] == 'intersection_update':
        insieme_a.intersection_update(set(map(int, input().strip().split())))
    elif cmd[0] == 'update':
        insieme_a.update(set(map(int, input().strip().split())))
    elif cmd[0] == 'symmetric_difference_update':
        insieme_a.symmetric_difference_update(set(map(int, input().strip().split())))
    elif cmd[0] == 'difference_update':
        insieme_a.difference_update(set(map(int, input().strip().split())))
print(sum(insieme_a))# then, print the sum of the element left in 'insieme_a'

# THE CAPTAIN'S ROOM
k = int(input()) # size of each group
lis_a = list(map(int, input().strip().split()))
diz = {}# initialize dict, keys will be the rooms number, values will be the number of times that the room occurs in the list
for el in lis_a:
    if el not in diz.keys(): # check if the element is in the dict and update the value
        diz[el] = 1
    else:
        diz[el] += 1
for key, value in diz.items():# look for the key with value 1 (will be the return value)
    if value == 1:
       
        print(key) # print the right room number
        break # break the loop when found

# CHECK SUBSET
t = int(input()) # number of tests
for _ in range(t):
    size_1 = int(input())
    set_1 = set(map(int, input().strip().split())) # creation of the first set from the given input
    size_2 = int(input())
    set_2 = set(map(int, input().strip().split())) # creation of the second set from the given input
    if set_1.issubset(set_2): # checking if it's a subset with the .issubset() method
        print(True)
    else:
        print(False)

# CHECK STRICT SUBSET
set_a = set(map(int, input().strip().split()))# creating the first set from the given input
n = int(input())# number of other sets
is_super = True # initialize of auxiliar variable to true, will be used as return value
for _ in range(n):
    set_aux = set(map(int, input().strip().split())) # initialize the given set
    if not set_a.issuperset(set_aux):
        # this parts define that if set_as isn't subset of at least
        # one other set, it isn't a strict superset. So 'is_super'
        # will be set to False
        is_super = False
        break 
print(is_super)


# -------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------COLLECTIONS----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# COLLECTIONS .counter()
from collections import Counter

shoes = int(input())
counter = Counter(input().split())
customers = int(input()) # number of customers
earn = 0 # intialize the variable that counts the earnign
for _ in range(customers):
    shop = input().split() # each line contains a purchase of a customer
    if shop[0] in counter.keys():
        if counter[shop[0]] > 0: # if there is at least one element of that product
            counter[shop[0]] -= 1 # decrease the number of element (product sold)
            earn += int(shop[1]) # update the earning, shop[1] contains the price
    elif shop[0] not in counter.keys(): # if shop[0] is not between the keys (the product isn't in the shop)
        continue
print(earn)


# DEFAULTDICT TUTORIAL
from collections import defaultdict

num = input().split()
n = int(num[0])
m = int(num[1])
d = defaultdict(list) # initialize defaultdict
i = 1
while i <= n:
    key = input() # the first n input are for the group A
    d[key].append(i) # create the new keys and append 'i' to each ('i' means the index of the element)
    i += 1
# initialize auxiliar variables
j = 0
list_b = []
while j < m:
    key = input() # the next m inputs are for the group B
    if key in d.keys(): # if the element is also in the group A
        aux = d[key]
        res = ' '.join(map(str,aux)) # format the output with the .join() method
        print(res)
    else: # if it isn't in the group A
        print(-1)
    j += 1
 

# COLLECTIONS .NamedTuple()
from collections import namedtuple

N = int(input()) # Enter your code here. Read input from STDIN. Print output to STDOUT

Student = namedtuple('Student',','.join(input().strip().split())) # initialize the named tuple
# initialize auxiliar variables
i = 0
lista = []
while i < N:
    vals = input().strip().split()
    a = Student(vals[0],vals[1],vals[2],vals[3]) # create a new instance of named tuple with the input vals
    lista.append(int(a.MARKS)) # append to 'lista' the MARKS value, casted to int
    i += 1
print(round(sum(lista)/N,2))# print the average of the element in 'lista', rounded to the second decimal digit.


# COLLECTIONS .OrderedDict()
from collections import OrderedDict

prices = OrderedDict()# initialize orderedDict and variables
N = int(input())#number of items
i = 0
while i < N:
    line = input().strip().split()# remove the price with the pop() function (remove and return the last element)
    price = int(line.pop())
    key = ' '.join(line) # define the key with join() method, if line is made by many elements
    if key not in prices.keys(): # update the ordered dict checking if each element in input is already saved in the dict
        prices[key] = price
    else: # else update the price
        prices[key] += price
    i += 1
for key, value in prices.items():# print the couple key-value
    print(key + ' ' + str(value))


# WORD ORDER
n = int(input())
# initialize aux variables
i = 0
diz = {}
while i < n:
    key = str(input())
    if key not in diz.keys(): # update the dictionary, checking if the value is already in it
        diz[key] = 1
    else: # eventually update the value of the key if already inserted
        diz[key] += 1
    i += 1
print(len(diz.keys()))# print the total number of keys (number of distinct words from the input.)
print(' '.join([str(val) for val in diz.values()]))# print as string the list of values (number of occurrences for each distinct word according to their appearance in the input) obtained through a list comprehension


# COLLECTIONS .deque()
from collections import deque

N = int(input())
# initialize aux variables
d = deque()
i = 0
while i < N:
    cmd = input().strip().split() # get the command from input
    if cmd[0] == 'append': # for each command, performs it on 'd'
        d.append(cmd[1])
    elif cmd[0] == 'appendleft':
        d.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        d.pop()
    elif cmd[0] == 'popleft':
        d.popleft()
    i += 1
print(' '.join(d))# print as string with the join() method

# COMPANY LOGO
if __name__ == '__main__':
    s = input()
    diz = {}
    for c in s:
        if c not in diz.keys(): # check if the key is already in the dictionary, otherwise I add it and initialize the value to 1.
            diz[c] = 1
        else: # if the key is already in, update the value
            diz[c] += 1
    # then, thorough a lambda function I sorted the element of the dict by descending order of values. if there are
    # many elements with the same value, I sorted them in alphabetical order
    sorted_diz = dict(sorted(diz.items(), key=lambda item: (-item[1], item[0]))[:3])
    for key, value in sorted_diz.items(): # for loop to print the couple key, value
        print(key + ' ' + str(value))

# PILING UP! TODO

# ---------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------DATE AND TIME----------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------
# CALENDAR MODULE
import calendar

date = input().strip().split()
# initialized the input values to three variables (month, day, year)
month = int(date[0])
day = int(date[1])
year = int(date[2])
cal = calendar.Calendar()# initialize new Calendar() item
itr = cal.itermonthdays2(year,month)# this function, given a year and a month, returns an iterator through the tuples (number of the day of that mont, weekday)
# simply dictionary that has number (0-6) as keys and the relative weekday as value
weekday = {
    0: 'MONDAY',
    1: 'TUESDAY',
    2: 'WEDNESDAY',
    3: 'THURSDAY',
    4: 'FRIDAY',
    5: 'SATURDAY',
    6: 'SUNDAY'
}
for i in itr:
    if i[0] == day:
        print(weekday[i[1]]) # print the right weekday when found the right day of the month
        break

# TIME DELTA
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # .strptime() converts a string to the datetime of the given output
    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta = abs(date1 - date2) # compute the difference between the two dates,must be positive so I used abs() method 
    return str(int(delta.total_seconds()))# cast to int to have the right output beacuse .total_seconds() returns a float

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


# ------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------EXCEPTIONS----------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# EXCEPTIONS
T = int(input())# number of tests
for _ in range(T):# loop over the T  tests
    inp = input().strip().split() # get the given input
    a = inp[0]# assigns the variable as showed in the istructions
    b = inp[1]
    try:
        print(int(int(a) / int(b)))  # try to perform the division
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")# needed to add 'integer division or modulo by zero' as string because the parameter e returned a different string
    except ValueError as e:
        # print the errore
        print("Error Code:",e)

# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------BUILT-IN----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ZIPPED!
# initialize the input()
inp = input().strip().split()
N = int(inp[0])# number of students
X = int(inp[1])# number of lists of marks
tot_list = []
for _ in range(X):# iterate over the marks
    lista = input().strip().split()# get the list of marks
    tot_list.append([float(elem) for elem in lista])# append to 'tot_list' the element of 'lista' but casted to float
zipped = zip(*tot_list)# call zip() using the * symbol because tot_list contains many lists. So we get a list of tuples containing marks for each student.
for z in zipped:# final iteration to print the average for each student
    print(sum(z) / X)

# ATHLETE SORT
# given code
if __name__ == '__main__':
    nm = input().split()
    # initialize input
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input()) # k is given from input
    arr.sort(key=lambda item: item[k])# sort the arr with a lambda function. 'arr' is sorted based on the kth attribute
    for elem in arr:
        elem = [str(e) for e in elem] # update 'elem' by casting every element to string
        print(' '.join(elem)) # print 'elem' as string using .join()


# GINORTS
def sorting(c):#define sorting function
    # for each character of the string returns the char 'c' and the priority so that charsacters are sorted based on their priority
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit():
        if int(c) % 2 != 0:
            return (2, c)
        else:
            return (3, c)

input_string = list(input())
input_string.sort(key=sorting)
print(''.join(input_string))


# --------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------PYTHON FUNCTIONALS----------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

# MAP AND LAMBDA FUNCTION
cube = lambda x: x ** 3# complete the lambda function 

def fibonacci(n):
    list = []
    for i in range(n): # fibonacci solved iteratively
        if i == 0: # base case
            list.append(0)
        elif i == 1: # other base case
            list.append(1)
        else:
            list.append(list[i - 1] + list[i - 2]) # appends to the list the 2 previous elements but only if i > 1
    return list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------REGEX AND PARSING CHALLENGES----------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# DETECT FLOATING POINT NUMBER
t = int(input()) # number of tests

for _ in range(t):
    flt = str(input())
    m = re.match(r'^([+|-])?[0-9]*[\.][0-9]+$', flt) # check if there is a match
    if m: # if a match is found print 'True', else print 'False'
        print(True)
    else:
        print(False)


# RE.split()
regex_pattern = r"[,|\.]"	 # Do not delete 'r'. The pattern '[,|\.]' means that it matches with ',' or '.'
print("\n".join(re.split(regex_pattern, input())))


# group(), groups() and groupdict()
string =str(input())
m = re.search(r'([A-Za-z0-9])\1+', string)# search for the given pattern. \1+ means that the char captured by the first group must repeat at least 2 times in sequence. 
if m: # if found a match
    print(m.group(0)[0])# print the first char of the first match found
else:
    print(-1)


# RE .findall() and RE .finditer()
s = str(input()) # input string
# i have to find all the substring that contains 2 or more vowels.
# (?=...) is a positive lookahead, it finds the match but doesn't consume the string.
# (?:...) is also a positive lookahead and means that there is a not-capturing group.
findall = re.findall(r'(?=(?:[^AEIOUaeiou])([AEIOUaeiou]{2,})(?:[^AEIOUaeiou]))', s)
if len(findall) == 0:  # findall() returns a list of matches, so if len = 0 there isn't any
    print(-1)
else:
    for vowels in findall: # for loop over all the matches and print them
        print(vowels)


# RE .start() and RE .end()
s = str(input())
k = str(input())
m = re.finditer(r'(?=(' + re.escape(k) + '))', s) # used finditer() to use .start() and .end()
list_iterator = [el for el in m] # creaete a list of matches
if len(list_iterator) > 0: # if there is at least one match
    for p in list_iterator: # iterate over the matches
        print((p.start(1), p.end(1) - 1)) # print the couple (start, end)
else: # if not found, print (-1,-1)
    print((-1, -1))


# REGEX SUBSTITUTION
def substitution(match):
    if '&' in match.group(0): # if in the match there is a '&' returns ' and'
        return ' and'
    else: # otherwise returns ' or' if there is a '|'
        return ' or'
        
pattern = r' [\|]{2}(?= )| [&]{2}(?= )' # patter to recognize '&&' or '||' if there are spaces before and after
n = int(input())
lista = []
for _ in range(n):
    line = str(input())
    lista.append(re.sub(pattern, substitution, line)) # apply the substitution of the pattern in the line 
for el in lista: # final print
    print(el)

# VALIDATING ROMAN NUMERALS
regex_pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$' # pattern to recognize roman numeral from 1 to 3999
# divided the pattern into 4 groups: units, tens, hundreds and thousands
# First group (M{0,3}) is for the thousands: matches with 1000/2000/3000 or no digit
# Second group (CM|CD|D?C{0,3}) is for the hundreds: matches with 900 or 400 or 100/200/300/600/700/800
# Third group (XC|XL|L?X{0,3})is for the tenth and it's basically the same as the precedent: mathces with 90 or 40 or 10/20/30/60/70/80
# Last group (IX|IV|V?I{0,3}) is for units:
print(str(bool(re.match(regex_pattern, input()))))

# VALIDATING PHONE NUMBERS
n = int(input()) # number of inputs
for _ in range(n):
    num = str(input())
    # look for a match. The pattern looks for a number that starts with 7 or 8 or 9 and then has 9 more digits
    m = re.match(r'\b[7|8|9][\d]{9}\b', num)
    if m: # if a match is found print 'YES'
        print('YES')
    else: #  otherwise print 'NO'
        print('NO')

# VALIDATING AND PARSING EMAIL ADDRESSES
n = int(input())
pattern = r'<[a-z][a-z0-9\-._]*@[a-z]+\.[a-z]{1,3}>' # pattern to recongize emails
lista = [] # will be the list of tuples to print
for _ in range(n):
    string = input().strip().split()
    m = re.match(pattern, string[1]) # look for the match
    if m: # if there is a match
        lista.append((string[0], m.group())) # add a tuple. string[0] contains the name, while m.group() contains the mail
    else: # if there isn't a match, then continue
        continue
for elem in lista: # print the two elements for each tuple
    print(elem[0] + ' ' + elem[1])


# HEX COLOR CODE
num_lines = int(input())
pattern = r'(?:[.]*:[ .\-a-z0-9(),]*)(#[0-9ABCDEFabcdef]{3,6})(?:, (#[0-9ABCDEFabcdef]{3,6}))*' # defined the pattern
lista = []
for _ in range(num_lines): # iterate over the lines given in input
    stringa = str(input())
    lista += re.findall(pattern, stringa) # for each line look for matches
# create a new list of element containing all the matches
lista = [el for t in lista for el in t]
for el in lista:
    if el != '': # there are some matches with empty string because the relative gorup hasn't found a match in that line
        print(el)

# HTML PARSER - PART 1 TODO
# HTML PARSER - PART 2 TODO
# DETECT HTML TAGS, ATTRIBUTES AND ATTRIBUTES VALUES TODO

# VALIDATING UID
t = int(input()) # number of tests
for _ in range(t):
    uid = str(input())
    # look for a match with this pattern
    m = re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?=[A-Za-z0-9]{10}$)[A-Za-z0-9]*$', uid)

    if m: # if there is a match
        print('Valid')
    else:
        print('Invalid')

# VALIDATING CREDIT CARD NUMBERS TODO
# VALIDATING POSTAL CODES TODO
# MATRIX SCRIPT TODO


# -----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------XML----------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
# XML 1 - FIND THE SCORE
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    output = 0 # initialize the output
    # add the number of attribute.
    # .attrib allows me to find how many attributes are there in the xml file 
    output += len(node.attrib.keys())
    for line in node:
        output += len(line.attrib) # update 'output' with the number of new attribute
        for elem in line: # iterate on line to find others attributes
            output += len(elem.attrib) # increase output
    return output

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# XML 2 - FIND THE MAXIMUM DEPTH
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    if level == -1:
        depth(elem, 0)
    global maxdepth
    # your code goes here
    if level > maxdepth: # update the variable max level if we are in a level bigger
        maxdepth = level
    for e in elem:
        depth(e, level + 1) # recursive call for each 'e' increasing level.  'e' is an element in the XML file

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------CLOSURES AND DECORATIONS----------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# STANDARDIZE MOBILE NUMBERS USING DECORATORS
def wrapper(f):
    def fun(l):
        # complete the function
        lista = []
        for number in l:
            if number[0] == '0': # check if the first number is '0'
                lista.append(int(number[1:]))
            elif number[:3] == '+91': # check if the first chars are '+91'
                lista.append(int(number[3:])) # append to the list the number, casted to int, but starting from the char in the third position
            elif number[:2] == '91': # check if the first 2 digits are '9' and '1'
                if len(number) > 10: # check if the number is of the right length
                    lista.append(int(number[2:])) # then append to the list the number, csted to int, but starting from the char with index 2 
                else:
                    lista.append(int(number))
            else: # otherwise just append the number
                lista.append(int(number))
        lista.sort() # sort the list of numbers
        for number in lista:
            print('+91 ' + str(number)[:5]+ ' ' + str(number)[5:]) # for loop to print the number with the tight format 
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# DECORATORS 2 - NAME DIRECTORY
from operator import itemgetter

def person_lister(f):
    def inner(people):
        # complete the function
        people = [[person[0], person[1], int(person[2]), person[3]] for person in people] # create a new array that allows me to sort it on the parameter in position 2
        # itemgetter() is a method of the operator module that allow me to extract specific element from a collection.
        people.sort(key=itemgetter(2)) # In this case it allows me to sort the array on the elements in position 2
        return [f(person) for person in people] # returns the array of people with f() apllied to each of its elements
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------NUMPY----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# ARRAYS
def arrays(arr):
    # complete this function
    # use numpy.array
    np_arr = numpy.array(arr, dtype=float)  # creat a new numpy array, defining float as the element's type
    return np_arr[::-1] # returns the array reversed

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# SHAPE AND RESHAPE
np_array = numpy.array([int(elem) for elem in input().strip().split()])# create new array from the given input
np_array.shape = (3, 3)# set the array shape as (3,3)
print(np_array)


# TRANSPOSE AND FLATTEN
nm = input().strip().split()
#  set up the variables 'n' and 'm'
n = int(nm[0])
m = int(nm[1])
lista = []
for _ in range(n):# iterate over range(n)
    
    row = input().strip().split()# get the input and update 'lista'
    lista += row
np_arr = numpy.array([int(e) for e in lista])# create a new numpy array starting from the one in input but with the element casted to int
np_arr.shape = (n, m)# reshape the array with the given size
# call the function .transpose() and flatten() and print the resukt
print(np_arr.transpose())
print(np_arr.flatten())


# CONCATENATE
nmp = input().strip().split()
# initialize input
n = int(nmp[0])
m = int(nmp[1])
p = int(nmp[2])
lista = []
for _ in range(n):
    row = input().strip().split()
    lista += row
np_arr1 = numpy.array([int(e) for e in lista]) # initialize first array
np_arr1.shape = (n, p)

lista = []
for _ in range(m):
    row = input().strip().split()
    lista += row
np_arr2 = numpy.array([int(e) for e in lista]) # initialize second array
np_arr2.shape = (m, p) # reshape the array
print(numpy.concatenate((np_arr1, np_arr2), axis=0)) # apply the numpy.concatenate() on the two arrays along the axis '0'

# ZEROS AND ONES
rcn = input().strip().split()
rcn = tuple(int(x) for x in rcn)# create a tuple with 3 int from the input. A tuple is needed because will be used as parameter for zeros() and ones() methods. It represents the size
print(numpy.zeros(rcn, dtype=int))# call the methods .zeros() and .ones() and print the results
print(numpy.ones(rcn, dtype=int))

# EYE AND IDENTITY
numpy.set_printoptions(legacy='1.13')
nm = input().strip().split()# 'n' and 'm' are the size of the final array
n = int(nm[0])
m = int(nm[1])
print(numpy.eye(n, m, k=0))# given a parameter k, numpy.eye() returns a 2-D array with 1's as the diagonal and 0's elsewhere. 


# ARRAY MATHEMATICS
nm = input().strip().split()# 'n' and 'm' are the size
n = int(nm[0])
m = int(nm[1])
lst = []
for _ in range(n):
    lst += input().strip().split()
np_arr1 = numpy.array([int(e) for e in lst])# initialize the first numpy array
np_arr1.shape = (n, m)# reshape the array
lst = []
for _ in range(n):
    lst += input().strip().split()
np_arr2 = numpy.array([int(e) for e in lst])# initialize the second numpy array
np_arr2.shape = (n, m)# reshape the array
# print the results for all the methods called
print(numpy.add(np_arr1, np_arr2))
print(numpy.subtract(np_arr1, np_arr2))
print(numpy.multiply(np_arr1, np_arr2))
print(numpy.divide(np_arr1, np_arr2).astype(int))
print(numpy.mod(np_arr1, np_arr2))
print(numpy.power(np_arr1, np_arr2))


# FLOOR, CEIL AND RINT
numpy.set_printoptions(legacy='1.13')
np_arr = numpy.array([float(e) for e in input().strip().split()])# create the numpy array of float from the given input
# compute the rresults using the numpy methods .floor(), .ceil() and .rint()
print(numpy.floor(np_arr))
print(numpy.ceil(np_arr))
print(numpy.rint(np_arr))


# SUM AND PROD
nm = input().strip().split()
n = int(nm[0])# number of lines
m = int(nm[1])# number of elements per line
lst = []
for _ in range(n):
    lst += input().strip().split() # create a list concatenating each line (I'm gonna reshape later)
np_arr = numpy.array([int(e) for e in lst])# create the numnpy array of int casting the element of 'lst'
np_arr.shape = (n, m) # reshape the array
print(numpy.prod(numpy.sum(np_arr, axis=0)))# sum along axis '0' (vertically) and then compute the product of this sum

# MIN AND MAX
nm = input().strip().split()
n = int(nm[0])# number of lines
m = int(nm[1])# number of elements for each line
lst = []
for _ in range(n):
    lst += input().strip().split()
np_arr = numpy.array([int(e) for e in lst])# creating the numpy.array
np_arr.shape = (n, m) # reshape the array
print(numpy.max(numpy.min(np_arr, axis=1)))# compute the min() alngo axis '1' (horizontally), so the min for each line and then find the max from all the min()


# MEAN, VAR AND STD
nm = input().strip().split()# the first part is the same as the previous excercises
n = int(nm[0])
m = int(nm[1])
lst = []
for _ in range(n):
    lst += input().strip().split()
np_arr = numpy.array([int(e) for e in lst])
np_arr.shape = (n, m)
# compute mean, var and std by using the numpy methods
print(numpy.mean(np_arr, axis=1))
print(numpy.var(np_arr, axis=0))
print(numpy.round(numpy.std(np_arr, axis=None), decimals=11))

# DOT AND CROSS
n = int(input())# 'n' represents the number of lines and the number of elements for each line 
# initialize the first numpy array
lst = []
for _ in range(n):
    lst += input().strip().split()
np_arr1 = numpy.array([int(e) for e in lst])
np_arr1.shape = (n, n)
# initialize the second numpy array
lst = []
for _ in range(n):
    lst += input().strip().split()
np_arr2 = numpy.array([int(e) for e in lst])
np_arr2.shape = (n, n)
print(numpy.dot(np_arr1, np_arr2))# the method numpy.dot(..) compute the matrix product

# INNER AND OUTER
array_a = input().strip().split() 
np_arra = numpy.array([int(a) for a in array_a]) # intialize array a 
array_b = input().strip().split()
np_arrb = numpy.array([int(b) for b in array_b]) # intialize array b
# compute the inner and the pouter product through the  numpy methods
print(numpy.inner(np_arra, np_arrb))
print(numpy.outer(np_arra, np_arrb))

# POLYNOMIALS
# in input is given a list of decimals, on which I'm gonna iterate with the list comprehension and then compute the value of the polynomial
# at the specific value given from input 'float(input())' with the numpy method polyval() 
print(numpy.polyval([float(e) for e in input().strip().split()], float(input())))

# LINEAR ALGEBRA
n = int(input())
lista = []
for _ in range(n):   
    lista += input().strip().split() # concatenate the inputs
np_arr = numpy.array([float(e) for e in lista])
np_arr.shape = (n, n)# create and reshape the numpy array
print(numpy.round(numpy.linalg.det(np_arr), decimals=2))# compute the determinant with the method numpy.linalg.det() and round the result to 2 places after the decimal

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////