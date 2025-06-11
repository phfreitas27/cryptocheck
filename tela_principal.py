import customtkinter as ctk
from imagens import Imagens
from gui.tela_criptografar import TelaCriptografar
from gui.ajuda import Ajuda

class CryptoCheckApp:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.janela = ctk.CTk()
        self.janela.title("CryptoCheck")
        self.janela.geometry("750x900")
        self.janela.configure(fg_color="#eae7e5")

        self.img = Imagens()
        self.ajuda = Ajuda(self.janela)

        self.tela_criptografar = TelaCriptografar(self.janela, self.img, self.mostrar_tela_principal)

        self.frame_principal = self.criar_tela_principal()
        self.frame_principal.pack(expand=True, fill="both")

    def criar_tela_principal(self):
        frame = ctk.CTkFrame(self.janela, fg_color="#eae7e5")

        ctk.CTkLabel(frame, image=self.img.logo, text="").pack(pady=20)

        ctk.CTkButton(frame, image=self.img.cadeado, text="criptografar",
                      font=("Terminal", 20, "bold"), fg_color="#25733c",
                      hover_color="#1f5e32", text_color="black",
                      width=300, height=60, corner_radius=20,
                      command=self.tela_criptografar.exibir
                      ).pack(pady=20)

        ctk.CTkButton(frame, image=self.img.padlock, text="descriptografar",
                      font=("Terminal", 20, "bold"), fg_color="black",
                      hover_color="#333333", text_color="#25733c",
                      width=300, height=60, corner_radius=30,
                      command=lambda: print("Descriptografar não implementado")
                      ).pack(pady=10)

        ctk.CTkButton(frame, image=self.img.question, text='',
                      width=50, height=50, corner_radius=15,
                      fg_color="black", hover_color="#333333",
                      command=self.ajuda.exibir).place(relx=0.93, rely=0.92, anchor="center")

        return frame

    def mostrar_tela_principal(self):
        self.tela_criptografar.ocultar()
        self.frame_principal.pack(expand=True, fill="both")

    def iniciar(self):
        self.janela.mainloop()