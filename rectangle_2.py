from rectangle import Rectangle, Square, Circle
# переменные прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# переменные для квадрата
square_1 = Square(5)
square_2 = Square(10)
# переменные для круга
circle_1 = Circle(2)
circle_2 = Circle(4)
# создадим список из фигур
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure,Rectangle):
        print('Площадь прямоугольника ')
        print(figure.get_area())
    if isinstance(figure,Square):
        print('Площадь квадрата ')
        print(figure.get_area_square())
    if isinstance(figure,Circle):
        print('Площадь круга ')
        print(figure.get_circle())




