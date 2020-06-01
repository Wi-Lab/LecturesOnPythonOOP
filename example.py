

'''
Abstract Base Class
'''

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


'''
we have no formula for an unknown shape
but we know that every shape has area
'''

'''
we can not instantiate an abstract class
'''
s1 = Shape()


# class Square(Shape):

#     def __init__(self, a):
#         self._a = a

#     def area(self):
#         print(f"Area for square is {(self._a)**2}")


# s1 = Square(2.1)
# s2 = Square(3.2)

# s1.area()
# s2.area()

''' every child class of an abstract class MUST override abstract methods of parent class '''


# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b

#     def calculateArea(self):
#         print(f"Area is {self._a*self._b}")


# r1 = Rectangle(2, 3)
# r1.calculateArea()
