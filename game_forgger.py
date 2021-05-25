import random
import sys
import time

import pygame


class Frog:
    num_frog=5
    def __init__(self):
        self.x = Game.width/2
        self.y= Game.height-75
        self.image=pygame.image.load('image/frog_arrived.png')
        self.rect = self.image.get_rect()
        print(self.rect)
        self.mo=" "
        self.area = Game.screen.blit(self.image, (self.x, self.y))
        self.on_wood = False

    def show(self):
        self.area=Game.screen.blit(self.image,(self.x,self.y))

    def moveFrog(self, x, y):
        self.x +=x*38
        self.y +=y*38
    def new(self):
        self.x = Game.width / 2
        self.y = Game.height - 75
class Platform:
    def __init__(self, line):
        super().__init__()
        self.x= random.randint(0,Game.width)
        self.y =50 * line
        # self.y = 50
        self.image=pygame.image.load('image/tronco.png')
        self.rect = self.image.get_rect()
        self.area = Game.screen.blit(self.image, (self.x, self.y))
        # self.way=way
        self.speed=1
    def show(self):
        self.area=Game.screen.blit(self.image,(self.x,self.y))
        
    def move(self):
        if self.x > Game.width:
            self.x = 0
        self.x += Game.speed


class Car:
    cars = ['image/car2.png', 'image/car3.png', 'image/car4.png', 'image/car1.png']
    def __init__(self,line):
        self.x =random.randint(0,Game.width)

        self.y= 230 + 50 * line
        self.image=pygame.image.load(random.choice(Car.cars))
        self.rect = self.image.get_rect()
        self.speed=3
        self.area = Game.screen.blit(self.image, (self.x, self.y))
    def show(self):
        self.area=Game.screen.blit(self.image,(self.x,self.y))
    def move(self):
        if self.x > Game.width:
            self.x = 0
        self.x += self.speed

class Game:
    width = 448
    height = 546
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("forgger")
    clock = pygame.time.Clock()
    background = pygame.image.load('image/bg.png')
    speed = 2
    @staticmethod
    def play(wood,cars):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        frog.moveFrog(-1, 0)
                    if event.key==pygame.K_RIGHT:
                        frog.moveFrog(1, 0)
                    if event.key==pygame.K_UP:
                        frog.moveFrog(0, -1)
                    if event.key == pygame.K_DOWN:
                        frog.moveFrog(0, 1)
            if frog.x >= Game.width - frog.rect[2]:
                frog.x = Game.width - frog.rect[2]
            elif frog.x<=0:
                frog.x=0
            elif frog.y>Game.height-65:
                frog.y=Game.height - 60

            cars_colid = []
            for n in range(4):
                cars_colid.append(frog.area.colliderect(cars[n].area))
            if any(cars_colid):
                pygame.mixer.music.load("music/boom_antigo.wav")
                pygame.mixer.music.play()
                frog.x -= 100
                frog.num_frog-=1

                print("frog.num_frog1", frog.num_frog)




            wood_colid = []
            for g in range(7):
                wood_colid.append(frog.area.colliderect(wood[g].area))
            if any(wood_colid):
                frog.x += Game.speed
                frog.on_wood=True
            elif Game.height-350>frog.y:
                pygame.mixer.music.load("music/agua.wav")
                pygame.mixer.music.play()
                Frog.num_frog-=1
                frog.new()



            f = []
            for i in range(4):
                if frog.y < 20:
                    f.append(i)
                    for file in f:
                        frog.show()
                    frog.new()


            Game.screen.fill((10, 10, 0))
            Game.screen.blit(Game.background, (0, 0))
            for wooden in wood:
                wooden.show()

            frog.show()
            for car in cars:
                car.show()

            for wooden in wood:
                wooden.move()


            for car in cars:
                car.move()

            endtime = time.time()
            second = endtime - start_time
            if frog.num_frog==0 or second>70:
                txt_score = text.render('game over', True, (255, 255, 255))
                Game.screen.blit(txt_score, [Game.width - 350, Game.height / 2])
                pygame.display.update()
                time.sleep(3)
                pygame.quit()

            txt_score = text_frog.render('froger: %d'% frog.num_frog , True, (255, 255, 255))
            Game.screen.blit(txt_score, [Game.width - 150, Game.height - 35])
            txt_score = text_frog.render('time: %d' % second, True, (255, 255, 255))
            Game.screen.blit(txt_score, [Game.width - 350, Game.height - 35])
            pygame.mixer.init()

            pygame.display.update()
            Game.clock.tick(30)

if __name__=="__main__":
    start_time = time.time()
    wood=[]
    for w in range(4):
        wood.append(Platform(int(w)+1))
        wood.append(Platform(int(w) + 1))
    frog = Frog()
    cars = []
    for m in range(4):
        cars.append(Car(int(m)+1))

    pygame.init()
    text = pygame.font.Font('COMIC.TTF', 50)
    # pygame.font.init()
    text_frog = pygame.font.Font('COMIC.TTF', 17)

    Game.play(wood,cars)