import turtle as wugui
bg = wugui.Screen()
wugui.colormode(255)
# sets background
# bg.bgcolor('grey')

# wugui.hideturtle()
wugui.speed(10)  ### 10
wugui.penup()
wugui.pensize(6)
wugui.goto(100,0)
wugui.pendown()
wugui.left(90)
wugui.color((0,0,0),(255,255,0))

# body
wugui.begin_fill()
wugui.forward(200)
wugui.circle(100,180)
wugui.forward(200)
wugui.circle(100,180)
wugui.end_fill()

### goggle band 
wugui.pensize(14)
wugui.penup()
wugui.goto(-100,200)
wugui.pendown()
wugui.right(100)
wugui.circle(500,23)

### the eye
wugui.pensize(3)
wugui.penup()
wugui.goto(40,180)
wugui.pendown()
wugui.seth(60)
wugui.color("black", "white")
wugui.begin_fill()
wugui.circle(50)
wugui.end_fill()

wugui.penup()
wugui.goto(10,200)
wugui.pendown()
wugui.color("black", "black")
wugui.begin_fill()
wugui.circle(20)
wugui.end_fill()

wugui.penup()
wugui.goto(0,205)
wugui.color("black", "white")
wugui.begin_fill()
wugui.circle(5)
wugui.end_fill()

# pants
wugui.penup()
wugui.goto(-100,0)
wugui.pendown()
wugui.seth(0)
wugui.color("black","blue")
wugui.begin_fill()
wugui.forward(20)
wugui.left(90)
wugui.forward(40)
wugui.right(90)
wugui.forward(160)
wugui.right(90)
wugui.forward(40)
wugui.left(90)
wugui.forward(20)
wugui.seth(270)
wugui.penup()
wugui.goto(-100,0)
wugui.circle(100,180)
wugui.end_fill()

# pants -- left strap
wugui.penup()
wugui.goto(-70,20)
wugui.pendown()
wugui.color("black","blue")
wugui.begin_fill()
wugui.seth(45)
wugui.forward(15)
wugui.left(90)
wugui.forward(60)
wugui.seth(270)
wugui.forward(15)
wugui.left(40)
wugui.forward(50)
wugui.end_fill()
wugui.left(180)
wugui.goto(-70,30)
wugui.dot()

# pants -- right strap
wugui.penup()
wugui.goto(70,20)
wugui.pendown()
wugui.color("black","blue")
wugui.begin_fill()
wugui.seth(135)
wugui.forward(15)
wugui.right(90)
wugui.forward(60)
wugui.seth(270)
wugui.forward(15)
wugui.right(40)
wugui.forward(50)
wugui.end_fill()
wugui.left(180)
wugui.goto(70,30)
wugui.dot()

# feet 
wugui.penup()
wugui.goto(4,-100)
wugui.pendown()
wugui.seth(270)
wugui.color("black","black")
wugui.begin_fill()
wugui.forward(30)
wugui.left(90)
wugui.forward(40)
wugui.seth(20)
wugui.circle(10,180)
wugui.circle(400,2)
wugui.seth(90)
wugui.forward(20)
wugui.goto(4,-100)
wugui.end_fill()
wugui.penup()

wugui.goto(-4,-100)
wugui.pendown()
wugui.seth(270)
wugui.color("black","black")
wugui.begin_fill()
wugui.forward(30)
wugui.right(90)
wugui.forward(40)
wugui.seth(20)
wugui.circle(10,-225)
wugui.circle(400,-3)
wugui.seth(90)
wugui.forward(21)
wugui.goto(-4,-100)
wugui.end_fill()

# left hand
wugui.penup()
wugui.goto(-100,60)
wugui.pendown()
wugui.seth(225)
wugui.color("black","yellow")
wugui.begin_fill()
wugui.forward(40)
wugui.left(90)
wugui.forward(36)
wugui.seth(90)
wugui.forward(50)
wugui.end_fill()

# right hand
wugui.penup()
wugui.goto(100,60)
wugui.pendown()
wugui.seth(315)
wugui.color("black", "yellow")
wugui.begin_fill()
wugui.forward(40)
wugui.right(90)
wugui.forward(36)
wugui.seth(90)
wugui.forward(50)
wugui.end_fill()

# logo 
colors = ["red", "orange", "yellow", "green", "grey", "purple", "black"]

wugui.penup()
wugui.goto(-5,-20)
wugui.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    wugui.color(each_color)
    wugui.circle(10)
    wugui.right(angle)
    wugui.forward(5)
wugui.penup()
    
wugui.seth(45)
wugui.forward(20)
#wugui.circle(10,180)
wugui.right(90)
#wugui.circle(10,180)
wugui.forward(20)
#wugui.end_fill()

# creases on the pants and hair color
wugui.penup()
wugui.color("black")
wugui.goto(-100,-20)
wugui.pendown()
wugui.circle(30,90)
wugui.penup()
wugui.goto(100,-20)
wugui.pendown()
wugui.circle(30,-90)

# hair
wugui.penup()
wugui.goto(2,300)
wugui.pendown()
wugui.begin_fill()
wugui.seth(135)
wugui.circle(100,40)
wugui.end_fill()

wugui.penup()
wugui.goto(2,300)
wugui.pendown()
wugui.begin_fill()
wugui.seth(45)
wugui.circle(100,40)

wugui.penup()
wugui.goto(2,300)
wugui.pendown()
wugui.begin_fill()
wugui.seth(90)
wugui.circle(100,40)
wugui.end_fill()


# mouth
wugui.penup()
wugui.goto(-50,100)
wugui.pendown()
wugui.seth(290)
wugui.color("black", "brown")
wugui.begin_fill()
wugui.circle(50, 180)
wugui.left(90)
wugui.forward(97)
wugui.end_fill()

wugui.penup()
wugui.goto(-300, -400)

wugui.color("blue")
wugui.pendown()
wugui.write('Happy Birthday Sweetheart ! \n~ Love Aunt', font=("Bradley Hand ITC", 45, "bold"))

wugui.exitonclick()            


            
            
            
            
            
            
            
            
            
            
            
            
