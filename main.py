import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# CONFIG
pyautogui.PAUSE = 0.3

URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CSV_PATH = "produtos.csv"

EMAIL = "email@gmail.com"
SENHA = "minhasenha"

# COORDENADAS
COORDENADAS = {
    "email": (685, 451),
    "senha": (685, 495),
    "btn_login": (955, 638),
    "primeiro_campo": (653, 294),  # campo "codigo"

    # Se precisar clicar no botão enviar, informe aqui. Se usar Enter, deixe como None.
    "btn_enviar": None
}


# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write(URL)
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(COORDENADAS["email"])
# escrever o seu email
pyautogui.write(EMAIL)
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write(SENHA)
pyautogui.click(COORDENADAS["btn_login"]) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv(CSV_PATH)

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(COORDENADAS["primeiro_campo"])
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim