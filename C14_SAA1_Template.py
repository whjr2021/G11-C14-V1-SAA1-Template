import pygame
import time

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

class Player:
    # Define the __init__ method with properties- self, name, xloc, yloc
    def __init__(self, name, xloc, yloc):
        pygame.init()
        self.name = name
        self.xloc = xloc
        self.yloc = yloc
        
    def image_load(self, location, width, height):
        img = pygame.image.load(location).convert_alpha()
        img_scaled = pygame.transform.smoothscale(img,(width,height))
        return img_scaled
    
    def player_name(self, position):
        font = pygame.font.Font(None, 30)
        text = font.render(self.name, 1, (0, 255,255))
        screen.blit(text, position)
        
    def text_display(size,text,r,g,b,x,y):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (r,g,b))
        screen.blit(text, (x,y))

    def move_up(self):
        self.yloc -= 10
        return self.yloc
    
    def move_down(self):
        self.yloc += 10
        return self.yloc
    
    def move_left(self):
        if self.xloc >= 50:                          
            self.xloc -= 10 
        return self.xloc
    
    def move_right(self):
        if self.xloc <= 320:                          
            self.xloc += 10
        return self.xloc   

carx = 140
cary = 450
red_carx = 300
red_cary = 300
blue_carx = 120
blue_cary = 450
bgy = 0
counter = 0

player1 = Player("John", carx, cary)
player2 = Player("Dodo", red_carx,red_cary)
# Create a player object of class Player for player 3
# 1. Create "player3" object with properties - "Maria", blue_carx, blue_cary


carryOn = True
t1 = time.time()

while carryOn:
    bgImg = pygame.image.load("road.png").convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    yellow_car = player1.image_load("yellow_car.png", 230, 140)
    player1.player_name((carx+90, cary+130))
    red_car = player2.image_load("red_car.png", 80, 130)
    player2.player_name((red_carx+20, red_cary+130))
    
    # Display the player 3 car image and name
    # 1. Display blue car scaled to (80, 130) 

    # 2. Display player3 name at location (blue_carx+20, blue_cary+130)

    
    # Update player location
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary = player1.move_up()
                bgy -= 10
            if event.key == pygame.K_DOWN:
                cary = player1.move_down()
                bgy += 10
            if event.key==pygame.K_RIGHT:
                carx = player1.move_right()
            if event.key==pygame.K_LEFT:
                carx = player1.move_left()  
            if event.key == pygame.K_u:
                red_cary = player2.move_up()
                bgy -= 10
            if event.key == pygame.K_d:
                red_cary = player2.move_down()
                bgy += 10
            if event.key==pygame.K_r:
                red_carx = player2.move_right()
            if event.key==pygame.K_l:
                red_carx = player2.move_left()
                
            # 1. If 'g' alphabet key is press move player2 upward, check for event "pygame.K_g"
            #    Call the method move_up() and store the result in blue_cary 



            # 2. If 'v' alphabet key is press move player2 downward, check for event "pygame.K_v"
            #    Call the method move_down() and store the result in blue_cary 



            # 3. If 'b' alphabet key is press move player2 to the right, check for event "pygame.K_b"
            #    Call the method move_right() and store the result in blue_carx


            # 4. If 'c' alphabet key is press move player2 to the left, check for event "pygame.K_c"
            #    Call the method move_left() and store the result in blue_carx


    
    if cary <= 30:
        bgy = 0
        cary = 450
        counter += 1
            
    t2 = time.time()
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # Display game time elapsed
    Player.text_display(35,"TIME ELAPSED: " + str(game_time)+ "seconds",0, 255,255,130,15)
    
    # Display finish line after 5 iterations of game loop
    # Check if "counter" is equal to 5
    if counter == 5:
        # Create and draw the finish line white-colored rectangle at (x,y)=(95, 40) with width=400 and height=30
        finish_line = pygame.Rect(95,40,400,30)
        pygame.draw.rect(screen,(255,255,255),finish_line)
        Player.text_display(40, "----------FINISH----------", 255,0,0,160,45)
        pygame.display.flip()
        
        # End the game loop after displaying finish line
        pygame.time.wait(3000)
        screen.fill((0,100,200))        
        Player.text_display(40,"Finish time: " + str(round(game_time,2))+ " seconds",255,255,255,140,200)       
        Player.text_display(40,"Game Over, Good Luck Next Time!",255,255,255,80,250)       
        pygame.display.flip()
        pygame.time.wait(5000)
        # Break out of 'while' game loop
        break
    
    screen.blit(yellow_car, (carx, cary))
    screen.blit(red_car, (red_carx, red_cary))
    screen.blit(blue_car, (blue_carx, blue_cary))

    pygame.display.flip()
pygame.quit()