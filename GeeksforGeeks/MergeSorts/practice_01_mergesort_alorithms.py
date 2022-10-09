class MergeShort:
    def __init__(self,):
        pass

    def split_arr(self,Arr,start,end):
        if start< end:
            mid = start + (end-start)//2

            # Divide Stage: left Arr Split
            self.split_arr(Arr,start,mid)
            # right Arr Split
            self.split_arr(Arr, mid+1,end)

            # Combine: Merge Procedure
            self.merge_procesure(Arr, start, mid, end)
        # print(Arr)
        return Arr


    def merge_procesure(self, Arr, start, mid, end):
        Left_array_length = mid-start+1   # start =0
        Right_Array_length = end-mid      # mid !=0
        i = 0       # left Array pointer
        j = mid+1   # Right Array pointer
        k = 0       # original Array pointer
        left_sub_array = Arr[:Left_array_length]
        right_sub_array = Arr[Left_array_length:]
        # print(left_sub_array, right_sub_array, sep= " <--left Array *|* right Array--> ")
        while i< Left_array_length and j<Right_Array_length:
            if left_sub_array[i]<= right_sub_array[j]:
                Arr[k]= left_sub_array[i]
                i = i+1
            else:
                Arr[k]= right_sub_array[j]
                j = j+1
            k = k+1
        while i<Left_array_length:
            Arr[k]= left_sub_array[i]
            i = i+1
            k = k+1
        while j<Right_Array_length:
            Arr[k] = left_sub_array[j]
            j = j+1
            k = k+1

    def merge_sort(self,Arr):
        if len(Arr)>1:
            mid = len(Arr)//2

            # Splitting Array in Right and Left Sub Array
            L = Arr[:mid]
            R = Arr[mid:]

            self.merge_sort(L)
            print(L, R, sep=" <--left Array *|* right Array--> ")
            print("------------------------------")
            self.merge_sort(R)
            print(L, R, sep=" <--left Array *|* right Array--> ")

            i = j =k =0 # initialising pointer for Left, Right and Arr

            while i <len(L) and j< len(R):
                if L[i]<=R[j]:
                    Arr[k]=L[i]
                    i =i+1
                else:
                    Arr[k]=R[j]
                    j = j+1
                k =k+1

            # Checking any Element left in Left sub Array
            while i<len(L):
                Arr[k]=L[i]
                i = i+1
                k = k+1

            # Checking any Element left in Right sub Array
            while j<len(R):
                Arr[k] = R[j]
                j = j+1
                k = k+1
        return Arr


if __name__ == "__main__":
    Arr = [54,25,65,987,86,0,25,66,45,36]
    # Arr = [12, 11, 13, 5, 6, 7]
    start = 0
    end = len(Arr)-1
    # A = MergeShort().split_arr(Arr,start,end)
    MergeShort().merge_sort(Arr)
    print(Arr)
    # print(shorted_array)
    #
    # pass



