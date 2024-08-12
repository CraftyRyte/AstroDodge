import pygess as gess
import pygame as pyg

pyg.init()

# Window
dimensions = (800, 600)
screen = pyg.display.set_mode(dimensions)
pyg.display.set_caption("Hallo")

# Entities
player = gess.entity.RectMovingEntity(dimensions[0]/2 - 15, dimensions[1]/2 - 15, 30, 30, (0, 0), gess.colors.BLUE)

# Loop
is_running = True
clock = pyg.time.Clock()

while is_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            is_running = False
    
    screen.fill((255, 255, 255))
    
    player.update()
    
    pyg.display.update()


pyg.quit()
