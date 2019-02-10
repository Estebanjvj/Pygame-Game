#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 23:08:42 2018

@author: zaoryliht-kun
"""
import pygame, sys
from pygame.locals import *
from Yocho import MainSprite
from SunSprite import SunSprite
import time
import random

class TheGame:
    #window = None
    #clock = None
    
    def __init__(self, fondo, caption, fps):
        #stage
        pygame.init()
        self.window = pygame.display.set_mode([1000, 500])
        self.fondo = self.imagen(fondo).convert()
        self.fondo = pygame.transform.scale(self.fondo,(1000,600))
        self.lastbackground = pygame.transform.scale(self.fondo,(1000,600))
        pygame.display.set_caption(caption)
        self.fps = fps
        self.font = pygame.font.SysFont('Consolas', 30)
        self.best = 0
        self.nivel = 1
        self.juego = True
        self.mensaje = "Bienvenido"
        self.inicializar()
        
    def inicializar(self):
        #time
        self.clock = pygame.time.Clock()
        self.tick = 0
        #sun sprite
        self.sunsprite = SunSprite('img/sunfome2.png',True, 0, 6, 45, 45, 500, 280)
        self.sunsprite2 = SunSprite('img/sunfome2.png',True, 0, 6, 45, 45, 400, 280)
        self.sunsprite3 = SunSprite('img/sunfome2.png',True, 0, 6, 45, 45, 700, 280)
        self.sunsprite4 = SunSprite('img/sunfome2.png',True, 0, 6, 45, 45, 300, 280)
        self.sunsprite5 = SunSprite('img/sunfome2.png',True, 0, 6, 45, 45, 900, 280)
        #the main sprite
        self.powerup = MainSprite('img/yoshi_todos.gif',True, 0, 5, 32*2, 37*2)
        self.powermove = MainSprite('img/yoshi_walk.gif',True, 0, 10, 32*2, 37*2)
        self.powerup_jump = pygame.transform.scale2x(self.imagen('img/yoshi_todos.gif',True))
        self.powerup_up = pygame.Rect(10,100,60,80)
        self.powerup_in = pygame.Rect(70,100,60,80)
        self.powerup_down = pygame.Rect(118,100,80,80)
        #default settings for sprites
        self.yoshi_x = 40
        self.yoshi_y = 350
        #self.sunsprite.x = 500
        #self.sunsprite.y = 150
        self.yoshi_default_y = 350
        #default settigs to moving        
        self.moving = False
        self.salto = False
        self.bajada = False
        
    def defineCoordenadas(self, x,y, sunsprite):
        direccion = sunsprite.direccion
        if(abs(x-self.yoshi_x)<50):
            if(y>self.yoshi_y and self.yoshi_default_y == self.yoshi_y):
                sunsprite.setAten(False)
            if(x-self.yoshi_x>0):
                direccion = 0
            else:
                direccion = 6
        else:
            if(sunsprite.concurrencia==40):
                direccion = random.randint(0,799)
                direccion = int(direccion/100)            
                sunsprite.concurrencia = 0
                sunsprite.direccion = direccion
            else:
                sunsprite.concurrencia += 1
            
        if(direccion==0):
            #print("abajo, izquierda")
            x = x - 5
            y = y + 5
        elif(direccion==1):
            #print(" ----, izquierda")
            x = x - 5
            #y = y
        elif(direccion==2):
            #print("arriba, izquierda")
            x = x - 5
            y = y - 5
        elif(direccion==3):
            #print("arriba, ---------")
            #x = x
            y = y - 5
        elif(direccion==4):
            #print("arriba, derecha ")
            x = x + 5
            y = y - 5
        elif(direccion==5):
            #print("------, derecha")
            x = x + 5
            #y = y
        elif(direccion==6):
            #print("abajo , derecha")
            x = x + 5
            y = y + 5
        else:#direccion==7):
            #print("abajo, --------")
            #x = x
            y = y + 5
        if(x>960):
            sunsprite.x = x-10
            sunsprite.y = y
            sunsprite.update(self.window, x, y)
            sunsprite.concurrencia = 40
        elif(y<10):
            sunsprite.x = x
            sunsprite.y = y+10
            sunsprite.update(self.window, x, y)
            sunsprite.concurrencia = 40
        elif(y>460):
            sunsprite.x = x
            sunsprite.y = y-10
            sunsprite.update(self.window, x, y)
            sunsprite.concurrencia = 40
        elif(x<10):
            sunsprite.x = x+10
            sunsprite.y = y
            sunsprite.update(self.window, x, y)
            sunsprite.concurrencia = 40
        else:
            sunsprite.update(self.window, x, y)
            sunsprite.x = x
            sunsprite.y = y
        if(abs(x-self.yoshi_x)<25 and abs(y-self.yoshi_y)<25):
            pygame.mixer.music.stop()
            #pygame.image.save(self.lastbackground, "img/lastScreen.jpg")
            #self.lastbackground = pygame.Surface.get_rect(0,0,1000,500)
            self.juego = False
            self.mensaje = "Te han atrapado ;("
            last = (self.tick)
            if last>self.best:
                self.best = int(last)
            pygame.time.__init__('name')
            self.inicializar()
            self.main()
        elif(self.sunsprite.free is False and self.sunsprite2.free is False and self.sunsprite3.free is False and self.sunsprite4.free is False and self.sunsprite5.free is False):
            pygame.mixer.music.stop()
            #pygame.image.save(self.lastbackground, "img/lastScreen.jpg")
            #self.lastbackground = pygame.Surface.get_rect(0,0,1000,500)
            self.juego = False
            self.mensaje = "Te los has comido a todos!! ;)"
            last = self.nivel*(500-int(self.tick))
            self.nivel += 1
            if last>self.best:
                self.best = int(last)
            self.main()
        
    def draw(self):
        #backgroudn
        self.window.blit(self.fondo,(0,0))
        #para el no principal
        self.defineCoordenadas(self.sunsprite.x, self.sunsprite.y, self.sunsprite)
        self.defineCoordenadas(self.sunsprite2.x, self.sunsprite2.y, self.sunsprite2)
        self.defineCoordenadas(self.sunsprite3.x, self.sunsprite3.y, self.sunsprite3)
        self.defineCoordenadas(self.sunsprite4.x, self.sunsprite4.y, self.sunsprite4)
        self.defineCoordenadas(self.sunsprite5.x, self.sunsprite5.y, self.sunsprite5)
        
        self.sunsprite.setAten(True)
        self.sunsprite2.setAten(True)
        self.sunsprite3.setAten(True)
        self.sunsprite4.setAten(True)
        self.sunsprite5.setAten(True)
        #para el principal
        if self.salto:
            #maximo
            if self.yoshi_y<=250:
                self.window.blit(pygame.transform.flip(self.powerup_jump.subsurface(self.powerup_in),self.powerup.invX,self.powerup.invY), (self.yoshi_x, self.yoshi_y))
                self.bajada = True
            #hacia arriba
            if not self.bajada:
                self.yoshi_y -=14
                self.window.blit(pygame.transform.flip(self.powerup_jump.subsurface(self.powerup_up),self.powerup.invX,self.powerup.invY), (self.yoshi_x, self.yoshi_y))
            #hacia abajo
            if self.bajada:
                self.yoshi_y +=14
                self.window.blit(pygame.transform.flip(self.powerup_jump.subsurface(self.powerup_down),self.powerup.invX,self.powerup.invY), (self.yoshi_x, self.yoshi_y))
            #fin
            if self.yoshi_y==self.yoshi_default_y:
                self.bajada = False
                self.salto = False
                self.window.blit(pygame.transform.flip(self.powerup_jump.subsurface(self.powerup_down),self.powerup.invX,self.powerup.invY), (self.yoshi_x, self.yoshi_y))
        elif not self.moving:
            self.powerup.update(self.window,self.yoshi_x,self.yoshi_y)
        else:
            self.powermove.update(self.window,self.yoshi_x,self.yoshi_y)
        #timer
        self.window.blit(self.font.render(str("{0:.2f}".format(self.tick)), True, (255, 255, 255)), (32, 28))
        self.window.blit(self.font.render(str("Nivel: "+str(self.nivel)), True, (255, 255, 255)), (900, 28))
        
    def update(self):
        self.teclado()
    
    def teclado(self):
        teclado = pygame.key.get_pressed()
        
        #saltos parabolicos
        if teclado[K_UP] and teclado[K_RIGHT]:
            self.salto = True
            if self.yoshi_x < 930:
                self.yoshi_x+=8
            self.moving = True
            self.powermove.invX = False
            self.powerup.invX = False
        elif teclado[K_UP] and teclado[K_LEFT]:
            self.salto = True
            if self.yoshi_x > 5:
                self.yoshi_x-=8
            self.moving = True
            self.powermove.invX = True
            self.powerup.invX = True
        #saltos simples
        elif teclado[K_RIGHT]:
            if self.yoshi_x < 930:
                self.yoshi_x+=8
            self.moving = True
            self.powermove.invX = False
            self.powerup.invX = False
        elif teclado[K_LEFT]:
            if self.yoshi_x > 5:
                self.yoshi_x-=8
            self.moving = True
            self.powermove.invX = True
            self.powerup.invX = True
        elif teclado[K_UP]:
            self.salto = True
        else:
            self.moving = False
        self.lastbackground = self.window.subsurface(0,0,1000,500)

    #gestor de imagenes
    def imagen(self, filename, transparent=False):
        image = None
        #try catch para lectura de archivos tipo imagen
        try:
            image = pygame.image.load(filename)
            image = image.convert()
            #si recibe true o si recibe algo como transparent
            if transparent:
                color = image.get_at((0,0))
                #hacer transparente lo blanco
                image.set_colorkey(color, pygame.RLEACCEL)
        except Exception as message:
            print ("Error -> ",str(message))
        return image
    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def main(self):
        startMenu = True
        pygame.mixer.init()
        pygame.mixer.music.load('img/Creditos finales.wav')
        pygame.mixer.music.play(-1)
        
        fondo = pygame.transform.smoothscale(self.lastbackground, (100,50))
        fondo = pygame.transform.smoothscale(fondo, (1000,500))
        
        r = 0
        suma = True
        
        while startMenu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    startMenu = False
                    pygame.mixer.music.stop()
                    self.juego = True
                    self.gameLoop()
                    break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.window.blit(fondo,(0,0))
            texto = pygame.font.Font('freesansbold.ttf',115)
            instrucciones = pygame.font.Font('freesansbold.ttf',18)
            mensaje = pygame.font.Font('freesansbold.ttf',50)
            record = pygame.font.Font('freesansbold.ttf',20)
            
            #TextSurf, TextRect = self.text_objects(str("Comesoles! "), texto, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            Text2Surf, Text2Rect = self.text_objects("Presiona cualquier tecla para comenzar", instrucciones, ( 211, 84, 0 ))
            Text3Surf, Text3Rect = self.text_objects(self.mensaje, mensaje, (255, 255, 255))
            if r == 254:
                suma = False
            if r == 1:
                suma = True
            if suma:
                r += 1
            else:
                r -= 1
            TextSurf, TextRect = self.text_objects(str("Comesoles! "), texto, (r, r, 0))
            Text4Surf, Text4Rect = self.text_objects("Mejor puntuación: "+str(self.best), record, ( 110, 44, 0 ))
            
            TextRect.center = (500,250)
            Text2Rect.center = (500,325)
            Text3Rect.center = (500,125)
            Text4Rect.center = (140,470)
            
            self.window.blit(TextSurf, TextRect)
            self.window.blit(Text2Surf, Text2Rect)
            self.window.blit(Text3Surf, Text3Rect)
            self.window.blit(Text4Surf, Text4Rect)
            pygame.display.update()
        #self.gameLoop()
        
    def gameLoop(self):
        self.inicializar()
        pygame.mixer.init()
        pygame.mixer.music.load('img/Fail Flute Mission Impossible Themesong.wav')
        pygame.mixer.music.play(-1)
        
        while self.juego:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(int(self.fps))
            self.tick += (self.clock.get_time()/1000)

if __name__ == '__main__':
    g = TheGame("img/background-up.jpg","COMESOLES", 25)
    g.main()