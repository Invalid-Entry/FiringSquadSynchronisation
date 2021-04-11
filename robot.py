import pygame
from pygame import transform, Surface
import random
import math

class Robot():

    spritedex = None
    state = None

    subsurf = None
    finalsurf = None
    size = None
    position = None

    head_bob = None
    body_bob = None

    head_bob_rate = None
    body_bob_rate = None

    def __init__(self, spritedex, size, position):
        self.spritedex = spritedex

        self.state = None
        self.size = size
        self.position = position
        self.subsurf = Surface((256,256), pygame.SRCALPHA)
        self.finalsurf = Surface(size, pygame.SRCALPHA)
        self.head_bob = 0
        self.body_bob = 0

        self.head_bob_rate = random.random() * .5 + 0.1
        self.body_bob_rate = random.random() * .5 + 0.1


    def blit(self, screen):

        arm_counter = 0

        self.head_bob += self.head_bob_rate
        self.body_bob += self.body_bob_rate

        while self.head_bob > math.pi * 2:
            self.head_bob -= math.pi*2

        while self.body_bob > math.pi * 2:
            self.body_bob -= math.pi*2

        body_actual_bob = math.sin(self.head_bob) * 2
        head_actual_bob = math.sin(self.body_bob) * 3
        i = 0

        larm_arr = ["NEUTRAL", "UP", "SHOOT", "DOWN"]
        rarm_arr = ["NEUTRAL", "DOWN", "UP", "IN"]
        leg_arr = ["NEUTRAL", "OUT", "BENT", "KICK"]

        # LARM, RARM, LLEG, RLEG
        states = {
            "BANG": ["SHOOT", "NEUTRAL", "NEUTRAL", "NEUTRAL"],
            "-1": ["SHOOT", "NEUTRAL", "NEUTRAL", "NEUTRAL"],
            "LHG": ["UP", "NEUTRAL", "NEUTRAL", "NEUTRAL"],
            "RHG": ["NEUTRAL", "UP", "NEUTRAL", "NEUTRAL"],
            "MHG": ["UP", "UP", "NEUTRAL", "NEUTRAL"],
            "0": ["NEUTRAL", "NEUTRAL", "NEUTRAL", "NEUTRAL"],
            "1": ["DOWN", "DOWN", "NEUTRAL", "NEUTRAL"],
            "2": ["NEUTRAL", "DOWN", "NEUTRAL", "NEUTRAL"],
            "3": ["NEUTRAL", "NEUTRAL", "OUT", "NEUTRAL"],
            "4": ["NEUTRAL", "NEUTRAL", "NEUTRAL", "OUT"],
            "5": ["NEUTRAL", "NEUTRAL", "OUT", "OUT"],
            "6": ["NEUTRAL", "UP", "NEUTRAL", "OUT"],
            "7": ["NEUTRAL", "UP", "OUT", "NEUTRAL"],
            "8": ["NEUTRAL", "UP", "OUT", "OUT"],
            "9": ["NEUTRAL", "DOWN", "NEUTRAL", "OUT"],
            "10": ["NEUTRAL", "DOWN", "OUT", "NEUTRAL"],
            "11": ["NEUTRAL", "DOWN", "OUT", "OUT"],
            "12": ["DOWN", "NEUTRAL", "NEUTRAL", "OUT"],
            "13": ["DOWN", "NEUTRAL", "OUT", "NEUTRAL"],
            "14": ["DOWN", "NEUTRAL", "OUT", "OUT"],
            "15": ["DOWN", "DOWN", "OUT", "OUT"],
            "16": ["DOWN", "UP", "NEUTRAL", "NEUTRAL"],
            "17": ["DOWN", "UP", "NEUTRAL", "OUT"],
            "18": ["DOWN", "UP", "OUT", "NEUTRAL"],
            "19": ["DOWN", "UP", "OUT", "OUT"],
        }

        self.subsurf.fill((0,0,0,0))
        self.subsurf.blit(self.spritedex.image("Robots", "LARM", states[self.state][0]), (0,0))

        if states[self.state][1] == "UP":
            self.subsurf.blit(self.spritedex.image("Robots", "RARM", "UP"), (14,0))
        else:
            self.subsurf.blit(self.spritedex.image("Robots", "RARM", states[self.state][1]), (-7,0))
        
        self.subsurf.blit(self.spritedex.image("Robots", "LLEG", states[self.state][2]), (0,0))
        self.subsurf.blit(self.spritedex.image("Robots", "RLEG", states[self.state][3]), (0,0))
        self.subsurf.blit(self.spritedex.image("Robots", "BODY", "MAIN"), (-6,body_actual_bob))
        self.subsurf.blit(self.spritedex.image("Robots", "HEAD", "MAIN"), (0,head_actual_bob))

        if self.state == "BANG":
            self.subsurf.blit(self.spritedex.image("Robots", "BANG", "MAIN"), (0,0))
      
        transform.scale(self.subsurf, self.size, self.finalsurf)
        screen.blit(self.finalsurf,  self.position)
        
        #return self.finalsurf
        # make 
    