import random, pygame, time, sys
pygame.init()
#Globals
#Classes
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (119,157,255)
RED = (255,64,34)
PURPLE = (184,120,255)
YELLOW = (255,243,17)
ORANGE = (255,166,33)
GREEN = (65,255,85)
BROWN = (99,73,5)
LIGHT_GREY = (55,54,56)
WIN_W = 275*3
WIN_H = 183*3
SHIP_WIDTH = SHIP_HEIGHT = 32


class Camera(object):
    def __init__(self, total_width, total_height):
        self.state = pygame.Rect(0, 0, total_width, total_height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target_rect):
        self.state = pygame.Rect(-target_rect.x + WIN_W/2, -target_rect.y + WIN_H/2, self.state.width, self.state.height)

class Lee():
    def __init__(self):
        self.health = 100
        self.move1name = "Set Quiz back A Week"
        self.move2name = "Participation"
        self.move3name = "UUhhhhhhhhhh Yeah"
        self.move4name = "Can I sit down?"
    def move_1(self):
        self.health -= 20
        return 0
    def move_2(self):
        return 20
    def move_3(self):
        return 0
    def move_4(self):
        return 20

class Arthur():
    def __init__(self):
        self.health = 100
        self.name = "Arthur"
        self.move1name = "Talk"
        self.move2name = "Code"
        self.move3name = "Youtube"
        self.move4name = "Music"
    def move_1(self):
        self.health -= 20
        return 0
    def move_2(self):
        return 20
    def move_3(self):
        self.health -= 20
        return 0
    def move_4(self):
        self.health -= 20
        return 0

class Evan():
    def __init__(self):
        self.health = 100
        self.name = "Evan"
        self.move1name = "Talk"
        self.move2name = "Code"
        self.move3name = "Youtube"
        self.move4name = "Music"
    def move_1(self):
        self.health -= 20
        return 0
    def move_2(self):
        return 20
    def move_3(self):
        self.health -= 20
        return 0
    def move_4(self):
        self.health -= 20
        return 0

