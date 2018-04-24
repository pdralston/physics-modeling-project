import sys, pygame
pygame.init()

def to_pygame(coords, height):
      """Convert coordinates into pygame coordinates (lower-left => top left)."""
      return (coords[0], height - coords[1])

size = width, height = 1536, 864
black = 0, 0, 0
green = 0, 255, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bullet Model")
radius = 25
x = 0
y = 0
vel = 5
while 1:
      for event in pygame.event.get():
      	  if event.type == pygame.QUIT:
                pygame.quit()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
            x -= vel
      if keys[pygame.K_RIGHT]:
            x += vel
      if keys[pygame.K_DOWN]:
            y -= vel
      if keys[pygame.K_UP]:
            y += vel
      pygame.draw.circle(screen, green, to_pygame((x, y), height), radius)
      pygame.display.update()
      screen.fill(black)
