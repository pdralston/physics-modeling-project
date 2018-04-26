import sys, pygame, math
pygame.init()
pygame.font.init()

def to_pygame(coords, height):
      """Convert coordinates into pygame coordinates (lower-left => top left)."""
      return (int)(coords[0]), int(height - coords[1])
def sin(Theta):  return math.sin(math.radians(Theta))
def cos(Theta):  return math.cos(math.radians(Theta)) 
def drag(C, rho, velocity, area, xDirect):
      calcDrag = (.5 * rho * math.pow(velocity, 2) * area * velocity) / math.fabs(velocity)
      return calcDrag if xDirect else -1 * calcDrag
def acceleration(drag, gravity, mass, yDirec): return gravity + drag / mass if yDirec else -1 * drag / mass
def velocity(velo, accel, step): return velo + accel * step
def position(pos, velo, step): return pos + velo * step 
size = width, height = 1536, 864
black = 0, 0, 0
green = 0, 255, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bullet Model")
radius = 10
x = 10
y = 10
mass = 16.19968
gravity = -9.81
bullet_radius = .004293
surface_area = .057888
rho = 1.225
theta = .000001
veloi = 30
vel = [veloi * cos(theta), veloi * sin(theta)]
accel =[0, 0]
#vel = 5
step = .4
drag_c = .224
myfont = pygame.font.SysFont('Helvetica', 20)
#toPrint = "x = " + x + "y = " + y
while 1:
      for event in pygame.event.get():
      	  if event.type == pygame.QUIT:
                pygame.quit()
      #keys = pygame.key.get_pressed()
      #if keys[pygame.K_LEFT]:
       #     x -= vel
      #if keys[pygame.K_RIGHT]:
      #      x += vel
      #if keys[pygame.K_DOWN]:
      #      y -= vel
      #if keys[pygame.K_UP]:
      #      y += vel
      #if keys[pygame.K_RETURN]:
      #      screen.fill(black)
      while(y >= 10):
  #          textsurface = myfont.render(toPrint, False, white)
   #         screen.blit(textsurface, (0,0))
            pygame.draw.circle(screen, green, to_pygame((x, y), height), radius)
            pygame.display.update()
            currDrag = [drag(drag_c, rho, vel[0], surface_area, True),  drag(drag_c, rho, vel[1], surface_area, False)]
            accel = [acceleration(currDrag[0], gravity, mass, False),
                     acceleration(currDrag[1], gravity, mass, True)]
            vel[0] = velocity(vel[0], accel[0], step)
            vel[1] = velocity(vel[0], accel[1], step)
            x = position(x, vel[0], step)
            y = position(y, vel[1], step)
 #           toPrint = "x = " + x + "y = " + y
#screen.fill(black)
