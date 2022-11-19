# 1:  O1_Array: Binary Search question and Application
"""
Facebook:
- not sorted array
- size of array-n=12
- position/index of first infinite (~)
arr = [-23,40,55,1,2,27,-89,~,~,~,~,~]
Note: infinite available only after all integers
"""
# 2: Modified Binary Search
"""
Facebook:
- not sorted array
- size of array-n- not defined
- position/index of first infinite "~"
arr = [-23,40,55,1,2,27,-89,~,~,~,~,~........................]
Note: infinite available only after all integers
"""
# 3: Two pointer approach
"""
arr = 20,40,60,80,90,120,240
- array is sorted
- combination? : sum=210
"""
def combination(arr):
    sum = 210
    first = 0
    last = len(arr)-1
    while first<=last:
        if arr[first]+ arr[last]==sum:
            print( arr[first],arr[last])
            last = last - 1
        elif arr[first]+ arr[last]>sum:
            last = last-1
            # print(last)
        else:
            first = first+1
            # print(first)
    return "Done"
arr = 20,40,60,80,90,120,240
arr1 = 0,10,20,30,40,50,60,80,90,120,180,190,200,210,240
# print(combination(arr1))
# 4:
"""
Brute force approach
Optimised approach
"""
# 5:
"""
- max profit?
- Best time to buy and sell the Stock?
- price in week days(Monday to saturday) - [7,1,5,3,6,4]
"""
# arr =[7,1,5,3,6,4]
arr =[7,10,9,3,16,4]
def max_profit(arr):
    min= float('inf')
    Maxprofit = 0

    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
        elif arr[i]-min>Maxprofit:
            Maxprofit = arr[i]-min
    print(f"---max profit:{Maxprofit}")
    return Maxprofit
# max_profit(arr)
# 6: 2D O1_Array: size-3*4
"""
- integer in each row is shorted from left to right
- first element of each Row> last element of above/previous row
- find 3 is present or not?
- find 32 is present or not?
arr = [       
    [1 ,3 ,5 ,7 ],
    [10,11,16,20],
    [23,30,34,60],
       ]

"""
arr = [
    [1 ,3 ,5 ,7 ],
    [10,11,16,20],
    [23,30,34,60],
       ]  #size:3*4-RC: number of row * number of column, m*n
def search2Darray(arr,target):
    nC = len(arr[0])
    nR = len(arr)
    if nR ==0:
        return False
    left =0
    right = nR*nC-1
    # simple binary search
    while left <=right:
        mid = left + (right - left) // 2
        array_mid_element = arr[mid // nC][mid % nC]
        if array_mid_element== target:
            return True
        elif array_mid_element< target:
            left = mid+1
        elif array_mid_element>target:
            right = mid-1
    return False


print(search2Darray(arr,21))

# print(arr[0][2])
# 7:
# 8:
# 9:
# 10:









