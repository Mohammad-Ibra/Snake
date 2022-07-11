import pygame
import random
from cube import Cube
from snake import Snake
import tkinter as tk
from tkinter import messagebox


def main():
    ##### INITIALIZING THE GAME ######
    pygame.init()
    global width, rows
    width = 500
    rows = 20
    screen = pygame.display.set_mode((width, width))
    running = True
    ##### TITLE AND ICON #######
    #### SET THE TITLE
    pygame.display.set_caption("The Snake Game")
    #### LOAD THE IMAGE OF THE ICON
    icon = pygame.image.load('src/snake.png')
    #### SET THE ICON
    pygame.display.set_icon(icon)
    ###### PLAYER CREATION ######
    #### CREATE AN INSTANCE OF THE CLASS SNAKE
    snake = Snake(Cube((10, 10)))
    ##### draw Grid ######
    ##### CLOCK ######
    clock = pygame.time.Clock()
    ##### INITIALIZE A SNACK ######
    snack = Cube(pos=(randomSnack(rows, snake)), color=(0,255,0))

    while running:
        
        ## Color the screen black
        screen.fill((0,0,0))
        draw_grid(width,rows,screen)
        clock.tick(10)

        for event in pygame.event.get():
            ## Quit Condition
            if event.type == pygame.QUIT:
                running = False

        snake.draw(screen)
        snake.move()
        snack.draw(screen)
        if snake.head.pos == snack.pos:
            snake.eat()
            snack = Cube(randomSnack(rows, snake), color=(0,255,0))


        #### CHECK FOR COLLISIONS
        body = [b.pos for b in snake]
        score = len(body)   
        if snake.head.pos in list(map(lambda z:z,body[1:])):
            message_box(f'You Lost! your score is {score}', 'Play again...')
            snake.reset((10,10))
        ## UPDATE THE SCREEN
        pygame.display.update()

        
    pygame.quit()

def draw_grid(width ,rows, surface):
    size_btwn = width // rows
    x=0
    y=0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,width))
        pygame.draw.line(surface, (255,255,255), (0,y), (width,y))

def randomSnack(rows, item):
 
    positions = item.head.pos
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

if __name__ == "__main__":
    main()