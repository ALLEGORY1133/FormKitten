import turtle


screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Kuchukcha shakli")


dog = turtle.Turtle()
dog.speed(5)
dog.pencolor("red")


dog.penup()
dog.goto(0, -50)
dog.pendown()
dog.circle(50)  # Bosh


dog.penup()
dog.goto(-50, 50)
dog.pendown()
dog.circle(20)


dog.penup()
dog.goto(50, 50)
dog.pendown()
dog.circle(20)


dog.penup()
dog.goto(-25, 0)
dog.pendown()
dog.dot(15, "red")

dog.penup()
dog.goto(25, 0)
dog.pendown()
dog.dot(15, "red")


dog.penup()
dog.goto(0, -20)
dog.pendown()
dog.dot(20, "red")


dog.penup()
dog.goto(-20, -40)
dog.pendown()
dog.setheading(-60)
dog.circle(20, 120)


dog.penup()
dog.goto(-75, -100)
dog.pendown()
dog.setheading(-90)
dog.circle(75, 180)

dog.setheading(0)
dog.forward(150)


dog.penup()
dog.goto(-50, -175)
dog.pendown()
dog.setheading(-90)
dog.forward(50)

dog.penup()
dog.goto(50, -175)
dog.pendown()
dog.setheading(-90)
dog.forward(50)

dog.penup()
dog.goto(-50, -100)
dog.pendown()
dog.setheading(-90)
dog.forward(50)

dog.penup()
dog.goto(50, -100)
dog.pendown()
dog.setheading(-90)
dog.forward(50)

dog.penup()
dog.goto(75, -50)
dog.pendown()
dog.setheading(45)
dog.circle(25, 180)

turtle.mainloop()


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ALLEGORY1133/FormKitten.git
git push -u origin main