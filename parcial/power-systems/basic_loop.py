# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

# Así es como inicia una triste historia sobre un estudiante que perdió 500 líneas
# de código por no respaldar y por descuidado...
# Érase una vez un examen que se debía entregar un domingo, pero debido a la
# complejidad de la resolución, pasó a entregarse el próximo domingo.
# Un valiente personaje y su equipo decidieron iniciar con el recorrido con varias
# semanas de antelación. El código para resolver el problema estuvo listo con tres
# días de anticipación a la fecha final de entrega.
# Pero un día... El personaje portador del código de respaldo lo destruyó por
# accidente la noche trasanterior al día de entrega.
# Una de las más grandes tragedias en las vidas de estos valientes.
# Sin embargo, no decidieron darse por vencido. Todo el empeño y dedicación, la
# noche sin dormir y el empeño adicional por obtener el mejor producto no se
# quedarían en el olvido. Y así es como surgió este programa...
