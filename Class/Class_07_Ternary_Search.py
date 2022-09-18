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
print(ternary_search_while(arr,i,j,85))
print(ternary_search(arr,i,j,25))

# 2:
# 3:
# 4:
# 5:
# 6:
# 7:
# 8:
# 9
# 10:















