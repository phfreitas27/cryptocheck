import customtkinter as ctk
from tkinter import filedialog, messagebox
from rsa_criptografia import descriptografar_texto, carregar_chave_privada

def criar_tela_descriptografar(janela, imagens, voltar_callback):
    frame = ctk.CTkFrame(janela, fg_color="#eae7e5")

    caminho_chave_privada = {"caminho": None}

    def executar_descriptografia():
        texto = entrada_texto.get()
        if texto.strip() == "":
            messagebox.showwarning("Atenção", "Digite um texto para descriptografar.")
            return

        if not caminho_chave_privada["caminho"]:
            messagebox.showwarning("Atenção", "Selecione uma chave privada antes de descriptografar.")
            return

        try:
            chave_priv = carregar_chave_privada(caminho_chave_privada["caminho"])
            texto_descript = descriptografar_texto(texto, chave_priv)

            texto_descriptografado.configure(state="normal")
            texto_descriptografado.delete("0.0", "end")
            texto_descriptografado.insert("0.0", texto_descript)
            texto_descriptografado.configure(state="disabled")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na descriptografia:\n{e}")

    def selecionar_chave():
        caminho = filedialog.askopenfilename(
            title="Selecione a chave privada",
            filetypes=(("Arquivo PEM", "*.pem"), ("Todos os arquivos", "*.*"))
        )
        if caminho:
            caminho_chave_privada["caminho"] = caminho
            messagebox.showinfo("Chave Selecionada", f"Chave privada carregada:\n{caminho}")

    def copiar_texto(widget):
        texto = widget.get("0.0", "end").strip()
        if texto:
            widget.clipboard_clear()
            widget.clipboard_append(texto)
            messagebox.showinfo("Copiado", "Texto copiado para a área de transferência.")

    # Topo com botão voltar
    top = ctk.CTkFrame(frame, fg_color="transparent")
    top.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))

    ctk.CTkButton(
        top, image=imagens["Undo_verde"], text="", width=40, height=40,
        corner_radius=15, fg_color="black", hover_color="#333333",
        command=voltar_callback
    ).grid(row=0, column=0)

    # Logo centralizado
    ctk.CTkLabel(frame, image=imagens["logo"], text="").grid(row=1, column=0, pady=10)

    # Entrada de texto
    entrada_frame = ctk.CTkFrame(frame, fg_color="transparent")
    entrada_frame.grid(row=2, column=0, pady=20)

    ctk.CTkLabel(entrada_frame, image=imagens["padlock_verde"], text="").grid(row=0, column=0, padx=(0, 10))

    entrada_texto = ctk.CTkEntry(
        entrada_frame, placeholder_text="Digite o texto a ser descriptografado",
        width=500, height=50, corner_radius=15,
        fg_color="#000000", text_color="#2e7d32",
        font=("Terminal", 18), placeholder_text_color="#2e7d32", justify="center"
    )
    entrada_texto.grid(row=0, column=1)

    # Seleção da chave
    chave_frame = ctk.CTkFrame(frame, fg_color="transparent")
    chave_frame.grid(row=3, column=0, pady=10)

    ctk.CTkLabel(chave_frame, image=imagens["Group_verde"], text="").grid(row=0, column=0, padx=(0, 10))

    ctk.CTkButton(
        chave_frame, text="Selecione a chave privada",
        font=("Terminal", 20, "bold"), fg_color="#000000", hover_color="#333333",
        text_color="#2e7d32", width=400, height=50, corner_radius=15,
        command=selecionar_chave
    ).grid(row=0, column=1)

    # Botão descriptografar
    ctk.CTkButton(
        frame, text="Descriptografar", font=("Terminal", 18, "bold"),
        fg_color="#2e7d32", hover_color="#333333", text_color="white",
        width=200, height=50, corner_radius=20,
        command=executar_descriptografia
    ).grid(row=4, column=0, pady=10)

    # Resultado
    resultado_frame = ctk.CTkFrame(frame, fg_color="transparent")
    resultado_frame.grid(row=5, column=0, pady=20)
    

    # Ícone cadeado
    ctk.CTkLabel(resultado_frame, image=imagens["padlock_verde"], text="").grid(row=0, column=0, padx=(30,10))

    # Textbox
    texto_descriptografado  = ctk.CTkTextbox(
        resultado_frame,
        width=400,
        height=100,
        corner_radius=20,
        fg_color="black",
        text_color="#2e7d32",
        font=("Terminal", 16),
    )
    texto_descriptografado.insert("0.0", "Texto Descriptografado")
    texto_descriptografado.configure(state="disabled")
    texto_descriptografado.grid(row=0, column=1)

    # Botão copiar
    ctk.CTkButton(
        resultado_frame,
        image=imagens["Copy_verde"],
        text="",
        fg_color="transparent",
        hover_color="#eae7e5",
        cursor="hand2",
        width=0,
        height=0,
        command=lambda: copiar_texto(texto_descriptografado)
    ).grid(row=0, column=2, padx=(10, 0))

    frame.grid_columnconfigure(0, weight=1)

    return frame
