import sys, pygame, math
#pygame.init()
#pygame.font.init()

def to_pygame(coords):
      """Convert coordinates into pygame coordinates (lower-left => top left)."""
      return (int(coords[0])), int((height - coords[1]))

def sin():  return math.ceil(math.sin(math.radians(theta)))

def cos():  return math.ceil(math.cos(math.radians(theta))) 

def drag(currVel, xDirect):
      calcDrag = (.5 * drag_c * rho * math.pow(currVel, 2) * surface_area)
      if xDirect:
            return calcDrag
      return -1 * ((calcDrag * currVel) / math.fabs(currVel))
      #return calcDrag if xDirect else -1 * (calcDrag * currVel) / math.fabs(currVel)

def acceleration(currDrag, yDirec): #return gravity + currDrag / mass if yDirec else -1 * currDrag / mass
      if yDirec:
            return gravity + (currDrag / mass)
      return -1 * currDrag / mass

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
     ''' global veloi, surface_area, mass, rho, theta,
      if input("Would you like to run a bullet simulation? Y to continue: ") == "Y" or == "y":
            veloi = input("Please enter a the muzzle velocity in m/s: ")
            diameter = input("Please enter the caliber or metric diameter as a whole number: ")
            cal_or_mm = input("Caliber or mm?: ") '''
     return 0
size = width, height = 1536, 864
black = 0, 0, 0
green = 0, 255, 0
white = 255, 255, 255
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Bullet Model")
radius = 2
x = 1
y = 1
mass = .016 #mass in kg
gravity = -9.81
surface_area = 5.78883e-5 #Surface area in meters^2
rho = 1.225 #density of the air
theta = 2 #theta in degrees
veloi = 951 #m/s
vel = [veloi * cos(), veloi * sin()] #componentize the velocity at initial point
accel =[0, 0] #x,y 
#vel = 5
step = .004
drag_c = .224
#myfont = pygame.font.SysFont('Helvetica', 20)
toPrint = "x = " + str(x) + " y = " + str(y)
data_point = 0
while(y >= 0):
      print("step: " + str(data_point) + " x: " + str(x) + " y: " + str(y))
      print("pygame coords: ", to_pygame((x,y)))
      data_point += 1
      currDrag = [drag(vel[0], True), drag(vel[1], False)]
      accel = [acceleration(currDrag[0], False),
               acceleration(currDrag[1], True)]
      x = position(x, vel[0])
      y = position(y, vel[1])
      vel[0] = velocity(vel[0], accel[0])
      vel[1] = velocity(vel[1], accel[1])
      print(str(y))
      toPrint = "x = " + str(x) + " y = " + str(y)
