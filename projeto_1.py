'''
Bot de curtidas e comentários no Instagram com PyAutoGUI

- Vamos criar um bot que define qual página quer seguir, verifica se a postagem mais atual ainda não foi curtida pelo bot. Caso uma nova postagem tenha sido feita, ele deve entrar nessa postagem ,curtir e comentar algo nela.


Sequencia de Passos
'''
import webbrowser
import pyautogui
from time import sleep

while True:
    # 1º Passo - Abrir o Instagram
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(2)

    # 2º Passo - Entrar na conta 
    pyautogui.moveTo(682,575,duration=2)
    sleep(1)
    pyautogui.click()
    sleep(10)

    # 3º Passo - Ir ate a barra de pesquisa e pequisar 'Nike'
    pyautogui.moveTo(36,267,duration=2)
    sleep(1)
    pyautogui.click()
    sleep(2)
    pyautogui.moveTo(207,200,duration=1)
    sleep(1)
    pyautogui.click()
    sleep(1)
    pyautogui.typewrite('Nike')
    sleep(1)

    # 4º Passo - Entrar na página
    pyautogui.move(0,50,duration=1)
    sleep(1)
    pyautogui.click()
    sleep(10)

    # 5º Passo - Clicar na postagem mais recente
    pyautogui.click(219,750,duration=2)
    sleep(5)

    # 6º Passo - Verificar se postagem já foi curtida ou não
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)

    # 7º Passo - Se já tiver curtido, fazer nada e pausar o bot por 24horas
    if coracao is not None:
        sleep(86400)

    # 8º Passo - Caso contrário, curtir a foto
    elif coracao == None:
        pyautogui.click(coracao[0],coracao[1],duration=2)
        sleep(5)
        # 9º Passo - Caso contrário, comentar na foto
        pyautogui.click(542,790,duration=2)
        sleep(3)
        pyautogui.typewrite('Let them cook!')
        sleep(5)
        pyautogui.click(833,892,duration=1)
        sleep(1)

    # 10º Passo - Sair da postagem
    pyautogui.click(912,111,duration=1)
    sleep(2)
    # 11º Passo - Sair do perfil
    pyautogui.click(35,984,duration=1)
    sleep(1)
    pyautogui.move(70,0,duration=1)
    sleep(2)
    pyautogui.click()
    sleep(10)
    # 12º Passo - Fechar a aba apos o logout
    pyautogui.hotkey('ctrl','w')

    # 13º Passo - Pausar por 24 horas e ao final desse período, rodar novamente
    sleep(86400)




