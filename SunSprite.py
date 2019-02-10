#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:29:32 2018

@author: zaoryliht-kun
"""
import pygame
import pyafai
from pygame.constants import RLEACCEL

class SunSprite(pygame.sprite.Sprite, pyafai.Agent):
    p = 0
    ida = True
    invX = False
    invY = False
        
    def __init__(self, path, transparent, current_frame, frames,frame_width, frame_heigth, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.imagen(path,transparent)
        self.rect = self.image.get_rect()
        self.current_frame = current_frame
        self.frames = frames
        self.frame_width = frame_width
        self.frame_height = frame_heigth
        self.p = 0
        self.moving = False
        self.direccion = 0
        self.concurrencia = 0
        self.x = x
        self.y = y
        self.free = True
        
    def update(self, window, x , y):
        if self.ida:
            if self.p < self.frames*2:
                self.p += 1
            else:
                self.ida = False
                self.p -=2
        else:
            if self.p > 0:
                self.p -=1
            else:
                self.ida = True
                self.p +=2
            
        for i in range(0,(self.frames)*2,2):
            if self.p == i:
                self.current_frame=i/2
            
        new_area = pygame.Rect((self.current_frame * (self.frame_width+(self.current_frame)), 0, (self.frame_width), self.frame_height))
        window.blit(pygame.transform.flip(self.image.subsurface(new_area),self.invX,self.invY), (x, y))
        
    def setAten(self, comido):
        self.free = comido
        
    def imagen(self, filename, transparent=False):
        #try catch para lectura de archivos tipo imagen
        try: image = pygame.image.load(filename)
        except Exception as message:
            print ("Error -> ",str(message))
        #except pygame.error, message:
        #    raise SystemExit, message
        image = image.convert()
        #si recibe true o si recibe algo como transparent
        if transparent:
            color = image.get_at((5,5))
            #hacer transparente lo blanco
            image.set_colorkey(color, RLEACCEL)
            return image
    '''
    def setMoving(self, moving):
        
        if not self.moving:
            self.path = "img/yoshi_todos.gif"
            self.current_frame = 0
            self.p=0
            self.frames = 5
        else:
            self.path = "img/yoshi_walk.gif"
            self.current_frame = 0
            self.p=0
            self.frames = 10
    '''