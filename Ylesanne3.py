

# Impordin vajaliku mooduli
import pygame

# Pygame mooduli ellukutsumine
pygame.init()
screen = pygame.display.set_mode((640, 480))  # ekraani suurus
screen.fill((154, 255, 155))  # ekraani taustavärv, erklroheline
pygame.display.set_caption("Harjutamine")  # ekraani pealkiri

# Muudetavad parameetrid
read = 100
veerud = 100
suurus = 20
joone_varv = (255, 0, 0)  # joone värv, punane

def joonista_ruudud(): # funktsioon, millega ruudud joonistan
    for i in range(read):
        for j in range(veerud):  #tsükkel, mis leiab iga kord ruudule uue x ja y koordinaadi
            pygame.draw.rect(screen, joone_varv, (j * suurus, i * suurus, suurus, suurus), 1)

running = True  # Hoiab ekraani avatuna kuni kasutaja selle sulgeb
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    joonista_ruudud()  #kutsun ellu funktsiooni, mis joonistab ruudud

    # Kuvan ekraanil
    pygame.display.flip()

# Sulgeb mängu, kui tsükkel lõppeb
pygame.quit()
