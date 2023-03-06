import pymunk
import pymunk.pygame_util
import pygame

pygame.init()

GRAY = (220, 220, 220)

size = 640, 240
screen = pygame.display.set_mode(size)
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0, 0

b0 = space.static_body
segment = pymunk.Segment(b0, (0, 240), (640, 240), 4)
segment.elasticity = 1

right = pymunk.Segment(b0, (640, 0), (640, 240), 4)
right.elasticity = 1

left = pymunk.Segment(b0, (0, 0), (0, 240), 4)
left.elasticity = 1

top = pymunk.Segment(b0, (0, 0), (640, 0), 4)
top.elasticity = 1

body = pymunk.Body(mass=1, moment=10)
body.position = 100, 0

circle = pymunk.Circle(body, radius=20)
circle.elasticity = 1
circle.body.apply_force_at_local_point((1000, 1000), (0.1, 0.2))


cart = pymunk.Body(mass=0, moment=0)
cart.position = 320, 240
rectangle = pymunk.Poly(cart, [(10,10),(20,10),(20,15),(10,15)])

space.add(body, circle, segment, right, left, top, cart)

def checkKeys():
     keys=pygame.key.get_pressed()
     if keys[pygame.K_LEFT]:
         circle.body.apply_force_at_local_point((-1000, 0))
     elif keys[pygame.K_RIGHT]:
         circle.body.apply_force_at_local_point((1000, 0))
     else:
         circle.body.apply_force_at_local_point((0, 0))



running = True
while running:
    for event in pygame.event.get():
        checkKeys()
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(GRAY)
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.01)

pygame.quit()