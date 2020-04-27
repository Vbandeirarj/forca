import pygame, random


try:
    pygame.init()
    pygame.font.init()
except:
    print('Pygame não pode ser inicializado corretamente')

largura = 800
altura = 600
branco = (202, 81, 0)
marrom = (32, 13, 0)
tamanho_a=108
tamanho_b=800
pos_x = 0
pos_y = 492

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Forca')
font = pygame.font.Font('FFF_Tusj.ttf', 35)
texto = font.render("Forca" , True, (0, 0, 0))
dica = font.render("DICA: ", True, (255,255,255))
iforca = pygame.image.load('forca.png')
iforca = pygame.transform.scale(iforca, (300, 500))
b_start = pygame.image.load('start.png')
b_start = pygame.transform.scale(b_start, (90,90))

lines = open('palavras.txt').read().split()
myline = random.choice(lines)
t = []
for letra in myline:
    t.append('_')

tracos = font.render(str(t), True, (0, 0, 0))
sorteio = font.render(myline, True, (0,0,0,))

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
            print(a)
            if event.unicode.isalpha():
                for i in myline:
                   if i == a:
                       print('Correto')



    fundo.blit(iforca, (0, 0))
    fundo.blit(b_start, (700,10))
    fundo.blit(texto, (100,10))
    fundo.blit(sorteio, (400, 300))
    fundo.blit(tracos, (350, 400))
    pygame.draw.rect(fundo, marrom, [pos_x, pos_y, tamanho_b, tamanho_a])
    fundo.blit(dica, (30, 500))
    pygame.display.update()

pygame.quit()