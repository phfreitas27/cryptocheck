from PIL import Image
import customtkinter as ctk
import os
import sys

def recurso_path(rel_path):
    """Resolve o caminho para recursos (compatível com PyInstaller)."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, rel_path)

def carregar_imagens():
    return {
        "logo": ctk.CTkImage(Image.open(recurso_path("imagens/logo_transparente.png")), size=(300, 300)),
        "cadeado": ctk.CTkImage(Image.open(recurso_path("imagens/Lock.png")), size=(25, 25)),
        "padlock": ctk.CTkImage(Image.open(recurso_path("imagens/Padlock.png")), size=(25, 25)),
        "padlock_2": ctk.CTkImage(Image.open(recurso_path("imagens/Padlock_2.png")), size=(50, 50)),
        "padlock_1_2": ctk.CTkImage(Image.open(recurso_path("imagens/Lock.png")), size=(50, 50)),
        "question": ctk.CTkImage(Image.open(recurso_path("imagens/Question.png")), size=(25, 25)),
        "chave": ctk.CTkImage(Image.open(recurso_path("imagens/Key.png")), size=(50, 50)),
        "copy": ctk.CTkImage(Image.open(recurso_path("imagens/Copy.png")), size=(50, 50)),
        "voltar": ctk.CTkImage(Image.open(recurso_path("imagens/Back.png")), size=(30, 30)),
        "padlock_verde": ctk.CTkImage(Image.open(recurso_path("imagens/Padlock_verde.png")), size=(50, 50)),
        "Undo_verde": ctk.CTkImage(Image.open(recurso_path("imagens/Undo_verde.png")), size=(30, 30)),
        "Lock_verde": ctk.CTkImage(Image.open(recurso_path("imagens/Lock_verde.png")), size=(50, 50)),
        "Group_verde": ctk.CTkImage(Image.open(recurso_path("imagens/Group_verde.png")), size=(50, 50)),
        "Copy_verde": ctk.CTkImage(Image.open(recurso_path("imagens/Copy_verde.png")), size=(50, 50)),
    }
