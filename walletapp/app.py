def test01():  #during function
    a = 5
    #print(s)

def test02():
    c1 = 3
    c2 = 3
    code = str(c1) + str(c2)
    print(code)

def test03():
    s1 = '10'
    s2 = '21'
    sum = float(s1) + float(s2)
    print(sum)

def selection02():
    a = 300
    b = 200
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

def forloop01():
    fruits = ["apple", 15, "banana","cherry", "potato", "tomato"]
    for i in fruits:
        print('There is the ' + str(i))

def forloop02():
    full_name = 'Assumption University'
    print(len(full_name))

    for i in full_name:
       # if i != ''
        print('The alphabet is ' + i)

def whileloop01():
    i = 1
    sum = 0
    while i < 6:
        sum += i
        i += 1
    print(sum)

def whileloop02():
    # start at 10
    # increase by 5
    # end with 200
    # 10 + 15 + 20 + ... + 200
    i = 10
    sum = 0
    while i < 205:
        sum += i
        i += 5
    print(sum)

def whileloop3():
    nums = range(10,205,5)
    sum = 0
    for i in nums:
        sum += i
    print(sum)

