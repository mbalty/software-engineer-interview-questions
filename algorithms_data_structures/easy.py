
# reverse an array or list (preferably in place, otherwise return) - checking a basic for loop
# 	 [1,3,2,4]   →  [4,2,3,1]
# 	 [] → []

def reverse(arr):
    ln = len(arr)
    for i in range(int(ln/2)):
        j = ln-1-i
        arr[i], arr[j] = arr[j], arr[i]




# check if arr has unique elements (here we are interested to hear sorted or set, so we could guide the conversation in that direction)
#     [1,3,2,4]   →  True
#     [1,2,3,2,4] → False

def uniqueWithSet(arr):
    uniq = set()
    for elem in arr:
        if elem in uniq:
            return False
        else:
            uniq.add(elem)
    return True

def uniqueWithSorting(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return False
    return True



# find all elements that repeated in an array ( sorted or dictionary/hashmap are keywords of interest)
# 	[1,3,2,4]   →  []
# 	[1,2,3,2,4,1] → [2,1]

def makeHistorgram(arr):
    """
    makes a histogram dictionary on an array: key = array value, val = number of occurences
    :param arr:
    :return:
    """
    hist = dict()
    for elem in arr:
        count = hist.get(elem, 0)
        hist[elem] = count + 1

    return hist

def findDuplicatesWithDict(arr):
    hist = makeHistorgram(arr)
    duplicates = list()
    for elem, count in hist.items():
        if count > 1:
            duplicates.append(elem)

    return duplicates


def findDuplicatesSorting(arr):
    if not arr:
        return list()
    arr.sort()
    duplicates = set()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            duplicates.add(arr[i])
    return list(duplicates)



# find nth fibonacci number (recursion + dynamic programming, what is the difference)
def fibReccursive(n):
    if n < 0:
        raise Exception('Error Invalid negative input!')
    elif n < 2:
        return n
    else:
        return fibReccursive(n-2) + fibReccursive(n-1)

def fibDynamic(n):
    if n < 0:
        raise Exception('Error Invalid negative input!')
    elif n < 2:
        return n
    fib1, fib2 = 0, 1

    for i in range(2, n+1):
        fib1, fib2 = fib2, fib1+fib2

    return fib2



#tests
def testReverse():
    print("***testing reverse")
    arr = [1,2,3,4]
    print("original", arr)
    reverse(arr)
    print("reversed", arr)


def testUnique():
    print("***testing unique")
    arr = [3,2,4,1,7,6]
    print('unique', arr,  uniqueWithSet(arr), uniqueWithSorting(arr))
    arr = [3,7,2,4,1,7,6]
    print('not-unique', arr, uniqueWithSet(arr), uniqueWithSorting(arr))


def testFindDup():
    print("***tetsing find dup")
    arr = [0,1,0,2,0,4,5,2]
    print("dup", arr, findDuplicatesSorting(arr), findDuplicatesWithDict(arr))


def testFib():
    print("***testing fib")
    n = 10
    print("n ", n, fibReccursive(n), fibDynamic(n))


if __name__ == "__main__":
    testReverse()
    testUnique()
    testFindDup()
    testFib()

