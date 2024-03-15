import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

#tela
largura = 960
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Frog")

#utilidades
preto = (0, 0, 0)
relogio = pygame.time.Clock() #Variável usada para delimitar frames por segundo: carregamento de imagem

#classe para sprites
class Sprites(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [] #lista local de imagens
        self.sprites.append(pygame.image.load("./Sprites/attack_1.png")) #adicionando imagens na lista com o pygame.image.load()
        self.sprites.append(pygame.image.load("./Sprites/attack_2.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_3.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_4.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_5.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_6.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_7.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_8.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_9.png"))
        self.sprites.append(pygame.image.load("./Sprites/attack_10.png"))
        
        self.atual = 0 
        self.image = self.sprites[self.atual] #Propriedade image pertence à classe Sprite do próprio pygame, ela é responsável por armazenar as imagens, estamos acessando nossa lista local de imagens com nosso contador local
        self.image = pygame.transform.scale(self.image, (128 * 6, 64 * 6)) #Aumentando o tamanho da imagem proporcionalmente

        self.rect = self.image.get_rect() #Armazenando rect da imagem
        self.rect.topleft = 0, largura / 2 - 64 * 3 #Centralizando no eixo da altura e encostando no canto esquero da largura

        self.animar = False #Inicando uma variável de controle de animação
    
    def update(self):
        if self.animar == True:
            self.atual += 0.10
            if self.atual >= len(self.sprites): #verificando se há imagem na lista correspondente à variável contadora
                self.atual = 0
                self.animar = False #animação terminou
            self.image = self.sprites[int(self.atual)] #atualizando imagem atual
            self.image = pygame.transform.scale(self.image, (128 * 6, 64 * 6)) #Aumentando o tamanho da imagem proporcionalmente

    def atacar(self):
        self.animar = True #permitindo animação quando acontecer o update


#objeto sprite e utilização do grupo de sprites do pygame para exibição da imagem no loop principal
all_sprites = pygame.sprite.Group() #Variável local que se torna um grupo de sprites
sapo = Sprites()
all_sprites.add(sapo)

#loop principal
while True:
    #usando utilidades
    tela.fill(preto)
    relogio.tick(120)

    #ações do usuário
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN: 
            sapo.atacar() #animação
        
    #desenhando e atualizando sprites - movimento
    all_sprites.draw(tela)
    all_sprites.update() 

    #atualizando "tela"
    pygame.display.flip()