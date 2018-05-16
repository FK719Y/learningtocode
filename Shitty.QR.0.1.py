# playing around with turtle
import turtle 
print ("find out what does this website looks like in shitty QR")
text = input("enter URL : ")
text = hash(text)
pirate = str(text)
ninja = []
colors = ['red', 'blue', 'green','yellow', 'white', 'navy',
          'purple','orange', 'brown', 'pink']
for digit in pirate:
    ninja.append (str(digit))
ninja.pop(0)
print ("( ͡° ͜ʖ ͡°)")
shelly = turtle.Turtle()
turtle.bgcolor('black')
shelly.speed(10)
for i in range(19):
    
    shelly.width(i/10 + 5)
    shelly.pencolor(colors[i%10])
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
