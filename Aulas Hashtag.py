import pyautogui
import pyperclip
import time
pyautogui.PAUSE = 1
# Passo 0: abrir chorme em nova guia:
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=967, y=562)
# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("Lélé é icá. EU NÃO GÓ!")
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(5)
# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=516, y=316, clicks=3)
time.sleep(2)
# Passo 3: Fazer o download do relatório
pyautogui.click(x=510, y=378)
pyautogui.click(x=1663, y=193)
pyautogui.click(x=1474, y=741)
time.sleep(5)
### Vamos agora ler o arquivo baixado para pegar os indicadores
# Passo 4: Calcular os indicadores
import pandas as pd
tabela = pd.read_excel(r"C:\\Users\Ayrto\Downloads\Vendas - Dez.xlsx(3)")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
### Vamos agora enviar um e-mail pelo gmail
# Passo 5: Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=109, y=183)

pyautogui.write("pythonimpressionador+diretoria@gmail.com")
pyautogui.press("tab") # seleciona o email
# escreve outro email
# tab
# escreve outro email
# tab
pyautogui.press("tab") # pula pro campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v") # escrever o assunto
pyautogui.press("tab") #pular pro corpo do email
texto = f"Prezados, bom dia\nO faturamento de ontem foi de: R${faturamento:}\nA quantidade de produtos foi de: {quantidade}"
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
# clicar no botão enviar
# apertar Ctrl Enter
pyautogui.hotkey("ctrl", "enter")

#### Use esse código para descobrir qual a posição de um item que queira clicar
"- Lembre-se: a posição na sua tela é diferente da posição na minha tela"
'''
time.sleep(5)
pyautogui.position()'''


### AULA 2:
'''https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs'''