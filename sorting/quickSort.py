def divide(list):
    # pivot is last element of a list

    if (len(list)==0):
        print (' ')
        return ' '
    elif len(list) == 1:
        print(list[0])
        return list[0]
    else:
        pivot = list[len(list)-1]
        left= []
        right =[]

        for x in list[0:len(list)-1]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)

        print(left)
        print(pivot)
        print(right)
        return divide(left), pivot, divide(right)

def run():
    list = [10,6,2,7,1,2,9,3,5]
    str_result = str(divide(list))
    print(str_result)

#another version
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def run01():
    arr = [10,6,2,7,1,2,9,3,5]
    print("Sorted array:", quick_sort(arr))

#run01()
run()


