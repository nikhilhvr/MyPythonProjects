from turtle import*
# Speed can be Changed by increasing and de-creasing values in speed("_")
speed(15)
bgcolor("black")
pencolor("steelblue")

for i in range(140):
    right(i)
    circle(200,i)
    forward(i)
    right(90)
    forward(i)

hideturtle()
turtle.done()
