import sys, pygame, math
pygame.init()
pygame.font.init()

def to_pygame(coords):
      """Convert coordinates into pygame coordinates (lower-left => top left)."""
      return (int(coords[0])), int((height - coords[1]))

def sin():  return math.sin(math.radians(theta))

def cos():  return math.cos(math.radians(theta)) 

def drag(currVel, xDirect):
      calcDrag = (.5 * rho * math.pow(currVel, 2) * surface_area)
      return calcDrag if xDirect else -1 * (calcDrag * currVel) / math.fabs(currVel)

def acceleration(currDrag, yDirec): return gravity + currDrag / mass if yDirec else -1 * currDrag / mass

def velocity(velo, accel): return velo + accel * step

def position(pos, velo): return pos + velo * step

def draw_bullet():
       textsurface = myfont.render(toPrint, False, green)
       screen.blit(textsurface, (0,0))
       pygame.draw.circle(screen, green, to_pygame((x, y)), radius)
       pygame.display.update()
def base_values():
      global x, y, accel, vel
      x = y = 1
      accel = [0, 0]
      vel = [veloi * cos(), veloi * sin()]
def begin_prompt():
     global veloi, surface_area, mass, rho, theta
     if input("Would you like to run a bullet simulation? Y to continue: ") == "Y":
            veloi = float(input("Please enter a the muzzle velocity in m/s: "))
            diameter = float(input("Please enter the caliber or metric diameter , i.e .338 or 10: "))
            #surface area = pi*r^2, .001 meters to a mm and .0254 meters to 1 inch
            surface_area = math.pi * math.pow((diameter * .0254) / 2, 2) if diameter < 1 else math.pi * math.pow(diameter * .001 ,2)
            mass = 6.47989e-5 * float(input("please enter the mass of the bullet in grains: "))
            rho = float(input("Please enter a density of the air. 1.225 is the accepted value at sea level: "))
            theta = float(input("What angle, in degrees, are we shooting at today? Values greater than 90 will be set to 90: "))
            if theta > 90:
                  theta = 90
            base_values()
            return True
     return False
size = width, height = 1536, 864
black = 0, 0, 0
green = 0, 255, 0
white = 255, 255, 255
radius = 2
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bullet Model")
x = 1
y = 1
mass = .016 #mass in kg
gravity = -9.81
surface_area = 5.78883e-5 #Surface area in meters^2
rho = 1.225 #density of the air
theta = .5 #theta in degrees
veloi = 951 #m/s
vel = [veloi * cos(), veloi * sin()] #componentize the velocity at initial point
accel =[0, 0] #x,y 
#vel = 5
step = .004
drag_c = .224
myfont = pygame.font.SysFont('Helvetica', 20)
toPrint = "x = " + str(x) + " y = " + str(y)
count = 0;
if not begin_prompt():
      pygame.quit()
while 1:
      count += 1
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_RETURN]:
            base_values
            screen.fill(black)
            if not begin_prompt():
                  pygame.quit()
      if(y >= radius / 2):
            if (count % 10 == 0):
                  draw_bullet()
                  count = 0
            currDrag = [drag(vel[0], True), drag(vel[1], False)]
            accel = [acceleration(currDrag[0], False),
                     acceleration(currDrag[1], True)]
            vel[0] = velocity(vel[0], accel[0])
            vel[1] = velocity(vel[1], accel[1])
            x = position(x, vel[0])
            y = position(y, vel[1])
            toPrint = "x = " + str(x) + " y = " + str(y)
            screen.fill(black, (0,0,600,100))
