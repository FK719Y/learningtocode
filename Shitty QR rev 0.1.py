text = input("enter URL : ")
text = hash(text)
b = str(text)
ninja = []

colors = ['red', 'black', 'gray','yellow', 'green', 'navy', 'white','red', 'black', 'white','yellow', 'green', 'navy','red', 'black', 'white','yellow', 'green', 'navy']

for digit in b:
    ninja.append (str(digit))
ninja.pop(0)
print (ninja)


import turtle 

shelly = turtle.Turtle()

shelly.speed(10)
for i in range(19):
    shelly.pencolor(colors[i%12])
    shelly.forward(100)
    shelly.right(90)
    shelly.forward(10 * int(ninja[i]))
    shelly.left(90)
    shelly.forward(10 * int(ninja[i]))
    shelly.right(60)
    
    shelly.penup()
    shelly.setposition(0, 0)
    shelly.pendown()
    
    shelly.right(30)
    
turtle.done()
