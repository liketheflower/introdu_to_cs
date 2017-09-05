# jimmy shen
# Sep 2, 2017
# Output the ascii code
import turtle

my_trutle = turtle.Turtle()
#For i = 10, 15, 20, 25, ..., 50:
for i in range(10,50,5):
    my_trutle.pensize(i)
    my_trutle.forward(i)
    my_trutle.left(50)
