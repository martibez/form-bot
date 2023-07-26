import time, pyautogui, pandas as pd

# Passo 1: Entrar no formulário
pyautogui.PAUSE = 0.3
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep (1)
pyautogui.hotkey('win','up')
# entrar no link
pyautogui.write("https://forms.gle/TJZYuSLgLVYyKtReA")
pyautogui.press("enter")
time.sleep (5)

# Passo 2; Importar a base de produtos para cadastrar
tabela = pd.read_csv("./form-bot/produtos.csv")

# Passo 3: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo codigo
    pyautogui.click(x=781, y=338)
    # pegar da tabela o valor do campo desejado
    codigo = tabela.loc[linha,"codigo"]
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not pd.isna (tabela.loc[linha,"obs"]):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    # salvar formulário
    pyautogui.click(x=781, y=395)
    time.sleep(2)
    # cadastrar novo item
    pyautogui.click(x=728, y=228)
    time.sleep(3)
