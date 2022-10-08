"""
# https://practice.geeksforgeeks.org/problems/find-the-median0527/1?page=1&difficulty[]=-2&category[]=Divide%20and%20Conquer&sortBy=submissions
Given an array arr[] of N integers, calculate the median
Example 1:

    Input: N = 5
    arr[] = 90 100 78 89 67
    Output: 89
    Explanation: After sorting the array
    middle element is the median
Example 2:

    Input: N = 4
    arr[] = 56 67 30 79
    Output: 61
    Explanation: After sorting the array. In case of even number of
    elements, average of two middle elements is the median.
"""
class Smart_Solution:
    def find_median(self, v):
        n = len(v)
        v.sort()
        return (v[(n//2)-1] + v[n//2])//2 if n%2 == 0 else v[n//2]


class Solution:
    def find_median(self, v):
        for i in range(len(v)-1):
            for j in range(i,len(v)):
                if v[i]>v[j]:
                    v[i],v[j] = v[j], v[i]
        print("----v:",v)
        if len(v) ==1:
            return v[0]//2
        elif len(v)==2:
            midian = (v[0]+v[1])//2
            return midian
        elif len(v)%2==0:
            mid = len(v)//2
            print("----mid:",mid)
            midian = (v[mid-1]+v[mid])//2
            return midian
        else:
            mid = len(v)//2
            print("----mid:",mid)
            midian = v[mid]
            return midian
        return -1
        # Code here

if __name__ == "__main__":
    v = [ 56, 67, 30, 79]
    v = [90, 100, 78, 89, 67]
    result = Solution().find_median(v)
    print(result)
