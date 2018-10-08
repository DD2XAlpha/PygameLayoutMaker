import os

class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

print("               Game Layout Creator")
print("Put the name of the File")
name = input()

print(Colors.OKBLUE + "Creating " + name + ".py file... " + Colors.ENDC)
f = open(name + ".py",  "w+")
print("Writing info on it...")
f.write("import os\n")
f.write("import pygame\npygame.init()\n")
f.write("win = pygame.display.set_mode((500,500))\n")
f.write("pygame.display.set_caption('Game')\n\n")
f.write("run = True\n")
f.write("while run:\n")
f.write("   pygame.time.delay(40)\n")
f.write("   for event in pygame.event.get():\n")
f.write("       if event.type == pygame.QUIT:\n")
f.write("           run = False\n")
f.write("   win.fill((0,0,0))\n")
f.write("   pygame.display.update()\n")

print(Colors.OKGREEN + "DONE" + Colors.ENDC)
