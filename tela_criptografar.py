import customtkinter as ctk
from tkinter import filedialog, messagebox
from rsa_criptografia import criptografar_texto, carregar_chave_publica, gerar_par_chaves

def criar_tela_criptografar(janela, imagens, voltar_callback):
    frame = ctk.CTkFrame(janela, fg_color="#eae7e5")
    gerar_par_chaves()
    caminho_chave_publica = {"caminho": None}

    def executar_criptografia():
        texto = entrada_texto.get()
        if texto.strip() == "":
            messagebox.showwarning("Atenção", "Digite um texto para criptografar.")
            return

        if not caminho_chave_publica["caminho"]:
            messagebox.showwarning("Atenção", "Selecione uma chave pública antes de criptografar.")
            return

        try:
            chave_pub = carregar_chave_publica(caminho_chave_publica["caminho"])
            texto_cifrado = criptografar_texto(texto, chave_pub)

            texto_criptografado.configure(state="normal")
            texto_criptografado.delete("0.0", "end")
            texto_criptografado.insert("0.0", texto_cifrado)
            texto_criptografado.configure(state="disabled")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na criptografia:\n{e}")

    def selecionar_chave():
        caminho = filedialog.askopenfilename(
            title="Selecione a chave pública",
            filetypes=(("Arquivo PEM", "*.pem"), ("Todos os arquivos", "*.*"))
        )
        if caminho:
            caminho_chave_publica["caminho"] = caminho
            messagebox.showinfo("Chave Selecionada", f"Chave pública carregada:\n{caminho}")
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
        top, image=imagens["voltar"], text="", width=40, height=40,
        corner_radius=15, fg_color="#25733c", hover_color="#1f5e32",
        command=voltar_callback
    ).grid(row=0, column=0)

    # Logo centralizado
    ctk.CTkLabel(frame, image=imagens["logo"], text="").grid(row=1, column=0, pady=10)

    # Entrada de texto
    entrada_frame = ctk.CTkFrame(frame, fg_color="transparent")
    entrada_frame.grid(row=2, column=0, pady=20)

    ctk.CTkLabel(entrada_frame, image=imagens["padlock_2"], text="").grid(row=0, column=0, padx=(0, 10))

    entrada_texto = ctk.CTkEntry(
        entrada_frame, placeholder_text="Digite o texto a ser criptografado",
        width=500, height=50, corner_radius=15,
        fg_color="#2e7d32", text_color="white",
        font=("Terminal", 18), placeholder_text_color="white", justify="center"
    )
    entrada_texto.grid(row=0, column=1)

    # Seleção da chave
    chave_frame = ctk.CTkFrame(frame, fg_color="transparent")
    chave_frame.grid(row=3, column=0, pady=10)

    ctk.CTkLabel(chave_frame, image=imagens["chave"], text="").grid(row=0, column=0, padx=(0, 10))

    ctk.CTkButton(
        chave_frame, text="Selecione a chave pública",
        font=("Terminal", 20, "bold"), fg_color="#2e7d32", hover_color="#256d1b",
        text_color="white", width=400, height=50, corner_radius=15,
        command=selecionar_chave
    ).grid(row=0, column=1)

    # Botão criptografar
    ctk.CTkButton(
        frame, text="Criptografar", font=("Terminal", 18, "bold"),
        fg_color="black", hover_color="#333333", text_color="#2e7d32",
        width=200, height=50, corner_radius=20,
        command=executar_criptografia
    ).grid(row=4, column=0, pady=10)

    # Resultado
    resultado_frame = ctk.CTkFrame(frame, fg_color="transparent")
    resultado_frame.grid(row=5, column=0, pady=20)

    # Ícone cadeado
    ctk.CTkLabel(resultado_frame, image=imagens["padlock_1_2"], text="").grid(row=0, column=0, padx=(30,10))

    # Textbox
    texto_criptografado = ctk.CTkTextbox(
        resultado_frame,
        width=400,
        height=100,
        corner_radius=20,
        fg_color="#2e7d32",
        text_color="white",
        font=("Terminal", 16),
    )
    texto_criptografado.insert("0.0", "Texto Criptografado")
    texto_criptografado.configure(state="disabled")
    texto_criptografado.grid(row=0, column=1)

    # Botão copiar
    ctk.CTkButton(
        resultado_frame,
        image=imagens["copy"],
        text="",
        fg_color="transparent",
        hover_color="#eae7e5",
        cursor="hand2",
        width=0,
        height=0,
        command=lambda: copiar_texto(texto_criptografado)
    ).grid(row=0, column=2, padx=(10, 0))

    frame.grid_columnconfigure(0, weight=1)

    return frame
