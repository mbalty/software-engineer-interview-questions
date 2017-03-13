class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    @staticmethod
    def from_array(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        node = head
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head


def reverseList(head):
    if not head or not head.next:
        return head
    cur = head.next
    prev = head

    while cur.next:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return cur



# you are given an array of length n-1 that contains all numbers from 1 to n exactly once, besides 1 number that is missing.
# Find that number. (possible solution: gauss sum (sum of 1 to n))
# 	[2,1,4,5] → 3

def findMissingGauss(arr):
    n = len(arr)+1
    sum = n*(n+1)/2 # gauss sum
    for num in arr:
        sum -= num

    return sum

def findMissingXor(arr): # a^a = 0, a^0 = a
    missing = 0
    for i in range(len(arr)):
        missing ^= i+1
        missing ^= arr[i]
    missing ^= len(arr)+1
    return missing


# followup for findMissinggauss  but the array is now sorted. (binary search)
# [1,2,4,5] → 3

def findMissingSorted(arr):
    lo = 0
    hi = len(arr)-1
    while lo < hi:
        mid = (lo+hi)/2
        if arr[mid] == mid+1:
            lo = mid + 1
        else:
            hi = mid

    return hi+1


# move all zeros to end in arr in place
# 	[0,0,3,5,0,1,0,0] → [1,5,3,0,0,0,0,0]

def moveZerosToEnd(arr):
    lo = 0
    hi = len(arr)-1
    while lo<hi:
        while lo<hi and arr[lo] != 0:
            lo += 1
        while lo<hi and arr[hi] == 0:
            hi -= 1
        arr[lo], arr[hi] = arr[hi], arr[lo]



# find 2 numbers in arr that sum up to target
# 	[1,4,2,6,5,3] , 9 → 4,5

def twoSumSet(arr, target):
    cache = set(arr)
    for val in arr:
        if target - val in cache:
            return val, target-val
    return None

def twoSumSorting(arr, target):
    arr.sort()
    lo = 0
    hi = len(arr)-1

    while lo < hi:
        sum = arr[lo] + arr[hi]
        if sum == target:
            return arr[lo], arr[hi]
        elif sum < target:
            lo += 1
        else:
            hi -= 1

    return None



# given a list of stock prices find the maximum profit, given that you can buy and sell once
# 		[2,3,1,2,4,5,2] → 4 (buy at 1 and sell at 5)

def stockMaxProfit(stocks):
    buy = 2**31 # big number
    max_profit = 0
    for sell in stocks:
        if sell < buy:
            buy = sell
        else:
            max_profit = max(max_profit, sell-buy)
    return max_profit




