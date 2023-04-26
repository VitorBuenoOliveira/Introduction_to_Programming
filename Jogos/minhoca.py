import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Definição das cores utilizadas no jogo
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Criação da janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Minhoca')

# Definição do tamanho e da posição inicial da minhoca
WORM_SIZE = 10
worm_x = SCREEN_WIDTH // 2
worm_y = SCREEN_HEIGHT // 2
worm_body = [(worm_x, worm_y)]

# Definição da direção inicial da minhoca
worm_direction = 'RIGHT'

# Definição da velocidade da minhoca
WORM_SPEED = 2

# Definição do tamanho e da posição da maçã
APPLE_SIZE = 10
apple_x = random.randint(APPLE_SIZE, SCREEN_WIDTH - APPLE_SIZE)
apple_y = random.randint(APPLE_SIZE, SCREEN_HEIGHT - APPLE_SIZE)

# Definição da fonte utilizada para o texto na tela
FONT = pygame.font.Font(None, 36)

# Definição da pontuação inicial
score = 0

# Loop principal do jogo
running = True
while running:
    # Processamento dos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and worm_direction != 'DOWN':
                worm_direction = 'UP'
            elif event.key == pygame.K_DOWN and worm_direction != 'UP':
                worm_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and worm_direction != 'RIGHT':
                worm_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and worm_direction != 'LEFT':
                worm_direction = 'RIGHT'
    pygame.time.delay(10)
    # Movimentação da minhoca
    if worm_direction == 'UP':
        worm_y -= WORM_SPEED
    elif worm_direction == 'DOWN':
        worm_y += WORM_SPEED
    elif worm_direction == 'LEFT':
        worm_x -= WORM_SPEED
    elif worm_direction == 'RIGHT':
        worm_x += WORM_SPEED

    # Verificação de colisão com as bordas da tela
    if worm_x < 0 or worm_x > SCREEN_WIDTH - WORM_SIZE or worm_y < 0 or worm_y > SCREEN_HEIGHT - WORM_SIZE:
        running = False

    # Adição do novo segmento da minhoca à sua lista de segmentos
    worm_body.insert(0, (worm_x, worm_y))

    # Verificação de colisão com a maçã
    if abs(worm_x - apple_x) < WORM_SIZE and abs(worm_y - apple_y) < WORM_SIZE:
        apple_x = random.randint(APPLE_SIZE, SCREEN_WIDTH - APPLE_SIZE)
        apple_y = random.randint(APPLE_SIZE, SCREEN_HEIGHT - APPLE_SIZE)
        score += 1
    else:
        # Remoção do último segmento da minhoca, se ela não comeu a maçã
        worm_body.pop()

    # Desenho da tela
    screen.fill(BLACK)
   
    # Desenho da maçã
    pygame.draw.rect(screen, RED, (apple_x, apple_y, APPLE_SIZE, APPLE_SIZE))

    # Desenho da minhoca
    for segment in worm_body:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], WORM_SIZE, WORM_SIZE))

    # Verificação de colisão com o próprio corpo da minhoca
    for i in range(1, len(worm_body)):
        if worm_body[0] == worm_body[i]:
            running = False

    # Desenho da pontuação na tela
    score_text = FONT.render('Pontuação: {}'.format(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Atualização da tela
    pygame.display.update()
# Pausa para exibir a tela por um curto período de tempo antes de fechar
pygame.time.wait(100)
# Encerramento do Pygame
pygame.quit()
