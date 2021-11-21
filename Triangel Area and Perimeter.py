class Triangle:
        a = 0
        b = 0
        def __init__(self , base , Height):
                self.base = base
                self.Height = Height
                self.a = (self.base * self.Height)/2
                self.b = self.base*3
        def Area(self):
                print('Hi ' , name , ', Area of the triangle is : %0.2f' % self.a)
        def Perimeter(self):
                print('And the Perimeter of the triangle is : %0.2f' % self.b)

name = input('Enter your name pls : ')

while True:
        base = float(input('Enter the base of the triangle : '))
        Height = float(input('Enter the Height of the triangle : '))

        triangle = Triangle(base , Height)
        triangle.Area()
        triangle.Perimeter()

        Continue = input('If you want to start over, enter y or not enter n : ')
        if Continue != 'y' and Continue!= 'n':
                Continue = input('Enter y or n , pls : ')
        if Continue == 'n':
                break