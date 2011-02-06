#!/usr/bin/env python

import pygame

IMG_SRC = "../kmaru-resources/images-copyrighted/UFP.png"
background_color = (37,51,129)

def main():
    pygame.init()
    running = True

    # screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((600,500))

    width  = screen.get_width()
    height = screen.get_height()

    image = pygame.image.load(IMG_SRC)

    image_width  = image.get_width()
    image_height = image.get_height()

    offset_w = (width  / 2 - (image_width  / 2))
    offset_h = (height / 4 - (image_height / 2))

    screen.fill(background_color)

    screen.blit(image, (offset_w, offset_h))
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    print "Quit"
                    running = False
                else:
                    keyinput = chr(event.key)
                    print keyinput

if __name__=="__main__":
    main()
