import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode((600, 480))
print('Setup Finish')

print('Loop start')
while True:
    # Check for all events (precisa ficar indentado aqui dentro)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
