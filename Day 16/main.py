from turtle import Turtle, Screen

tom = Turtle()
tom.shape('turtle')
tom.color("coral")

print(tom.position())
tom.forward(100)
print(tom.position())

my_screen = Screen()
my_screen.exitonclick()

