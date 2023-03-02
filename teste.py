import pygame

# Inicializar o Pygame
pygame.init()

# Definir o tamanho da tela
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Definir o título da janela
pygame.display.set_caption("Jogo")

# Definir a cor de fundo da tela
bg_color = (255, 255, 255)

# Criar um objeto Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height / 2 - self.rect.height / 2
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Manter o personagem dentro da janela
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                self.speed_x = 5
            elif event.key == pygame.K_UP:
                self.speed_y = -5
            elif event.key == pygame.K_DOWN:
                self.speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.speed_x < 0:
                self.speed_x = 0
            elif event.key == pygame.K_RIGHT and self.speed_x > 0:
                self.speed_x = 0
            elif event.key == pygame.K_UP and self.speed_y < 0:
                self.speed_y = 0
            elif event.key == pygame.K_DOWN and self.speed_y > 0:
                self.speed_y = 0

player = Player()

# Definir o loop principal do jogo
running = True
clock = pygame.time.Clock()
while running:
    # Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            player.handle_event(event)

    # Atualizar o jogo
    player.update()

    # Desenhar a tela
    screen.fill(bg_color)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

    # Esperar por 1/60 de segundo
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
