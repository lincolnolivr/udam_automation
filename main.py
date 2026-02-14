import os
import time
import pyautogui
import pyperclip
import pygetwindow as gw



# ============================================
# CONFIGURAÇÕES
# ============================================
pyautogui.FAILSAFE = True  # Move mouse pro canto superior esquerdo para abortar
pyautogui.PAUSE = 0.3  # Delay padrão entre ações do pyautogui


# ============================================
# FUNÇÕES DE JANELA
# ============================================
def ativar_janela(titulo: str) -> bool:
    """
    Ativa uma janela pelo título (ou parte dele).

    Args:
        titulo: Nome ou parte do nome da janela

    Returns:
        True se encontrou e ativou, False caso contrário
    """
    janelas = gw.getWindowsWithTitle(titulo)
    if janelas:
        janelas[0].activate()
        time.sleep(0.5)
        return True
    return False

def maximizar_janela(titulo: str) -> bool:
    """
    Maximiza uma janela pelo título.

    Args:
        titulo: Nome ou parte do nome da janela

    Returns:
        True se encontrou e maximizou, False caso contrário
    """
    janelas = gw.getWindowsWithTitle(titulo)
    if janelas:
        janelas[0].maximize()
        time.sleep(0.3)
        return True
    return False

def listar_janelas() -> list:
    """
    Lista todas as janelas abertas.

    Returns:
        Lista com títulos das janelas
    """
    return [w.title for w in gw.getAllWindows() if w.title]


# ============================================
# FUNÇÕES DE MOUSE
# ============================================
def clicar(x: int, y: int, duplo: bool = False):
    """
    Clica em uma posição específica da tela.

    Args:
        x: Coordenada X
        y: Coordenada Y
        duplo: Se True, faz duplo clique
    """
    if duplo:
        pyautogui.doubleClick(x, y)
    else:
        pyautogui.click(x, y)

def clicar_direito(x: int, y: int):
    """
    Clica com botão direito em uma posição.

    Args:
        x: Coordenada X
        y: Coordenada Y
    """
    pyautogui.rightClick(x, y)

def mover_mouse(x: int, y: int, duracao: float = 0.25):
    """
    Move o mouse para uma posição.

    Args:
        x: Coordenada X
        y: Coordenada Y
        duracao: Tempo em segundos para o movimento
    """
    pyautogui.moveTo(x, y, duration=duracao)

def scroll(quantidade: int):
    """
    Rola a página.

    Args:
        quantidade: Positivo para cima, negativo para baixo
    """
    pyautogui.scroll(quantidade)

def pegar_posicao_mouse() -> tuple:
    """
    Retorna a posição atual do mouse.

    Returns:
        Tupla (x, y) com a posição
    """
    return pyautogui.position()


# ============================================
# FUNÇÕES DE TECLADO
# ============================================
def digitar(texto: str, intervalo: float = 0.05):
    """
    Digita um texto caractere por caractere.

    Args:
        texto: Texto a ser digitado
        intervalo: Tempo entre cada caractere
    """
    pyautogui.write(texto, interval=intervalo)

def digitar_unicode(texto: str):
    """
    Digita texto com suporte a caracteres especiais (acentos, ç, etc).
    Usa o clipboard para colar o texto.

    Args:
        texto: Texto a ser digitado
    """
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)

def pressionar(tecla: str):
    """
    Pressiona uma tecla única.

    Args:
        tecla: Nome da tecla (enter, tab, esc, space, backspace, delete, etc)
    """
    pyautogui.press(tecla)

def atalho(*teclas: str):
    """
    Executa um atalho de teclado.

    Args:
        teclas: Teclas do atalho (ex: 'ctrl', 'c')
    """
    pyautogui.hotkey(*teclas)

# ============================================
# FUNÇÕES DE CLIPBOARD
# ============================================
def copiar() -> str:
    """
    Executa Ctrl+C e retorna o conteúdo copiado.

    Returns:
        Texto copiado
    """
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    return pyperclip.paste()

