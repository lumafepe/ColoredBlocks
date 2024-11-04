import pygame
import sys
import random
import time
from collections import defaultdict
from preencher import agrupar_jogadores_por_cor

# Pool de cores expandido
pool_de_cores = [
    "vermelho", "azul", "verde", "amarelo", "roxo", "laranja", 
    "rosa", "marrom", "ciano"
]

# Gerar jogadores e blocos de cores de forma aleatória
def gerar_jogadores_aleatorios():
    num_jogadores = random.randint(3, 6)  # Número aleatório de jogadores entre 3 e 6
    cores_dos_jogadores = {}
    for i in range(1, num_jogadores + 1):
        nome_jogador = f"Jogador{i}"
        cores_do_jogador = random.sample(pool_de_cores, random.randint(3, 5))  # Cada jogador recebe de 3 a 5 cores
        cores_dos_jogadores[nome_jogador] = cores_do_jogador
    return cores_dos_jogadores

# Gerar jogadores e cores
cores_dos_jogadores = gerar_jogadores_aleatorios()

# Configuração do Pygame
pygame.init()

# Dimensões da janela
largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cores dos Jogadores")

# Definir fonte menor
fonte = pygame.font.Font(None, 24)

# Função lógica do jogo
def agrupar_c_j(cores_dos_jogadores):
    cor_para_jogadores = defaultdict(set)
    for j, cs in cores_dos_jogadores.items():
        for c in cs:
            cor_para_jogadores[c].add(j)
    return cor_para_jogadores

# Dicionário de cores para exibição no Pygame
dicionario_cores = {
    "vermelho": (255, 0, 0), "azul": (0, 0, 255), "verde": (0, 255, 0),
    "amarelo": (255, 255, 0), "roxo": (128, 0, 128), "laranja": (255, 165, 0),
    "rosa": (255, 192, 203), "marrom": (139, 69, 19), "ciano": (0, 255, 255)
}

# Função para exibir os jogadores e suas cores
def exibir_jogadores():
    posicao_x = 50  # Posição inicial X para os jogadores
    for jogador, cores in cores_dos_jogadores.items():
        # Calcular altura total dos blocos de cores para alinhar o nome do jogador na parte inferior
        altura_total_blocos = len(cores) * 40
        posicao_y_inicial = altura - altura_total_blocos - 50  # Posição Y inicial para alinhar no fundo

        # Exibir blocos de cores menores para cada jogador de forma vertical
        posicao_y = posicao_y_inicial
        for cor in cores:
            pygame.draw.rect(screen, dicionario_cores.get(cor, (0, 0, 0)), pygame.Rect(posicao_x, posicao_y, 30, 30))
            posicao_y += 40  # Mover para baixo para o próximo bloco
        
        # Exibir nome do jogador abaixo dos blocos de cores
        superficie_texto = fonte.render(jogador, True, (0, 0, 0))
        screen.blit(superficie_texto, (posicao_x, posicao_y + 5))
        
        # Mover para a direita para o próximo jogador
        posicao_x += 100

    pygame.display.flip()

# Função para exibir as cores e os jogadores que possuem cada cor
def exibir_cores_por_jogadores(y, f, texto):
    cor_para_jogadores = f(cores_dos_jogadores)
    
    posicao_x = 50  # Posição inicial X para as cores
    # Exibir texto esperado
    superficie_texto_esperado = fonte.render(texto, True, (0, 0, 0))
    screen.blit(superficie_texto_esperado, (posicao_x, y - 50))

    for cor, jogadores in cor_para_jogadores.items():
        # Exibir bloco de cor menor
        pygame.draw.rect(screen, dicionario_cores.get(cor, (0, 0, 0)), pygame.Rect(posicao_x, y, 30, 30))
        
        # Exibir nome da cor acima do bloco
        superficie_texto_cor = fonte.render(cor, True, (0, 0, 0))
        screen.blit(superficie_texto_cor, (posicao_x, y - 30))
        
        # Exibir nomes dos jogadores abaixo do bloco
        posicao_y = y + 40
        for jogador in jogadores:
            superficie_texto_jogador = fonte.render(jogador, True, (0, 0, 0))
            screen.blit(superficie_texto_jogador, (posicao_x, posicao_y))
            posicao_y += 20  # Mover para baixo para o próximo jogador
        
        # Mover para a direita para a próxima cor
        posicao_x += 100

    pygame.display.flip()

# Loop principal
executando = True
while executando:
    screen.fill((255, 255, 255))  # Fundo branco
    # Primeira exibição: jogadores e suas cores
    exibir_jogadores()
    time.sleep(5)
    screen.fill((255, 255, 255))  # Fundo branco
    # Segunda exibição: cores e os jogadores que as possuem
    exibir_cores_por_jogadores(70, agrupar_c_j, "Esperado:")
    exibir_cores_por_jogadores(270, agrupar_jogadores_por_cor, "Resposta:")
    
    time.sleep(30)
    
    # Loop de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

pygame.quit()
sys.exit()
