#!/usr/bin/env python

import pygame

IMG_SRC = "../kmaru-resources/images-copyrighted/UFP.png"
background_color = (37,51,129)

# define a main function
def main():
    pygame.init()
    running = True

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    width  = screen.get_width()
    height = screen.get_height()

    image = pygame.image.load(IMG_SRC)

    image_width  = image.get_width()
    image_height = image.get_height()

    offset_w = (width/2  - (image_width/2))
    offset_h = (height/2 - (image_height/2))

    screen.fill(background_color)

    screen.blit(image, (offset_w,offset_h))
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                running = False

if __name__=="__main__":
    main()
