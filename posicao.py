import time
from Quartz import CGEventCreate, CGEventGetLocation

# Loop infinito para continuar monitorando a posição do mouse
while True:
    # Cria um evento de captura do mouse
    event = CGEventCreate(None)
    
    # Obtém e imprime a posição atual do mouse
    mouse_position = CGEventGetLocation(event)
    print(mouse_position.x, mouse_position.y)
    
    # Aguarda 2 segundos antes de obter a próxima posição do mouse
    time.sleep(2)


    # posicao 1406.11328125 864.73046875