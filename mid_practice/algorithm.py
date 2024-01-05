import random
from time import time

def find_max1():
    num = 5
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0,10))
        i += 1

    max1 = 0
    for x in my_list:
        if x > max1:
            max1 = x
    print('This list include:',my_list)
    print('Max is:',max1)

def find_max2():
    num = 50
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0,10))
        i += 1

    max2 = 0
    score_list = [10,9,8,7,6,5,4,3,2,1,0]
    for x in score_list:
        if my_list.count(x) > 0: # x is in the my_list or not
            max2 = x
            break
    print('Max is:', max2)

def run():
    start_time = time()  # record the starting time
    find_max1()
    end_time = time()  # record the ending time
    elapsed_time = end_time - start_time
    print(elapsed_time)

    start_time2 = time()  # record the starting time
    find_max2()
    end_time2 = time()  # record the ending time
    elapsed_time2 = end_time2 - start_time2
    print(elapsed_time2)


#Range
#Recursion
def sum1(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

def sum2(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + sum2(num - 1)

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def run2():
    print(sum1(5))
    print(sum2(5))
    print(factorial(5))