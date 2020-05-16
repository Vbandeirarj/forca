import pygame, random, sys
import time



try:
    pygame.init()
    pygame.font.init()
except:
    print('Pygame não pode ser inicializado corretamente')

largura = 1280
altura = 700
branco = (202, 81, 0)
marrom = (32, 13, 0)
tamanho_a=90
tamanho_b=1280
pos_x = 0
pos_y = 610






fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Forca')
font = pygame.font.Font('FFF_Tusj.ttf', 35)
texto = font.render("Forca" , True, (0, 0, 0))
dica = font.render("DICA: ", True, (255,255,255))
enforcado= font.render("Enforcado" , True, (0, 0, 0))
iforca = pygame.image.load('forca.png')

#iforca = pygame.transform.scale(iforca, (300, 500))
b_start = pygame.image.load('start.png')
b_start = pygame.transform.scale(b_start, (90,90))
x=str
teste=[]
dicas=[]
dicas2=[]
dicas3=[]
letra=''
a=' '

#aa=font.render(str(a), True, (0, 0, 0))

erro=0

lines = open('palavras.txt').read().split()
lines2= open('dicas.txt').read().split()


myline = random.choice(lines)
for linha in lines:
    if linha == myline:
        teste = linha
        print(teste)


        with open('dicas.txt') as f:
            for l in f:  # percorrer linhas e enumera-las a partir de 1
                if teste in l:  # ver se palavra esta na linha
                    dicas = l
                    dicas2=dicas.split('=')
                    dicas3=dicas2[1]
                    print(dicas3)

t = []
for letra in myline:
    t.append('_')

aa=font.render(str(t), True, (0, 0, 0))
tracos = font.render(str(a), True, (0, 0, 0))
sorteio = font.render(myline, True, (0, 0, 0,))
dicas = font.render(dicas3, True,(255,255,255))
direita=500

sair = True
pygame.mixer.music.load('suspense.mp3')
pygame.mixer.music.play()

while sair:
    fundo.fill(branco)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            a = event.key
            a = chr(a)
            print(a)
            for n, letra in enumerate(myline):

                if myline[n] == a.upper():
                    t[n] = myline[n]
                    print('possui')
                    print('teste:',t)
                    print(direita)
                    aa = font.render(str(t), True, (0, 0, 0))





            if a.upper() not in myline:
                print('Não possui')
                erro = erro + 1
                if erro == 1:
                    iforca = pygame.image.load('forca1.png')
                if erro == 2:
                    iforca = pygame.image.load('forca2.png')
                if erro == 3:
                    iforca = pygame.image.load('forca3.png')
                if erro == 4:
                    iforca = pygame.image.load('forca4.png')
                if erro == 5:
                    iforca = pygame.image.load('forca5.png')
                if erro == 6:
                    iforca = pygame.image.load('forca6.png')
                    fundo.blit(iforca, (0, 0))
                    continuar = font.render("Deseja continuar S/N", True, (0, 0, 0))
                    fundo.blit(continuar, (500, 600))
                    pygame.display.update()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            print('não continuar')
                            pygame.quit()
                        if a.upper() == 'S':
                            break
                    time.sleep(5)






    fundo.blit(iforca, (0, 0))
    fundo.blit(aa, (500, 550))
    fundo.blit(b_start, (700,10))
    fundo.blit(texto, (120,20))
    fundo.blit(tracos, (500, 550))
    pygame.draw.rect(fundo, marrom, [pos_x, pos_y, tamanho_b, tamanho_a])
    fundo.blit(dica, (30, 630))
    fundo.blit(dicas, (150, 630))

    pygame.display.update()

pygame.quit()