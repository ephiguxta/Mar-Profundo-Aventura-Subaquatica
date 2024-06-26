import pygame

# Inicializando pygame
pygame.init()

# Definindo as dimensões da janela
LARGURA_JANELA = 500
ALTURA_JANELA = 400

# Carregando as imagens do cenário
imagem_cenario1 = pygame.image.load('Imagens/cenario1.png')
imagem_cenario2 = pygame.image.load('Imagens/cenario2.png')
imagem_cenario3 = pygame.image.load('Imagens/cenario3.png')
imagem_cenario4 = pygame.image.load('Imagens/cenario4.png')

# Carregando as imagens do peixe
imagemPeixe = pygame.image.load('Imagens/peixe.png')

# Ajustando o tamanho das imagens do cenário
imagem_cenario1 = pygame.transform.scale(imagem_cenario1, (LARGURA_JANELA, ALTURA_JANELA))
imagem_cenario2 = pygame.transform.scale(imagem_cenario2, (LARGURA_JANELA, ALTURA_JANELA))
imagem_cenario3 = pygame.transform.scale(imagem_cenario3, (LARGURA_JANELA, ALTURA_JANELA))
imagem_cenario4 = pygame.transform.scale(imagem_cenario4, (LARGURA_JANELA, ALTURA_JANELA))

# Definindo algumas constantes
LARGURAPEIXE = imagemPeixe.get_width()
ALTURAPEIXE = imagemPeixe.get_height()
VEL = 6
ITERACOES = 30
# Definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda-100:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita+120:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > borda_superior-117:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior+105:
        jogador['objRect'].y += jogador['vel']
    #Tive que colocar esses valores somando e subtraindo pq o tamanho do peixe bagunça os limites da tela

# Definindo a função moverPeixe(), que registra a posição do peixe
def moverPeixe(peixe):
    peixe['objRect'].x += peixe['vel']

relogio = pygame.time.Clock()

# Criando a janela
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Imagem e Som')

# Posicionando os cenários
posicao_cenario1 = (0, 0)
posicao_cenario2 = (LARGURA_JANELA, 0)
posicao_cenario3 = (2 * LARGURA_JANELA, 0)
posicao_cenario4 = (3 * LARGURA_JANELA, 0)

# Velocidade do movimento do cenário
velocidade_cenario = 1

# Criando jogador
jogador = {'objRect': pygame.Rect(10, 45, LARGURAPEIXE, ALTURAPEIXE), 'imagem': imagemPeixe, 'vel': VEL}

# Definindo o dicionário que guardará as direções pressionadas
teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}

# Inicializando variavel de controle do jogo
deve_continuar = True

# Variável de controle para pausar o jogo
pausado = False

# Carregando e reproduzindo a música de fundo em loop
pygame.mixer.music.load('Sons/musicadefundo.wav')
pygame.mixer.music.play(-1)  # coloca -1 para reprodução ficar em looping

# É a função para mover o cenario do Jogo
def mover_cenario():
    global posicao_cenario1, posicao_cenario2, posicao_cenario3, posicao_cenario4 #tenho que declarar como globar pq vou mexer nas posicoes e precisa salvar
    posicao_cenario1 = (posicao_cenario1[0] - velocidade_cenario, posicao_cenario1[1]) # posicao 0 significa que esta em x e eu tiro a velocidade, ou seja vou diminuindo os pixels para dar sensação que esta andando enquanto na posicao 1 que é o y, ele está parado
    posicao_cenario2 = (posicao_cenario2[0] - velocidade_cenario, posicao_cenario2[1])
    posicao_cenario3 = (posicao_cenario3[0] - velocidade_cenario, posicao_cenario3[1])
    posicao_cenario4 = (posicao_cenario4[0] - velocidade_cenario, posicao_cenario4[1])

    # Aqui ele faz as comparações, ou seja, se a primeira imagem sair completamente da tela que é a soma da posicao mais o cenario, ele coloca depois direita do quarto cenário para ficar em looping
    if posicao_cenario1[0] + LARGURA_JANELA < 0:
        posicao_cenario1 = (posicao_cenario4[0] + LARGURA_JANELA, posicao_cenario1[1])

    # Se a segunda imagem sair completamente da tela, mova-a para a direita da primeira imagem
    if posicao_cenario2[0] + LARGURA_JANELA < 0:
        posicao_cenario2 = (posicao_cenario1[0] + LARGURA_JANELA, posicao_cenario2[1])

    # Se a terceira imagem sair completamente da tela, mova-a para a direita da segunda imagem
    if posicao_cenario3[0] + LARGURA_JANELA < 0:
        posicao_cenario3 = (posicao_cenario2[0] + LARGURA_JANELA, posicao_cenario3[1])

    # Se a quarta imagem sair completamente da tela, mova-a para a direita da terceira imagem
    if posicao_cenario4[0] + LARGURA_JANELA < 0:
        posicao_cenario4 = (posicao_cenario3[0] + LARGURA_JANELA, posicao_cenario4[1])

# Loop do jogo
while deve_continuar:
    # Checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        # Quando uma tecla é pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True
            # Pausa do jogo quando a tecla "P" é pressionada
            if evento.key == pygame.K_p:
                pausado = not pausado
                pygame.mixer.music.pause() if pausado else pygame.mixer.music.unpause()
        # Quando uma tecla é solta
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False

    if not pausado:  # Verifica se o jogo não está pausado
        # Movendo o cenário
        mover_cenario()

        # Desenhando o cenário
        janela.blit(imagem_cenario1, posicao_cenario1)
        janela.blit(imagem_cenario2, posicao_cenario2)
        janela.blit(imagem_cenario3, posicao_cenario3)
        janela.blit(imagem_cenario4, posicao_cenario4)

        # Movendo jogador
        moverJogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))
        # Desenhando jogador
        janela.blit(jogador['imagem'], jogador['objRect'])

    # Atualizando a janela
    pygame.display.update()
    relogio.tick(40)

# Encerrando a reprodução da música e os módulos do Pygame
pygame.mixer.music.stop()
pygame.quit()
