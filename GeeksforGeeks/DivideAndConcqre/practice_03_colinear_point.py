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
        # x1, y1 = A
        # x2, y2 = B
        # x3, y3 = C
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
    print("------------------------------")
    # Collinear(points).coordinate()
    Collinear(points).area_method()

"""
How to Prove if Points are Collinear?There are two methods to find whether the three points are collinear or not,
 they are:
   One is the slope formula method : if the slope of any two pairs of points is the same.
         With three points R, S, and T, three pairs of points can be formed, they are: RS, ST, and RT.
         If the slope of RS = slope of ST = slope of RT, then R:(X1,Y1), S:(X2,Y2), and T:(X3,Y3) are collinear points.
         Slope of RS = (y2−y1) / (x2−x1)
         WHERE: R: (X1,Y1)   S:(X2,Y2)
  and
  
   The other is the area of the triangle method.
        AREA OF TRIANGLE = 0.5* ( X1*(Y2-Y3) +
                                               X2*(Y3-Y1) +
                                                            X3*(Y1-Y2))
                                                            
        Formula for area of a triangle formed by three points is
            |x1−x2  x2−x3|
        0.5*|            |   == 0
            |y1−y2  y2−y3|
"""

