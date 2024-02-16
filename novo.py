import openpyxl
import time
import pywhatkit
from datetime import datetime
import pyautogui
from time import sleep

# Selecionar planilha
planilhaAviso = openpyxl.load_workbook('avisos.xlsx')

# Selecioando páginas da planilha
pagina = planilhaAviso['Planilha1']

# Tempo de espera até o WhatsApp Web ser carregado (em segundos)
tempo_espera_whatsapp = 50

# Inicializa uma string vazia para armazenar todas as mensagens
todas_mensagens = ""

# Ler as informações da planilha por linhas (a partir da linha 2)
# indice 0 = aula 
# indice 1 = dia
# indice 2 = aviso
for linhas in pagina.iter_rows(min_row=2):
    aula = linhas[0].value
    dia = linhas[1].value
    aviso = linhas[2].value

    # Não mostra o campo que está vazio (None)
    if aula is not None or dia is not None or aviso is not None:
        mensagem = ""
        if aula is not None:
            mensagem += f"Aula: {aula}\n"
        if dia is not None:
            mensagem += f"Dia: {dia}\n"
        if aviso is not None:
            mensagem += f"Aviso: {aviso}\n"

        # Adiciona a mensagem atual à string de todas as mensagens
        todas_mensagens += mensagem + "\n"  # Adiciona uma quebra de linha entre as mensagens

# Aguarda até que todas as mensagens tenham sido coletadas
time.sleep(tempo_espera_whatsapp)

# Número de telefone para o qual deseja enviar a mensagem (substitua pelo número desejado)
numero_telefone = "numero"

# Enviar todas as mensagens de uma vez
pywhatkit.sendwhatmsg(numero_telefone, todas_mensagens, datetime.now().hour, datetime.now().minute + 1)

time.sleep(5)



# parte do envio 

# Define a posição inicial do mouse
posicao_inicial = pyautogui.position()

# Define a posição final desejada
posicao_final = (1406.11328125, 864.73046875)

# Verifica as coordenadas antes do movimento do mouse
print("Coordenadas do mouse antes do movimento:", pyautogui.position())

# Move o mouse para a posição final com duração especificada
pyautogui.moveTo(posicao_final[0], posicao_final[1], duration=0.5)

# Verifica as coordenadas após o movimento do mouse
print("Coordenadas do mouse após o movimento:", pyautogui.position())

# Realiza o clique na posição final
pyautogui.click()

# Move o mouse de volta para a posição inicial (opcional)
pyautogui.moveTo(posicao_inicial[0], posicao_inicial[1], duration=0.5)