def colar():
    """
    Executa Ctrl+V para colar o conteúdo do clipboard.
    """
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)

def definir_clipboard(texto: str):
    """
    Define o conteúdo do clipboard.

    Args:
        texto: Texto a ser colocado no clipboard
    """
    pyperclip.copy(texto)

def obter_clipboard() -> str:
    """
    Obtém o conteúdo atual do clipboard.

    Returns:
        Conteúdo do clipboard
    """
    return pyperclip.paste()

# ============================================
# FUNÇÕES DE LOCALIZAÇÃO POR IMAGEM
# ============================================
def localizar_imagem(caminho_imagem: str, confianca: float = 0.9) -> tuple | None:
    """
    Localiza uma imagem na tela.

    Args:
        caminho_imagem: Caminho para o arquivo de imagem
        confianca: Nível de confiança (0 a 1)

    Returns:
        Tupla (x, y) do centro da imagem ou None se não encontrar
    """
    try:
        posicao = pyautogui.locateCenterOnScreen(caminho_imagem, confidence=confianca)
        return posicao
    except Exception:
        return None

def clicar_imagem(caminho_imagem: str, confianca: float = 0.9) -> bool:
    """
    Localiza uma imagem na tela e clica nela.

    Args:
        caminho_imagem: Caminho para o arquivo de imagem
        confianca: Nível de confiança (0 a 1)

    Returns:
        True se encontrou e clicou, False caso contrário
    """
    posicao = localizar_imagem(caminho_imagem, confianca)
    if posicao:
        pyautogui.click(posicao)
        return True
    return False

def screenshot(caminho: str = None, regiao: tuple = None):
    """
    Tira um screenshot da tela.

    Args:
        caminho: Caminho para salvar a imagem (opcional)
        regiao: Tupla (x, y, largura, altura) para capturar região específica

    Returns:
        Objeto Image do Pillow
    """
    return pyautogui.screenshot(caminho, region=regiao)

# ============================================
# FUNÇÕES UTILITÁRIAS
# ============================================
def esperar(segundos: float):
    """
    Pausa a execução por um tempo.

    Args:
        segundos: Tempo de espera em segundos
    """
    time.sleep(segundos)

def aguardar_imagem(caminho_imagem: str, timeout: int = 30, confianca: float = 0.9) -> tuple | None:
    """
    Aguarda uma imagem aparecer na tela.

    Args:
        caminho_imagem: Caminho para o arquivo de imagem
        timeout: Tempo máximo de espera em segundos
        confianca: Nível de confiança (0 a 1)

    Returns:
        Tupla (x, y) do centro da imagem ou None se timeout
    """
    inicio = time.time()
    while time.time() - inicio < timeout:
        posicao = localizar_imagem(caminho_imagem, confianca)
        if posicao:
            return posicao
        time.sleep(0.5)
    return None

# ============================================
# EXEMPLO DE USO
# ============================================
if __name__ == "__main__":
    print("=== RPA Automation ===")
    print("Funções disponíveis:")
    print()
    print("JANELAS: ativar_janela, maximizar_janela, listar_janelas")
    print("MOUSE: clicar, clicar_direito, mover_mouse, scroll, pegar_posicao_mouse")
    print("TECLADO: digitar, digitar_unicode, pressionar, atalho")
    print("CLIPBOARD: copiar, colar, definir_clipboard, obter_clipboard")
    print("IMAGEM: localizar_imagem, clicar_imagem, screenshot, aguardar_imagem")
    print("UTIL: esperar")
    print()
    print("Iniciando Script")
    print(listar_janelas())
    ativar_janela('ONEWAY   :. 23.258 .:  OW Infinity (udam)')
    print("Dica: Mova o mouse para o canto superior esquerdo para abortar (FAILSAFE)")
    os.system('pause')