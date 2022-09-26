# 1: Ternary Search
def ternary_search_while(arr,i,j,key):
    mid1 = i+(j-i)//3
    mid2 = j - (j - i) // 3
    while i<=j:
        if arr[mid1]==key:
            return arr[mid1], True
        elif arr[mid2]==key:
            return arr[mid2], True
        elif arr[mid1] >key:
            return ternary_search(arr,i,mid1-1,key)
        elif arr[mid2] < key:
            return ternary_search(arr,mid2+1,j,key)
        else:
            return ternary_search(arr,mid1+1,mid2-1,key)
    return -1,False

# without while loop
def ternary_search(arr,i,j,key):
    mid1 = i+(j-i)//3
    mid2 = j - (j - i) // 3
    try:
        if arr[mid1]==key:
            return arr[mid1], True
        elif arr[mid2]==key:
            return arr[mid2], True
        elif arr[mid1] >key:
            return ternary_search(arr,i,mid1-1,key)
        elif arr[mid2] < key:
            return ternary_search(arr,mid2+1,j,key)
        else:
            return ternary_search(arr,mid1+1,mid2-1,key)
    except:
        return -1,False
arr = [20,25,47,56,59,63,65,79,82]
i = 0
j = len(arr) - 1
# print(ternary_search_while(arr,i,j,85))
# print(ternary_search(arr,i,j,25))

# 2: Shorting
# 3: Comparison based shorting: Bubble/selection/insertion/Quick/Merge/Heap/Shell Short
# 4: Non-Comparison based Shorting: Count/Radix/Bucket sort
# 5: Stable(10-a, 10-b) Vs Unstable Short (10-b, 10-a) Algorithm
# 6: Unstable Short- Quick/Heap Short
# 7: Inplace/Outplace shorting algorithms
# 8: Bubble short


def Bubble_short(arr):
    for i in range(len(arr)):
    # for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


def BubbleShort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
# arr = [99,20, 1,0,1,25, 47,1, 56, 59,1,1,0,0, 63, 65, 79, 82,0,1,0]
# print(Bubble_short(arr))
# print(BubbleShort(arr))


# 9: Selection Shorts
def Selection_shorts(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if  arr[j]<arr[min_index]:
                min_index=j
        # after each complete iteration swap will daon
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

arr = [99,20, 1,0,1,25, 47,1, 56, 59,1,1,0,0, 63, 65, 79, 82,0,1,0]
print(Selection_shorts(arr))

# 10:















