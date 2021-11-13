######################################################
# Project: Project 1
# Student Name:  Patel, Sagar
# UIN: 655397649
# URL: https://replit.com/@SagarkumarPatel/Project1#main.py
######################################################

#Inital settings. 
import turtle
import random
screen = turtle.Screen()
screen.setup(1000, 1000)
t = turtle.Turtle()
t2 = turtle.Turtle()
turtle.tracer(0)
canvas_width = 400
canvas_height = 400
ground_starting_height = -90

#Function for drawing background
def draw_background():
    '''Draw the sky and random grasses at x and y position'''
    #For loop for drawing grass
    for i in range(5):
        x = random.randint(-700, 100)
        y = random.randint(-300, -150)
        draw_grass(x + 50 , y + 10)
    #Draws the trees at different x and y corridents. 
    '''Calling the tree function with different x and y corridents'''
    draw_tree(-500, -200)
    draw_tree(-400, -300)
    draw_tree(-300, -200)
    draw_tree(-200, -300)
    draw_tree(300, -300)
    draw_tree(100, -200)
    draw_tree(400, -200)
    # set screen
    turtle.screensize(canvwidth=1000, canvheight=1000, bg="#87CEEB")
    draw_title()


#Function for drawing triangle
def draw_triangle(t, x, y, heading, pensize, pen_color, fill_color, side_length):
    '''Function for Drawing Triangle'''
    t.setheading(heading)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.pensize(pensize)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(3): 
        t.forward(side_length)
        t.left(120)
    t.end_fill()

#Function for Drawing Circle
def draw_circle (t, x, y, heading, pensize, pen_color, fill_color, radius, extent, steps):
    '''Function for Drawing Cirlce'''
    #Chnages position
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(heading)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.pensize(pensize)
    #Makes the circle
    t.circle(radius, extent, steps)
    t.end_fill()

# Draw rectangle
def draw_rectangle(t, x, y, heading, pensize, pen_color, fill_color, length, width):
    '''Function for Drawing Rectangle'''
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(heading)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.pensize(pensize)
    #Draws the rectangle
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()


#Draws hepatagon
def draw_shape (t2, heading, pensize, pen_color, fill_color, heptagon_length):
    '''Function for Drawing Heptagon'''
    t2.setheading(heading)
    t2.pencolor(pen_color)
    t2.fillcolor(fill_color)
    t2.begin_fill()
    t2.pensize(pensize)
    #Draws the heptagon
    for i in range(6):
        t2.forward(heptagon_length)
        t2.left(60)
    t2.end_fill()

# Function for drawing mountains
def draw_mountain(): 
    '''This Function draws mountains'''
    mountain_side_length = 400
    #draw_triangle(t, x, y, heading, pensize, pen_color, fill_color, side_length)
    draw_triangle(t, -500, -90, 0, 1, '#804f30', '#804f30', mountain_side_length)
    draw_triangle(t, -100, -90, 0, 1, '#804f30', '#804f30', mountain_side_length - 200)
    draw_triangle(t, 100, -90, 0, 1, '#804f30', '#804f30', mountain_side_length - 100)


#Function for Drawing Rainbow
def draw_rainbow():
    '''This function draws rainbow'''
    rainbow_colors = ['#FFB1B0', '#FFDFBE', '#FFFFBF', '#B4F0A7', '#A9D1F7', '#CC99FF']
    i = 0
    #draw_circle (t, x, y, heading, pensize, pen_color, fill_color, radius, extent, steps)
    #conditional statment
    radius = 350
    #Draws the biggest semi circle
    draw_circle (t2, 400, -90, 90, 1, '#FFB1B0', '#FFB1B0', 350, 180, None)
    t2.left(90)
    t2.forward(80)
    t2.left(90)
    #Draws the second biggest semi cirlc
    draw_circle (t2, -280.00, -90, 90, 1, '#FFDFBE', '#FFDFBE', -330, 180, None)
    t2.right(90)
    t2.forward(80)
    t2.right(90)
    #draws the next semi circle after changing the position
    draw_circle (t2, 340, -90, 90, 1, '#FFFFBF', '#FFFFBF', 300, 180, None)
    t2.left(90)
    t2.forward(40)
    t2.left(90)
    #draws the next semi circle after changing position
    draw_circle (t2, -220, -90, 90, 1, '#B4F0A7', '#B4F0A7', -270, 180, None)
    t2.right(90)
    t2.forward(30)
    t2.right(90)
    # You get the idea....
    draw_circle (t2, 290, -90, 90, 1, '#A9D1F7', '#A9D1F7', 240, 180, None)
    t2.left(90)
    t2.forward(-40)
    t2.left(90)
    draw_circle (t2, -170.00, -90, 90, 1, '#CC99FF', '#CC99FF', -210, 180, None)
    t2.right(90)
    t2.forward(5)
    t2.right(90)
    draw_circle (t2, 210.00, -90, 90, 1, "#87CEEB", "#87CEEB", 180, 180, None)

