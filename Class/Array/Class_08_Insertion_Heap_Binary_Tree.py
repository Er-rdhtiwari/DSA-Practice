# 1: Insertion Shorts
arr = [80,75,99,0,65,1,0,48,1]
# def InsertionShorts(arr):
#     for i in range(len(arr)):
#         i = 1
#         j = i-1
#         key = arr[i]
#         while j>=0 and key< arr[j]:
#             arr[j+1]= arr[j]
#             j = j-1
#         arr[j+1] = key
#     return arr
def InsertionShorts(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and key< arr[j]:
            arr[j+1]= arr[j]
            j = j-1
        arr[j+1] = key
    return arr
print(InsertionShorts(arr))
    # pass
# 2: Outplace/Inplace Shorting algorithms
# 3: Heap Shorts
# 4: Max Heap and Mean Heap
# 5: Tree Data Structure
# 6: Root/Internal/Leaf Node
# 7: Binary Tree
# 8: Full/Almost complete/Complete Binary Tree
# 9: Heap database structure
# 10: Mean(minimum element-parent)/Max Heap(maximum element-parent) and both-Complete Binary Tree
# 11: element index in array =  2 * i+1,  where: -parent index-i
# 12: Skewed binary tree- left/right Skewed binary tree- high wested in array data that's why we use Linked list















