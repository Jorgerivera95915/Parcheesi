#!/usr/bin/env python
# coding: utf-8

# In[9]:


from graphics import graphWin, Point, Line
from math import pi, cos, sin

def Koch (Turtle, Length, degree):
    if degree == 0:
        Turtle.draw(length)
    else:
        length1 = length/3
        degree1 = degree - 1
        koch(Turtle, length1, degree1)
        Turtle.turn(-60)
        koch(Turtle, length1, degree1)
        Turtle.turn(120)
        koch(Turtle, length1, degree1)
        Turtle.turn(120)
        koch(Turtle, length1, degree1)
        turtle.turn(-60)
        koch(Turtle, length1, degree1)
        
    class Turtle:
        def _init_(self, point, direction, window):
            self.location = point
            self.direction = direction
            self.win = window
            
        def moveTo(self, newpoint):
            self.location = newpoint
            
        def  _ moveTo(self, length):
            dx = length * cos(self.direction)
            dy = length * sin(self.direction)
            x = self.location.getX()
            y = self.location.getY()
            x += dx
            y += dy
            newpoint = Point( x, y)
            return self.moveTo(newpoint)
        
        def draw(self, length):
            oldLocation = self.location
            self._moveTo(length)
            path = Line(oldLocation, self.Location)
            path.draw(self.win)
            
        def turn(self, direction):
            if direction == -60:
                selfdirection  -= (pi/3)
            elif direction == 120:
                self.direction += (2 * pi/3)
                
        def main():
            length = 500
            degree = 5
            win = GraphWin("Koch Snowf Lake", 800, 800)
            dir = 0
            turtle = Turtle(Point(150, 250), dir, win)
            for i in range(3):
                koch(turtle, length, degree)
                turtle.turn(120)
            win.getMouse()
            
            main()
                    






# In[ ]:




