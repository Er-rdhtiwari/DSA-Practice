# 1:  Data Structure: https://github.com/priya6971
# 2:  Array
# 3: Searching
# 4: Linear Search


def search_element(myarr,n):

    for i in range(len(myarr)):
        if myarr[i]==n:
            print(i)
            return i
    print(-1)
    return -1

# myarr = [20,45,27,47,55,67,75,88,90]
# print(search_element(myarr,67))

# 5: Binary Search: only for sorted Array: ascending/descending order
myarr = [1,5,10,25,35,45,78,80,88,89,99,100]

#
def BynarySearch(myarr, left,right, element):

    mid = left + (right-left)//2
    x = myarr[mid]
    if mid<0 or mid>len(myarr):
        # print(mid)
        return -1
    elif myarr[mid]== element:
        return mid
    elif myarr[mid]> element:
        return  BynarySearch(myarr, left,mid-1, element)
    elif myarr[mid]< element:
        return  BynarySearch(myarr, mid+1,right ,element)


def BynarySearch_2(myarr, left,right, element):
    mid = left + (right - left) // 2
    while mid<len(myarr):

        # print(mid)
        if myarr[mid]== element:
            return mid
        elif myarr[mid]> element:
            return  BynarySearch(myarr, left,mid-1, element)
        elif myarr[mid]< element:
            return  BynarySearch(myarr, mid+1,right ,element)
        # elif mid<1 or mid>len(myarr):
        #     print(mid)
        return -1

print(BynarySearch(myarr, 0,12, 100))



