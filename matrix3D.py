import pygame
import random
import time

# set up Pygame
pygame.init()
frame_width = 800
frame_height = 600
frame = pygame.display.set_mode((frame_width, frame_height))

# set up font
font_size = 20
font = pygame.font.Font(None, font_size)

# set up characters
chars = ['0', '1', '\u03A9', '\u03A3', '\u03A8', '\u03A0', '\u0393', '\u03A6']

# set up drops
drops = []
for i in range(0, 80):
    drops.append({'x': random.randint(0, frame_width), 'y': random.randint(0, frame_height), 'speed': random.randint(2, 6), 'char': random.choice(chars), 'color': (255, 0, 0)})

# animation loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # clear screen
    frame.fill((0, 0, 0))

    # draw frame
    frame_box = pygame.draw.rect(frame, (255, 255, 255), (5, 5, frame_width - 10, frame_height - 10), 1)
    frame_title = font.render('CMATRIX', True, (255, 255, 255))
    frame_title_rect = frame_title.get_rect(center=(frame_width // 2, 20))
    frame.blit(frame_title, frame_title_rect)

    # update drops
    for drop in drops:
        drop['y'] += drop['speed']
        if drop['y'] > frame_height:
            drop['y'] = 0
            drop['x'] = random.randint(0, frame_width)
            drop['speed'] = random.randint(2, 6)
            drop['char'] = random.choice(chars)
            drop['color'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        char_text = font.render(drop['char'], True, drop['color'])
        frame.blit(char_text, (drop['x'], drop['y']))

    # update screen
    pygame.display.update()

    # wait a bit before drawing next frame
    time.sleep(0.03)
