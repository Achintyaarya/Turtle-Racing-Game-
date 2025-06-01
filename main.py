import random
import turtle
import time

WIDTH = 750
HEIGHT = 750
COLORS = ['red' , 'green' , 'blue' , 'orange' , 'yellow' , 'black' , 'pink' , 'cyan' , 'purple' , 'brown' ]

# Initialising screen
def init_turtle():

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("TURTLE RACING !")

# Function to get the number of racers
def get_number_of_racers():

    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10) : ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                break
            else:
                print("Please enter a racers between 2 and 10. ")
        else:
            print("This is not numeric... Please Try again.")
    
    return racers

# Function to create turtles
def create_turtles(colors):
    turtles = []
    spacing_btw_turtles = WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer =  turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos((i+1)*spacing_btw_turtles - (WIDTH/2), 20 - (HEIGHT//2))
        racer.pendown()
        turtles.append(racer)
    return turtles

# Function to start the race
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for i,racer in enumerate(turtles):
            distance = random.randrange(1,25)
            racer.forward(distance)
            x,y = racer.pos()
            if y >= HEIGHT//2 -20:
                return colors[i]


# Main Function
def main():
    
    print("Welcome to the turle racing game !")
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print(f"The {winner} turtle is the winner!")
    time.sleep(5)

main()