class Ray():
    def __init__(self):
        self.health = 100
        self.name = "Ray"
        self.move1name = "Bahlegdah"
        self.move2name = "Communism"
        self.move3name = "Chabad Subscription"
        self.move4name = "Vote For Trump"
    def move_1(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0
    def move_2(self):
        self.health -= 10
        return -10
    def move_3(self):
        return 20
    def move_4(self):
        self.health -= 10
        return 30

class Blake():
    def __init__(self):
        self.health = 100
        self.name = "Blake"
        self.move1name = "Watch Club Pengiun"
        self.move2name = "Touch Wills Hair"
        self.move3name = "Open All Apps"
        self.move4name = "Mess With Dean"
    def move_1(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0
    def move_2(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0
    def move_3(self):
        return 20
    def move_4(self):
        return random.randrange(0,30)

class Will():
    def __init__(self):
        self.health = 100
        self.name = "Will"
        self.move1name = "Do The Code At Home"
        self.move2name = "Help Darren"
        self.move3name = "Make A List"
        self.move4name = "Let Them Feel Hair"
    def move_1(self):
        self.health += 30
        if self.health > 100:
            self.health = 100
        return 0
    def move_2(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        return 10
    def move_3(self):
        return 20
    def move_4(self):
        self.health -= 15
        return random.randrange(0,36)

class Tjett():
    def __init__(self):
        self.health = 100
        self.name = "Tjett"
        self.move1name = "Research History"
        self.move2name = "Fuck Everything Up"
        self.move3name = "Make Weird Reference"
        self.move4name = "Stutter"
    def move_1(self):
        self.health -= 15
        return 0
    def move_2(self):
        self.health -= 15
        return 0
    def move_3(self):
        self.health -= 15
        return 0
    def move_4(self):
        self.health -= 15
        return 0

class Water():
    def __init__(self):
        self.health = 100
        self.name = "Water"
        self.move1name = "Help Darren"
        self.move2name = "Make srpg"
        self.move3name = "Learn To Code"
        self.move4name = "Get Comp Back"
    def move_1(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        return 10
    def move_2(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0
    def move_3(self):
        return 20
    def move_4(self):
        return random.randrange(-10,41)

class Steven():
    def __init__(self):
        self.health = 100
        self.name = "Steven"
        self.move1name = "Talk"
        self.move2name = "Code"
        self.move3name = "Youtube"
        self.move4name = "Music"
    def move_1(self):
        self.health -= 20
        return 0
    def move_2(self):
        return 20
    def move_3(self):
        self.health -= 20
        return 0
    def move_4(self):
        self.health -= 20
        return 0

class Darren():
    def __init__(self):
        self.health = 100
        self.name = "Darren"
        self.move1name = "Spread Sickness"
        self.move2name = "Get Help"
        self.move3name = "Bring Laptop"
        self.move4name = "Fail SAT"
    def move_1(self):
        return 25
    def move_2(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0
    def move_3(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        return 10
    def move_4(self):
        return 0

class Dean():
    def __init__(self):
        self.health = 100
        self.name = "Dean"
        self.move1name = "Talk"
        self.move2name = "Code"
        self.move3name = "Come To Class"
        self.move4name = "Turn On Computer"
    def move_1(self):
        self.health -= 10
        return -10
    def move_2(self):
        self.health -= 10
        return -10
    def move_3(self):
        self.health -= 10
        return -10
    def move_4(self):
        self.health -= 10
        return -10

class Patrick():
    def __init__(self):
        self.health = 100
        self.name = "Patrick"
        self.move1name = "Harass Dean"
        self.move2name = "Play CSGO"
        self.move3name = "Comm A Comm O"
        self.move4name = "Talk"
    def move_1(self):
        return random.randrange(0,30)
    def move_2(self):
        return 20
    def move_3(self):
        return 20
    def move_4(self):
        return 20

class John():
    def __init__(self):
        self.health = 100
        self.name = "John"
        self.move1name = "Set Backround"
        self.move2name = "Code"
        self.move3name = "Play CSGO"
        self.move4name = "Photoshop"
    def move_1(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0
    def move_2(self):
        return 20
    def move_3(self):
        return 20
    def move_4(self):
        self.health += 20
        if self.health > 100:
            self.health = 100
        return 0


class Ship(pygame.sprite.Sprite):
    def __init__(self,container):
        pygame.sprite.Sprite.__init__(self)
        self.side_speed = 32
        self.top_speed = 32
        self.speed = 32
        self.image = pygame.Surface((SHIP_WIDTH, SHIP_HEIGHT)).convert()
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = 21*32
        self.rect.y = 2*32
        self.container = container
        self.rect.move(WIN_W/2,WIN_H/2)
    def collide(self, x, y, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.rect.right > p.rect.left:
                    self.rect.right = p.rect.left

                elif self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right

                elif self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top

                elif self.rect.top < p.rect.bottom:
                    self.rect.top = p.rect.bottom
    def update(self,platform_group,character1):
        #Movement
        key = pygame.key.get_pressed()




        #Movement and barriers
        if key[pygame.K_w] or key[pygame.K_UP]:
            if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
                self.rect.y -= self.speed

                pygame.time.wait(100)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.top < p.rect.bottom:
                            self.rect.top = p.rect.bottom
            else:
                self.rect.y -= self.speed
                pygame.time.wait(200)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.top < p.rect.bottom:
                            self.rect.top = p.rect.bottom
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
                self.rect.y += self.speed
                pygame.time.wait(100)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.bottom > p.rect.top:
                            self.rect.bottom = p.rect.top
            else:
                self.rect.y += self.speed
                pygame.time.wait(200)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.bottom > p.rect.top:
                            self.rect.bottom = p.rect.top
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
                self.rect.x -= self.speed
                pygame.time.wait(100)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.left < p.rect.right:
                            self.rect.left = p.rect.right
            else:

                self.rect.x -= self.speed
                pygame.time.wait(200)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.left < p.rect.right:
                            self.rect.left = p.rect.right
        if key[pygame.K_d]or key[pygame.K_RIGHT]:
            if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
                self.rect.x += self.speed
                pygame.time.wait(100)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.right > p.rect.left:
                            self.rect.right = p.rect.left
            else:
                self.rect.x += self.speed
                pygame.time.wait(200)
                self.person_collide(platform_group,character1)
                for p in platform_group:
                    if pygame.sprite.collide_rect(self, p):
                        if self.rect.right > p.rect.left:
                            self.rect.right = p.rect.left
        if key[pygame.K_i]:
            sys.exit()
        #self.collide(self.rect.x,self.rect.y,platform_group)
        #Screen
        #if self.rect.top < 0:
            #self.rect.top = 0
        #if self.rect.bottom > total_height:
            #self.rect.bottom = total_height
    def person_collide(self, platform_group,character1):
        for p in platform_group:
            if pygame.sprite.collide_rect(self,p) and p.col == "L":
                character2 = Lee()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "1":
                character2 = Arthur()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "2":
                character2 = Evan()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "3":
                character2 = Ray()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "4":
                character2 = Blake()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "5":
                character2 = Will()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "6":
                character2 = Tjett()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "7":
                character2 = Water()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "8":
                character2 = Steven()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "9":
                character2 = Darren()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "0":
                character2 = Dean()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "-":
                character2 = Patrick()
                battle(character1,character2)
            if pygame.sprite.collide_rect(self,p) and p.col == "+":
                character2 = John()
                battle(character1,character2)

#Function#
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, col):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.convert()
        if col == "P":
            self.image.fill(BLACK)
        if col == "C":
            self.image.fill(LIGHT_GREY)
        if col == "H":
            self.image.fill(ORANGE)
        if col == "D":
            self.image.fill(BROWN)
        if col == "L":
            self.image.fill(YELLOW)
        if col == "1":
            self.image.fill(ORANGE)
        if col == "2":
            self.image.fill(ORANGE)
        if col == "3":
            self.image.fill(ORANGE)
        if col == "4":
            self.image.fill(ORANGE)
        if col == "5":
            self.image.fill(ORANGE)
        if col == "6":
            self.image.fill(ORANGE)
        if col == "7":
            self.image.fill(ORANGE)
        if col == "8":
            self.image.fill(ORANGE)
        if col == "9":
            self.image.fill(ORANGE)
        if col == "0":
            self.image.fill(ORANGE)
        if col == "-":
            self.image.fill(ORANGE)
        if col == "+":
            self.image.fill(ORANGE)
        self.col = col
        self.rect = pygame.Rect(x, y, 32, 32)

def battle(character1,character2):
    play = True
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    beg_time = pygame.time.get_ticks()
    font = pygame.font.Font(None, 50)
    smallfont = pygame.font.Font(None, 30)
    screenimage = pygame.image.load("image/background.png")
    screenimage = pygame.transform.scale(screenimage, (WIN_W,WIN_H))
    clock = pygame.time.Clock()
    picktext = font.render("Pick Your touch me Character", 1, BLACK)
    picktextpos = picktext.get_rect()
    picktextpos.centerx = WIN_W/2
    fps = 90

    character1healthamount = 171
    character2healthamount = 171
    character1health = pygame.Surface((character1healthamount, 16))
    character1healthrect = character1health.get_rect()
    character1healthrect.x = 596
    character1healthrect.y = 306
    character1health.fill(RED)
    #introhitbox = pygame.Surface((introstartpos.width,introstartpos.height),1,GREEN)
    ##introhitboxpos = introstart.get_rect()
    #introhitboxpos.centerx = screen.get_rect().centerx
    #introhitboxpos.y = intropos.y + 100
    enemyhealth = pygame.Surface((character2healthamount,16))
    enemyhealthrect = enemyhealth.get_rect()
    enemyhealthrect.x = 177
    enemyhealthrect.y = 110
    enemyhealth.fill(RED)
    move1text = font.render(character1.move1name, 1, BLACK)
    move1textpos = move1text.get_rect()
    move1textpos.x = 50
    move1textpos.y = 400
    move2text = font.render(character1.move2name, 1, BLACK)
    move2textpos = move2text.get_rect()
    move2textpos.x = 450
    move2textpos.y = 400
    move3text = font.render(character1.move3name, 1, BLACK)
    move3textpos = move3text.get_rect()
    move3textpos.x = 50
    move3textpos.y = 460
    move4text = font.render(character1.move4name, 1, BLACK)
    move4textpos = move1text.get_rect()
    move4textpos.x = 450
    move4textpos.y = 460
    p1gofirst = True
    blitname = smallfont.render("nothing", 1, BLACK)
    blitnamepos = blitname.get_rect()
    blitnamepos.x = 100
    blitnamepos.y = 360
    character1nameplate = smallfont.render(character1.name, 1, BLACK)
    character1nameplatepos = character1nameplate.get_rect()
    character1nameplatepos.x = 500
    character1nameplatepos.y = 270
    character2nameplate = smallfont.render(character2.name, 1, BLACK)
    character2nameplatepos = character2nameplate.get_rect()
    character2nameplatepos.x = 80
    character2nameplatepos.y = 70
    p1damage = 0
    p2damage = 0
    p1go = False
    p2go = False
    blitmove = font.render("nothing much bruh",1,BLACK)
    blitmovepos = blitmove.get_rect()
    blitmovepos.x = blitnamepos.x#130
    blitmovepos.y = blitnamepos.y#447
    while play:
        character2move = random.randrange(1,5)
        mousepos = pygame.mouse.get_pos()
        print(mousepos)
        SHIP_AIM = [0,1]
        #Checks if window exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.blit(screenimage,(0,0))
        #character1healthrect.
        if p1gofirst == True:
            if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > move1textpos.x and mousepos[0] < move1textpos.x + move1textpos.width and mousepos[1] > move1textpos.y and mousepos[1] < move1textpos.y + move1textpos.height:
                p2damage = character1.move_1()
                blitname = smallfont.render(character1.name + " used " + character1.move1name, 1, BLACK)
                p1go = True
                p1d = p1damage*171*.01
                if p1go == True:
                    character2healthamount -= p2d
                blitmove = smallfont.render(("It did "+ str(p2d)+"damage"),1,BLACK)
                screen.blit(blitmove,blitmovepos)
                screen.blit(screenimage,(0,0))
                screen.blit(blitname,blitnamepos)
                screen.blit(enemyhealth,enemyhealthrect)
                screen.blit(character1health,character1healthrect)

                pygame.display.flip()
                pygame.time.wait(2000)
                if True:
                    blitname = smallfont.render(character1.name + " used " + character1.move1name, 1, BLACK)
                    #print(blitmovepos)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitmove,blitmovepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                if character2move == 1:
                    p1damage = character2.move_1()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move1name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                    p2go = True
                if character2move == 2:
                    p1damage = character2.move_2()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move2name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 3:
                    p1damage = character2.move_3()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move3name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 4:
                    p1damage = character2.move_4()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move4name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
            elif pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > move2textpos.x and mousepos[0] < move2textpos.x + move2textpos.width and mousepos[1] > move2textpos.y and mousepos[1] < move2textpos.y + move2textpos.height:
                p2damage = character1.move_2()
                blitname = smallfont.render(character1.name + " used " + character1.move2name, 1, BLACK)
                p1go = True
                p1d = p1damage*171*.01
                if p1go == True:
                    character2healthamount -= p2d
                blitmove = font.render(("It did " + str(p2d) + "damage"),1,BLACK)
                screen.blit(blitmove,blitmovepos)
                screen.blit(screenimage,(0,0))
                screen.blit(blitname,blitnamepos)
                screen.blit(enemyhealth,enemyhealthrect)
                screen.blit(character1health,character1healthrect)
                pygame.display.flip()
                pygame.time.wait(2000)
                if True:
                    blitname = smallfont.render(character1.name + " used " + character1.move1name, 1, BLACK)
                    #print(blitmovepos)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitmove,blitmovepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                if character2move == 1:
                    p1damage = character2.move_1()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move1name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 2:
                    p1damage = character2.move_2()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move2name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 3:
                    p1damage = character2.move_3()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move3name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 4:
                    p1damage = character2.move_4()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move4name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
            elif pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > move3textpos.x and mousepos[0] < move3textpos.x + move3textpos.width and mousepos[1] > move3textpos.y and mousepos[1] < move3textpos.y + move3textpos.height:
                p2damage = character1.move_3()
                blitname = smallfont.render(character1.name + " used " + character1.move3name, 1, BLACK)
                p1go = True
                p1d = p1damage*171*.01
                if p1go == True:
                    character2healthamount -= p2d
                blitmove = font.render(("It did " + str(p2d) + "damage"),1,BLACK)
                screen.blit(blitmove,blitmovepos)
                screen.blit(screenimage,(0,0))
                screen.blit(blitname,blitnamepos)
                screen.blit(enemyhealth,enemyhealthrect)
                screen.blit(character1health,character1healthrect)
                pygame.display.flip()
                pygame.time.wait(2000)
                if True:
                    blitname = smallfont.render(character1.name + " used " + character1.move1name, 1, BLACK)
                    #print(blitmovepos)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitmove,blitmovepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                if character2move == 1:
                    p1damage = character2.move_1()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move1name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 2:
                    p1damage = character2.move_2()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move2name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 3:
                    p1damage = character2.move_3()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move3name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 4:
                    p1damage = character2.move_4()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move4name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True

            elif pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > move4textpos.x and mousepos[0] < move4textpos.x + move4textpos.width and mousepos[1] > move4textpos.y and mousepos[1] < move4textpos.y + move4textpos.height:
                p2damage = character1.move_4()
                blitname = smallfont.render(character1.name + " used " + character1.move4name, 1, BLACK)
                p1go = True
                p1d = p1damage*171*.01
                if p1go == True:
                    character2healthamount -= p2d
                blitmove = font.render(("It did " + str(p2d) + "damage"),1,BLACK)
                screen.blit(blitmove,blitmovepos)
                screen.blit(screenimage,(0,0))
                screen.blit(blitname,blitnamepos)
                screen.blit(enemyhealth,enemyhealthrect)
                screen.blit(character1health,character1healthrect)
                pygame.display.flip()
                pygame.time.wait(2000)
                if True:
                    blitname = smallfont.render(character1.name + " used " + character1.move1name, 1, BLACK)
                    #print(blitmovepos)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitmove,blitmovepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                if character2move == 1:
                    p1damage = character2.move_1()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move1name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 2:
                    p1damage = character2.move_2()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move2name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 3:
                    p1damage = character2.move_3()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move3name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True
                if character2move == 4:
                    p1damage = character2.move_4()
                    blitmove = font.render(("It did " + str(p1d) + "damage"),1,BLACK)
                    screen.blit(blitmove,blitmovepos)
                    blitname = smallfont.render(character2.name + " used " + character2.move4name, 1, BLACK)
                    screen.blit(screenimage,(0,0))
                    screen.blit(blitname,blitnamepos)
                    screen.blit(enemyhealth,enemyhealthrect)
                    screen.blit(character1health,character1healthrect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    p2go = True


            else:
                screen.blit(move1text,move1textpos)
                screen.blit(move2text,move2textpos)
                screen.blit(move3text,move3textpos)
                screen.blit(move4text,move4textpos)

        p2d = p2damage*171*.01

        if p2go == True:
            character1healthamount -= p1d
        if character1health < 1:
            return "You WIN"
        if character2healthamount < 1:
            return "You lose"
        character1health = pygame.Surface((character1healthamount, 16))
        #character1healthrect = character1health.get_rect()
        character1health.fill(RED)
        enemyhealth = pygame.Surface((character2healthamount, 16))
        #enemyhealthrect = enemyhealth.get_rect()
        enemyhealth.fill(RED)
        screen.blit(character1nameplate,character1nameplatepos)
        screen.blit(character2nameplate,character2nameplatepos)
        screen.blit(enemyhealth,enemyhealthrect)
        screen.blit(character1health,character1healthrect)
        p1go = False
        p2go = False
        #Bullet Shooting
        #print(mousepos)
        #Enemy Adding

        #Update
        if character1healthamount > 171:
            character1healthamount = 171
        if character2healthamount > 171:
            character2healthamount = 171
        #Print Everything
        #for p in platform_group:
            #screen.blit(p.image, camera.apply(p))
        #for s in ship_group:
            #screen.blit(s.image, camera.apply(s))
        #Draw Everything
        #platform_group.draw(screen)
        #ship_group.draw(screen)
        #bullet_group.draw(screen)


        #Limits FPS
        clock.tick(fps)

        #Writes to surface
        pygame.display.flip()
def main():

    #variables
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    beg_time = pygame.time.get_ticks()
    intro = play = character_select = True
    font = pygame.font.Font(None, 100)
    introtext = font.render("Class Clash", 1, BLACK)
    intropos = introtext.get_rect()
    intropos.centerx = screen.get_rect().centerx
    introstart = font.render("Click Here to Start",1,WHITE)
    introstartpos = introstart.get_rect()
    introstartpos.centerx = screen.get_rect().centerx
    introstartpos.y = intropos.y + 100
    introhitbox = pygame.Surface((introstartpos.width,introstartpos.height),1,GREEN)
    introhitboxpos = introstart.get_rect()
    introhitboxpos.centerx = screen.get_rect().centerx
    introhitboxpos.y = intropos.y + 100

    ship = Ship(screen.get_rect())
    ship_group = pygame.sprite.Group()
    ship_group.add(ship)
    platform_group = pygame.sprite.Group()

    Room = [
        "PPPPPPPPPPPPPPPPPPPPPPP",
        "P                     P",
        "P                     D",
        "P          L          P",
        "P        PPCPP       1C",
        "P        PPPPP        P",
        "P        PPPPP       2C",
        "P        PPPPP        P",
        "P        PPPPP       3C",
        "P        PPPPP        P",
        "P        PPPPC+      4C",
        "P        PPPPP        P",
        "P        PPPPC-      5C",
        "P        PPPPP        P",
        "P        PPPPC0      6C",
        "P        PPPPP  9 8 7 P",
        "PPPPPPPPPPPPPPPPCPCPCPP", ]
    x = y = 0
    for row in Room:
        for col in row:
            if col == "P":
                p = Platform(x,y,col)
                platform_group.add(p)
            if col == "C":
                c = Platform(x,y,col)
                platform_group.add(c)
            if col == "H":
                h = Platform(x,y,col)
                platform_group.add(h)
            if col == "D":
                d = Platform(x,y,col)
                platform_group.add(d)
            if col == "L":
                l = Platform(x,y,col)
                platform_group.add(l)
            if col == "1":
                arthur = Platform(x,y,col)
                platform_group.add(arthur)
            if col == "2":
                evan = Platform(x,y,col)
                platform_group.add(evan)
            if col == "3":
                ray = Platform(x,y,col)
                platform_group.add(ray)
            if col == "4":
                blake = Platform(x,y,col)
                platform_group.add(blake)
            if col == "5":
                will = Platform(x,y,col)
                platform_group.add(will)
            if col == "6":
                tjett = Platform(x,y,col)
                platform_group.add(tjett)
            if col == "7":
                water = Platform(x,y,col)
                platform_group.add(water)
            if col == "8":
                darren = Platform(x,y,col)
                platform_group.add(darren)
            if col == "9":
                stephen = Platform(x,y,col)
                platform_group.add(stephen)
            if col == "0":
                dean = Platform(x,y,col)
                platform_group.add(dean)
            if col == "-":
                patrick = Platform(x,y,col)
                platform_group.add(patrick)
            if col == "+":
                john = Platform(x,y,col)
                platform_group.add(john)

            x += 32
        y += 32
        x=0
    total_width = len(Room[0])*32
    total_height = len(Room)*32
    camera = Camera(total_width, total_height)

    #introtext loop
    clock = pygame.time.Clock()
    fps = 90
    while intro:

        mousepos = pygame.mouse.get_pos()
        # Print background
        screen.fill(WHITE)
        screen.blit(introtext, intropos)

        # Blinking Text: Click here to start
        cur_time = pygame.time.get_ticks()
        if ((cur_time - beg_time) % 1000) < 500:
            screen.blit(introhitbox,introhitboxpos)
            screen.blit(introstart, introstartpos)
        #print(pygame.mouse.get_pressed()[0])
            # Limits frames per iteration of while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  sys.exit()
            if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > 110 and mousepos[0] < 715 and mousepos[1] > 100 and mousepos[1] < 169:
                #print ("introtext left is" , introhitboxpos.left)
                #print ("introtext right is" , introhitboxpos.right)
                #print ("introtext bottom is" , introhitboxpos.bottom)
                #print ("introtext top is" , introhitboxpos.top)
                #print mousepos[0]
                #print mousepos[1]
                #print(intro)
                intro = False

        clock.tick(fps)
        # Writes to main surface
        pygame.display.flip()
    pygame.time.wait(500)
    picktext = font.render("Pick Your Character", 1, BLACK)
    picktextpos = picktext.get_rect()
    picktextpos.centerx = WIN_W/2
    #picktextpos.y = WIN_H/7

    arthurtext = font.render("Arthur", 1, BLACK)
    arthurtextpos = arthurtext.get_rect()
    arthurtextpos.centerx = WIN_W/4
    arthurtextpos.y = WIN_H/7

    evantext = font.render("Evan", 1, BLACK)
    evantextpos = evantext.get_rect()
    evantextpos.centerx = WIN_W/4
    evantextpos.y = WIN_H/7 + WIN_H/7

    raytext = font.render("Ray", 1, BLACK)
    raytextpos = raytext.get_rect()
    raytextpos.centerx = WIN_W/4
    raytextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7

    blaketext = font.render("Blake", 1, BLACK)
    blaketextpos = blaketext.get_rect()
    blaketextpos.centerx = WIN_W/4
    blaketextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7

    willtext = font.render("Will", 1, BLACK)
    willtextpos = willtext.get_rect()
    willtextpos.centerx = WIN_W/4
    willtextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7

    tjetttext = font.render("TJett", 1, BLACK)
    tjetttextpos = tjetttext.get_rect()
    tjetttextpos.centerx = WIN_W/4
    tjetttextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7

    watertext = font.render("Water", 1, BLACK)
    watertextpos = watertext.get_rect()
    watertextpos.centerx = WIN_W/2 + WIN_W/4
    watertextpos.y = WIN_H/7

    steventext = font.render("Steven", 1, BLACK)
    steventextpos = steventext.get_rect()
    steventextpos.centerx = WIN_W/2 + WIN_W/4
    steventextpos.y = WIN_H/7 + WIN_H/7

    darrentext = font.render("Darren", 1, BLACK)
    darrentextpos = darrentext.get_rect()
    darrentextpos.centerx = WIN_W/2 + WIN_W/4
    darrentextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7

    deantext = font.render("Dean", 1, BLACK)
    deantextpos = deantext.get_rect()
    deantextpos.centerx = WIN_W/2 + WIN_W/4
    deantextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7

    patricktext = font.render("Patrick", 1, BLACK)
    patricktextpos = patricktext.get_rect()
    patricktextpos.centerx = WIN_W/2 + WIN_W/4
    patricktextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7

    johntext = font.render("John", 1, BLACK)
    johntextpos = johntext.get_rect()
    johntextpos.centerx = WIN_W/2 + WIN_W/4
    johntextpos.y = WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7 + WIN_H/7
    mousepos = pygame.mouse.get_pos()

    while character_select:
        mousepos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  sys.exit()
        screen.blit(picktext,picktextpos)
        screen.blit(arthurtext,arthurtextpos)
        screen.blit(evantext,evantextpos)
        screen.blit(raytext,raytextpos)
        screen.blit(blaketext,blaketextpos)
        screen.blit(willtext,willtextpos)
        screen.blit(watertext,watertextpos)
        screen.blit(tjetttext,tjetttextpos)
        screen.blit(steventext,steventextpos)
        screen.blit(darrentext,darrentextpos)
        screen.blit(deantext,deantextpos)
        screen.blit(patricktext,patricktextpos)
        screen.blit(johntext,johntextpos)
        #get Clicking to work on the people
        mousepos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > arthurtextpos.x and mousepos[0] < arthurtextpos.x + arthurtextpos.width and mousepos[1] > arthurtextpos.y and mousepos[1] < arthurtextpos.y + arthurtextpos.height:
            character_select = False
            character1 = Arthur()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > evantextpos.x and mousepos[0] < evantextpos.x + evantextpos.width and mousepos[1] > evantextpos.y and mousepos[1] < evantextpos.y + evantextpos.height:
            character_select = False
            character1 = Evan()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > raytextpos.x and mousepos[0] < raytextpos.x + raytextpos.width and mousepos[1] > raytextpos.y and mousepos[1] < raytextpos.y + raytextpos.height:
            character_select = False
            character1 = Ray()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > blaketextpos.x and mousepos[0] < blaketextpos.x + blaketextpos.width and mousepos[1] > blaketextpos.y and mousepos[1] < blaketextpos.y + blaketextpos.height:
            character_select = False
            character1 = Blake()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > willtextpos.x and mousepos[0] < willtextpos.x + willtextpos.width and mousepos[1] > willtextpos.y and mousepos[1] < willtextpos.y + willtextpos.height:
            character_select = False
            character1 = Will()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > tjetttextpos.x and mousepos[0] < tjetttextpos.x + tjetttextpos.width and mousepos[1] > tjetttextpos.y and mousepos[1] < tjetttextpos.y + tjetttextpos.height:
            character_select = False
            character1 = Tjett()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > watertextpos.x and mousepos[0] < watertextpos.x + watertextpos.width and mousepos[1] > watertextpos.y and mousepos[1] < watertextpos.y + watertextpos.height:
            character_select = False
            character1 = Water()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > steventextpos.x and mousepos[0] < steventextpos.x + steventextpos.width and mousepos[1] > steventextpos.y and mousepos[1] < steventextpos.y + steventextpos.height:
            character_select = False
            character1 = Steven()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > darrentextpos.x and mousepos[0] < darrentextpos.x + darrentextpos.width and mousepos[1] > darrentextpos.y and mousepos[1] < darrentextpos.y + darrentextpos.height:
            character_select = False
            character1 = Darren()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > deantextpos.x and mousepos[0] < deantextpos.x + deantextpos.width and mousepos[1] > deantextpos.y and mousepos[1] < deantextpos.y + deantextpos.height:
            character_select = False
            character1 = Dean()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > patricktextpos.x and mousepos[0] < patricktextpos.x + patricktextpos.width and mousepos[1] > patricktextpos.y and mousepos[1] < patricktextpos.y + patricktextpos.height:
            character_select = False
            character1 = Patrick()
        if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > johntextpos.x and mousepos[0] < johntextpos.x + johntextpos.width and mousepos[1] > johntextpos.y and mousepos[1] < johntextpos.y + johntextpos.height:
            character_select = False
            character1 = John()
      #  if pygame.mouse.get_pressed()[0] == 1 and mousepos[0] > textpos.x and mousepos[0] < textpos.x + textpos.width and mousepos[1] > textpos.y and mousepos[1] < textpos.y + textpos.height:
       #     character_select = False

        #Set the player to whoever choses on monday

        clock.tick(fps)
        pygame.display.flip()
    while play:
        #Checks if window exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #Update
        ship.update(platform_group,character1)
        camera.update(ship.rect)
        screen.fill(WHITE)

        #Print Everything
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for s in ship_group:
            screen.blit(s.image, camera.apply(s))
        #Draw Everything
        #platform_group.draw(screen)
        #ship_group.draw(screen)
        #bullet_group.draw(screen
        #Limits FPS
        clock.tick(fps)
        #Writes to surface
        pygame.display.flip()
main()