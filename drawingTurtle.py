import turtle
# Draw a square
skk = turtle.Turtle()
wn = turtle.Screen()
for i in range(4):
	skk.forward(50)
	skk.right(90)

	
# Draw a star
star = turtle.Turtle()
for i in range(50):
	star.forward(50)
	star.right(144)


# Draw a hexagon
polygon = turtle.Turtle()
sides = 6
length = 70
angle = 360.0 / sides
for i in range(sides):
	polygon.forward(length)
	polygon.right(angle)

	
# Draw a spiral square Outside_In
skt = turtle.Turtle()
def sqrfunc(size):
	for i in range(4):
		skt.fd(size)
		skt.left(90)
		size = size - 5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

# Draw a spiral square Inside_Out
sks = turtle.Turtle()
def sqrfunc(size):
	for i in range(4):
		sks.fd(size)
		sks.left(90)
		size = size + 5

		
sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)

# Draw a rainbow benzene
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)

turtle.exitonclick()

# Draw a spiral helix pattern
loadWindow = turtle.Screen()
turtle.speed(2)
for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

turtle.exitonclick()
