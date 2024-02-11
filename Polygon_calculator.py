
""" The Polygon Area calculator has this features:

- You could create a Rectangle or Square with width and height parameters.

- the set_width method, change the width to the rectangle

- the set_height method, change the height to the rectangle

- set_side, change the side to the square

- get_area, returns the area value for the shape


-get_perimeter, returns the perimeter

-get_diagonal, returns the diagonal measure for the shape

-get_picture, shows in a string the figure shape . 

-get_amount_inside, Calculate how many rectangles fit inside the square
"""


class Rectangle:
	def __init__ (self,width,height):
		self.width=width
		self.height=height

	def __repr__(self):

		return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

	def set_width(self,width):
		self.width=width


	def set_height(self,height):
		self.height=height

	def get_area(self):
		return self.height*self.width

	def get_perimeter(self):
		return (2*self.height)+(2*self.width)


	def get_diagonal(self):
		return ((self.height**2)+(self.width**2))**.5

	def get_picture(self):

		if self.width>50 or self.height>50:
			return "Too big for picture"

		picture=""
		for row in range(self.height):
			picture+='*'*self.width+'\n'

		return picture

	def get_amount_inside(self,poligon):

		return self.get_area()//poligon.get_area()

class Square(Rectangle):

	def __init__ (self,side):
		super().__init__ (side,side)


	def __repr__(self):

		return 'Square(side='+str(self.width)+')'

	def set_side(self,side):
		self.width=side
		self.height=side

	def set_width(self,side):
		self.set_side(side)

	def set_height(self,side):
		self.set_side(side)


	

# ----------------TEST-------------------	
rect = Rectangle(10, 5)# create a rectangle 10(with)x5(height)
print(rect.get_area())#print the area for the rectangle
rect.set_height(3)# modify the height to 3
print(rect.get_perimeter())#calculate the perimeter for the rectangle
print(rect)# shows the rectangle features
print(rect.get_picture())# print the figure shape in string 

sq = Square(9)# create a Squere 9x9
print(sq.get_area())#calculate the area square
sq.set_side(4)#change the side to 4
print(sq.get_diagonal())#calculate the diagonal measure for the square
print(sq)# print the square features
print(sq.get_picture())#shows the square figure 

rect.set_height(8)# change the height to the rectangle
rect.set_width(16)# change the width to the rectangle
print(rect.get_amount_inside(sq))#calculte number of rectangles(rect) that fit inside the square(sq)


