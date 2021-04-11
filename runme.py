import pygame
from pygame.time import Clock
from spritedex import Spritedex
from robot import Robot
import math
from statemachine import RobotStateMachine, construct_army, tick_army, end_game_check
from bamscript import BAMCompile
import sys

pygame.init()

#width = 1920
#height = 1080
width = 1080
height = 512

clock = Clock()
screen = pygame.display.set_mode((width,height), display=0)

spritedex = Spritedex()

spritedex.load_sheet("assets/robots.json", "Robots")

print("Starting game loop)")
alive = True

# quick maths
l = width//2 - 256//2
t = height//2 - 256//2

larm_arr = ["NEUTRAL", "UP", "SHOOT", "DOWN"]
rarm_arr = ["NEUTRAL", "DOWN", "UP", "IN"]
leg_arr = ["NEUTRAL", "OUT", "BENT", "KICK"]

real_arm_counter = 0

head_bob = 0
head_bob_offset = 0.15

robot_army_size = 64

subsize = width // (robot_army_size + 1)

robots = []
states = []

speed = 15 # fps
tick_speed = 8 # ticks per sec
tick_counter = 0
run = False

# load program
#print(sys.argv[1])
with open(sys.argv[1]) as fp:
    program = fp.read()

end_machine_code, main_machine_code = BAMCompile(program)

states.append(RobotStateMachine(end_machine_code))
robots.append(Robot(spritedex, (subsize,subsize), (subsize//2, height//2 - subsize//2)))

for i in range(robot_army_size-2):
    i+=1 
    states.append(RobotStateMachine(main_machine_code))
    robots.append(Robot(spritedex, (subsize,subsize), (subsize//3 + subsize*i, height//2 - subsize//2)))

states.append(RobotStateMachine(end_machine_code))
robots.append(Robot(spritedex, (subsize,subsize), (subsize//3 + subsize*(robot_army_size-1), height//2 - subsize//2)))

font = pygame.font.Font(pygame.font.get_default_font(), 12)

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye Bye")
            pygame.display.quit()
            alive = False

        if event.type == pygame.KEYDOWN:
            print('*')

            if run:
                run = False
            else:

                run = True
                #tick_army(states)
                if states[0]._current_state == "0":
                    states[0]._current_state = "1"
                print(construct_army(states))
            

    
    if run:
        tick_counter += 1
        if tick_counter > (speed//tick_speed):
            tick_counter = 0
            tick_army(states)
            print(construct_army(states))
            if end_game_check(states):
                run = False

    if alive:
        #screen.fill((200,200,100))
        screen.fill((100,200,200))
        
        for i in range(len(states)):
            robots[i].state = states[i].current_state()
            robots[i].blit(screen)

            fsurface = font.render(states[i].current_state(), True, (255,255,255))
            x,y = fsurface.get_size()
            offset =  (1+i) *subsize - x//2
            screen.blit(fsurface, (offset, height//2+subsize//1.5))

        pygame.display.flip()
        clock.tick(speed)

