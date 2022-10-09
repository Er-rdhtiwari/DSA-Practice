"""
1. Given an integer array nums of length n and an integer target, find three integers in nums
such that the sum is closest to the target.[Amazon]
You need to return the sum of three integers.
For example:arr = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: [-1+2+1] = 2 (The sum that is closest to the target is 2)
"""



"""
2. Given three points, check whether they lie on a straight (collinear) or not. [Google]
For example:
Input- [(1,1), (1,6), (0,9)]
Output- No
Input- [(1,1), (1,4), (1,5)]
Output- Yes
"""


class Collinear:
    def __init__(self,points):
        self.points = points

    def all_points(self):
        A,B,C = self.points
        return A,B, C

    def coordinates(self):
        A, B, C = self.all_points()
        (x1, y1), (x2, y2),( x3, y3) = A, B, C      # Smart Approach
        print(x1, y1, x2, y2, x3, y3)
        return x1, y1, x2, y2, x3, y3

    def slope_method(self):
        x1, y1, x2, y2, x3, y3 = self.coordinates()
        # Slope between AB == Slope between BC
        if (y2-y1)*(x3-x2)==(x2-x1)*(y2-y2):
            print(True)
            return True
        print(False)
        return False

    def area_method(self):
        x1, y1, x2, y2, x3, y3 = self.coordinates()
        # area of triangle == 0
        if 0.5* ( x1*(y2-y3)  + x2*(y3-y1)  + x3*(y1-y2) ==0 ):
            print(True)
            return True
        print(False)
        return False

if __name__ == "__main__":
    # points= [(1,1), (1,6), (0,9)]
    points = [(1,1), (1,4), (1,5)]
    Collinear(points).slope_method()
    Collinear(points).area_method()


"""
3. An e-commerce site tracks the purchases made each day. The product that is purchased
the most one day is the featured product for the following day. If there is a tie for the product
purchased most frequently, those product names are ordered alphabetically ascending and
the last name in the list is chosen.[Amazon]
['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
'greenPants', 'greenPants', 'greenPants']
'yellowShirt' - 2
'redHat' - 2
'blackShirt' - 2
'bluePants' - 1
'greenPants' - 3
'pinkHat' - 1
Output - greenPants
"""


class FrequentProduct:
    def __init__(self,product):
        self.product = product
        self.frequency_dict = {}
        self.__max = 0
        self.ITEM = ""

    def item_frequency(self):
        self.product.sort()
        print(self.product)
        for i in self.product:
            if i in self.frequency_dict:
                self.frequency_dict[i] = self.frequency_dict[i]+1
            else:
                self.frequency_dict[i]=1
        print(self.frequency_dict)
        return self.frequency_dict

    def frequent_item_dict_method(self):
        item_dict = self.item_frequency()
        for i in item_dict:
            if self.__max<= item_dict[i]:
                self.__max = item_dict[i]
                self.ITEM = i
        print(self.ITEM,self.__max, sep=" : ")
        return self.ITEM,self.__max




if __name__ == "__main__":
    # product = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
    #             'greenPants', 'greenPants', 'greenPants',"zellt", 'redHat',"zellt", "zellt",]
    product = ['yellowShirt',"zellt", 'redHat',"zellt", "zellt",'blackShirt', 'bluePants', 'redHat', 'pinkHat', 'blackShirt', 'yellowShirt',
               'greenPants', 'greenPants']
    Item, Count = FrequentProduct(product).frequent_item_dict_method()


"""
4. An almost sorted array is given to us and the task is to sort that array completely. Then,
which sorting algorithm would you prefer and why?[Salesforce]
"""