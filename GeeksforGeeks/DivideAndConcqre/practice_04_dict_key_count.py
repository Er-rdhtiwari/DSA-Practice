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
    # Item = FrequentProduct(product).item_frequency()
    Item, Count = FrequentProduct(product).frequent_item_dict_method()