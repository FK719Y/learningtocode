# playing around with turtle
import turtle 
print ("find out what does this website looks like in shitty QR")
text = input("enter URL : ")
text = hash(text) #will replace with properhash from hashlib and find a way to use the wider hexadecimal values in a creative way
pirate = str(text) # need to figure out how to play around with storing vlaues
ninja = [] # ninjapoper
colors = ['red', 'blue', 'green','yellow', 'white', 'navy',
          'purple','orange', 'brown', 'pink'] #will later try to figure out a way to make the colors meaningful
for digit in pirate:
    ninja.append (str(digit))
ninja.pop(0)
print ("( ͡° ͜ʖ ͡°)") 
shelly = turtle.Turtle()
turtle.bgcolor('black')
shelly.speed(10)
for i in range(19): # size of hash digest value 
                    #this place will be filled with "creativity"    
    shelly.width(i/10 + 5)
    shelly.pencolor(colors[i%10]) #NEEDS IMPROVMENT AS ABOVE
    shelly.forward(100)
    shelly.right(90)
    shelly.forward(10 * int(ninja[i]))
    shelly.left(90)
    shelly.forward(10 * int(ninja[i]))
    shelly.right(60)
    shelly.penup()
    shelly.setposition(0, 0)
    shelly.pendown()
    shelly.right(60)
    
turtle.done()