#Function for dawing sun
def draw_sun(): 
    '''Function for drawing sun'''
    y= 200 # intial y position set to 200
    radius = 80 # intial radius
    colors = 0 # intial color
    sun_colors = ['#fca503', '#fc9003', '#fc7703' , '#fc5e03']
    #Required For loop
    for i in range(4):
        # Required Conditional Loop
        if (y <= 60) or (radius >= 20) or (colors <= 3):
            # iterate each color
            draw_circle(t, 300, y, 0, 1, sun_colors[colors], sun_colors[colors], radius, None, None)
            #change the y position
            y += 20
            #change the radius
            radius -=20
            #change the color
            colors += 1


#Function for Drawing Clouds
def draw_clouds():
    '''Function for drawing clouds'''
    number_of_clouds = 6
    for i in range(number_of_clouds):
        # random x position
        random_x = random.randint(-500, 500)
        #random y position
        random_y = random.randint(100, 200)
        starting_value_x = 10
        # draws the cloud using circle
        number_of_cloud_circles= 4
        for i in range (number_of_cloud_circles):
            starting_value_x += 30
            draw_circle(t2, random_x + starting_value_x, random_y, 0, 1, 'white', 'white', 20, None, None)



def draw_ground():
    '''Function for drawing cloud'''
    # Draws the ground   
    draw_rectangle(t, -3000, -90, 0, 1, 'green', 'green', 6000, 6000)

#Function for drawing house
def draw_house(x, y, length, width):
  '''Function for drawing house'''
  t.penup()
  t.goto(x, y)
  t.pendown()
  #Draw Rectangle
  draw_rectangle(t, x, y, 0, 3, 'black', 'blue', length, width)
  # Draw Triangle
  draw_triangle(t, x, y, 0, 3, 'black', 'yellow', length)
  t.penup()
  t.goto(x + 70, (y + 80))
  t.pendown()
  #draw_heptagon (t2, x, y, heading, pensize, pen_color, fill_color, length)
  #draw first heptagon
  draw_shape(t, 0, 3, 'black', 'red', 10 )
  #change the position
  t.penup()
  t.goto((x + 40), (y + 20))
  t.pendown()
  #draw the second heptagon
  draw_shape(t, 0, 3, 'black', 'red', 10 )
  #change position
  t.penup()
  t.goto((x + 100), (y + 20))
  t.pendown()
  # draw the third heptagon
  draw_shape(t, 0, 3, 'black', 'red', 10 )
  #draw the Door
  draw_rectangle(t, (x + 55), (y - 22), 0, 3, 'black', 'peru', length * 1/4, width * 3/4)

# Function for drawing tree
def draw_tree(x, y,):
    '''Draws the tree'''
    t2.penup()
    t2.goto(x, y)
    t2.pendown()
    #Draws the branch
    draw_rectangle(t2, x, y, 0, 2, 'black', 'peru', 20, 50)
    # Draws the second triangle
    draw_triangle(t2, x - 25, y, 0, 2, 'black', 'lightgreen', 70)
    #Draws the third triangle
    draw_triangle(t2, x - 25, y + 30, 0, 2, 'black', 'lightgreen', 70)


# Function that graw grass
def draw_grass(x, y):
  '''Function for drawing grass'''
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.setheading(0)
  t.pencolor('darkgreen')
  t.pensize(3)
  t.left(90)
  t.forward(30)
  t.right(150)
  t.forward(20)
  t.right(-150)
  t.forward(30)
  t.right(150)
  t.forward(30)
  t.right(-120)
  t.forward(30)
  t.right(150)
  t.forward(30)
  t.left(160)
  t.forward(20)
  t.right(160)
  t.forward(30)

# Welcome home Title at corridents (-100, 300)
def draw_title():
    '''Function for title'''
    t.penup()
    t.goto(-100, 300)
    t.pendown()
    t.color('black')
    t.write('Welcome Home!!', font=("Cursive", 30, 'normal'))


# Calls all the 6 objects on the screen    
def draw_object():
    '''Function for calling all the objects inside the draw_object function''' 
    draw_rainbow()
    draw_sun()
    draw_mountain()
    draw_clouds()
    draw_ground()
    draw_house(200, -100, 150, 90)

#prints Name and UIN
turtle.update()
#Runs the program
def main():
    '''Main function that calls all the objects and background elements'''
    draw_object()
    draw_background()

#Main function that runs the whole program
main()

print('Name: Sagar Patel, UIN: 655397649')
screen.exitonclick()
## information for scorers

## on what line number is the required for loop?
## <24>

## on what line number is the required use of a random number?
## <25>

## on what line number is the required use of a conditional statement?
## <167>

## on what line number is the required use of a list?
## <163>

## Special Note: I used Visual Studio Code to make the project so it might look bit different on Replit.

