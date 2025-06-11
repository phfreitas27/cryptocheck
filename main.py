import customtkinter as ctk
# Certifique-se de que seus arquivos estão na mesma pasta ou acessíveis
from assets import carregar_imagens 
from ajuda import ajuda
from tela_criptografar import criar_tela_criptografar
from tela_descriptografar import criar_tela_descriptografar
import sys
import os

# --- Bloco de Código para a Splash Screen ---
# Este código só funciona quando executado pelo .exe
try:
    import pyi_splash

    # Opcional: Mudar o texto da splash screen durante o carregamento
    pyi_splash.update_text("Carregando componentes...")

    # Fecha a splash screen para mostrar a janela principal
    pyi_splash.close()
except ImportError:
    # Se não estiver rodando via .exe, apenas ignora
    pass
# --- Fim do Bloco de Código ---

def resource_path(relative_path):
    """ Retorna o caminho absoluto para o recurso, funciona para dev e para PyInstaller """
    try:
        # PyInstaller cria uma pasta temp e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.geometry("750x900")
janela.title("CryptoCheck")

icon_path = resource_path("imagens/logo_transparente_icon.ico")
janela.iconbitmap(icon_path)

janela.configure(fg_color="#eae7e5")

# Supondo que sua função 'carregar_imagens()' retorna um dicionário com os objetos de imagem
imagens = carregar_imagens()

# --- ESTRUTURA DA BARRA DE ROLAGEM ---
# 1. Criamos um frame rolável que preenche a janela
scrollable_frame = ctk.CTkScrollableFrame(janela, fg_color="#eae7e5")
scrollable_frame.pack(fill="both", expand=True)

# Função para alternar a visibilidade dos frames
def mostrar_frame(frame):
    for f in [frame_principal, frame_criptografar, frame_descriptografar]:
        f.pack_forget()
    # Empacota o frame desejado DENTRO do frame rolável
    frame.pack(pady=20, fill="both", expand=True)

# --- CONTEÚDO ORIGINAL DENTRO DO FRAME ROLÁVEL ---
# 2. Todos os frames de conteúdo agora são filhos do 'scrollable_frame'

# Frame principal
frame_principal = ctk.CTkFrame(scrollable_frame, fg_color="#eae7e5")
ctk.CTkLabel(frame_principal, image=imagens["logo"], text="").pack(pady=20)

ctk.CTkButton(frame_principal, image=imagens["cadeado"], text="criptografar",
              font=("Terminal", 20, "bold"), fg_color="#25733c",
              hover_color="#1f5e32", text_color="black", width=300, height=60,
              corner_radius=20,
              command=lambda: mostrar_frame(frame_criptografar)).pack(pady=20)

ctk.CTkButton(frame_principal, image=imagens["padlock"], text="descriptografar",
              font=("Terminal", 20, "bold"), fg_color="black",
              hover_color="#333333", text_color="#25733c", width=300,
              height=60, corner_radius=30,
              command=lambda: mostrar_frame(frame_descriptografar)).pack(pady=10)

# Tela criptografar (usando sua função original)
frame_criptografar = criar_tela_criptografar(scrollable_frame, imagens, lambda: mostrar_frame(frame_principal))

# Tela descriptografar (usando sua função original)
frame_descriptografar = criar_tela_descriptografar(scrollable_frame, imagens, lambda: mostrar_frame(frame_principal))

# --- ELEMENTOS FIXOS (FORA DA ÁREA DE ROLAGEM) ---
# O botão de ajuda continua sendo filho da 'janela' para ficar fixo no lugar
ctk.CTkButton(janela, image=imagens["question"], text="",
              fg_color="black", hover_color="#333333", text_color="#25733c",
              width=50, height=50, corner_radius=15,
              command=lambda: ajuda(janela)).place(relx=0.93, rely=0.92, anchor="center")

# Inicia mostrando o frame principal
mostrar_frame(frame_principal)

janela.mainloop()