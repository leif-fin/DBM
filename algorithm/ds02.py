# count number of vowels

def number_of_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in str:
        if i.lower() in vowels:
            count += 1
    return count
#print(number_of_vowels('Yes I am leif'))

def run03():
    print(number_of_vowels('HELLO WORLD'))

# '2 Jan 2024'
def run04():
    my_date = '02 Jan 2024'
    my_list = my_date.split()

    print(my_list[2])

# sum odds - can not divide by 2
def sum_odds(n):
    my_list = range(1,n+1) # -1
    result = 0
    for x in my_list:
        if (x % 2) == 1: # odds
            result += x

    return result

def run05():
    print(sum_odds(10))# 1 +3 +5 +7 +9

def isPrime(n):
   if (n % 1) == 0:
       if n <= 1:
           return False
       else:
           # count number of dividend 1..n that make the remainder = 0
           # prime number has count--> 2
           count = 0
           #rint(n)
           list = range(1, n+1)
           for x in list:
               if ((n % x) == 0):
                   count += 1
           #print(count)
           if count == 2:
               return True
           else:
               return False
   else:
       return False

def run06():
    my_list = [11,12,13,14,15,16,17,18,19,20]
    # sum() excludes prime number
    result = 0

    for x in my_list:
        if isPrime(x):
            print(str(x) + ' is a prime number')
            #Do nothing
        else:
            result += x
    print("Sum() excludes prime is " + str(result))
run06()