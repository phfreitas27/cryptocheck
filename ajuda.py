import customtkinter as ctk

def ajuda(janela):
    ajuda_janela = ctk.CTkToplevel(janela)
    ajuda_janela.overrideredirect(True)
    ajuda_bg = "#000000"
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    mensagens = [
        {
            "titulo": "O quê é CryptoCheck?",
            "texto": "CryptoCheck é um sistema de criptografia do tipo RSA, através dele o usuário pode tanto criptografar quanto descriptografar mensagens com segurança."
        },
        {
            "titulo": "Para que serve CryptoCheck?",
            "texto": "Perfeito para proteger informações que necessitam ser protegidas. Através do sistema, mensagens, senhas e links por exemplo, são protegidas pelo sistema de criptografia RSA, mantendo o conteúdo da mensagem protegida e de acesso apenas a aqueles q possuírem uma chave única de acesso."
        },
        {
            "titulo": "Como usar CryptoCheck?",
            "texto": "O sistema CryptoCheck foi desenvolvido para ser extremamente simples, intuitivo e direto com o usuário.\n\n"
                     "Para criptografar e proteger uma mensagem, deve-se clicar na opção criptografar, escrever o conteúdo a ser criptografado, escolher a Chave Pública e então a mensagem será criptografada.\n\n"
                     "Para descriptografar e revelar uma mensagem, deve-se clicar na opção Descriptografar, escrever o conteúdo criptografado, escolher a Chave Privada e então a mensagem será descriptografada."
        }
    ]
    current_message_index = 0
    titulo_label, texto_box, left_arrow_btn, right_arrow_btn = None, None, None, None

    def update_content():
        nonlocal titulo_label, texto_box, left_arrow_btn, right_arrow_btn
        
        mensagem_atual = mensagens[current_message_index]

        # --- ALTERAÇÃO 1: Aumentar a altura da caixa de texto ---
        # Aumentei os valores base e por linha. Sinta-se à vontade para ajustá-los.
        base_height = 150  # Era 100
        height_per_line = 35 # Era 30
        num_newlines = mensagem_atual["texto"].count('\n')
        new_height = base_height + (num_newlines * height_per_line)
        
        texto_box.configure(height=new_height)

        titulo_label.configure(text=mensagem_atual["titulo"])
        texto_box.configure(state="normal")
        texto_box.delete("0.0", "end")
        texto_box.insert("0.0", mensagem_atual["texto"])
        texto_box.configure(state="disabled")
        left_arrow_btn.configure(state="disabled" if current_message_index == 0 else "normal", fg_color="gray20" if current_message_index == 0 else "#2e7d32")
        right_arrow_btn.configure(state="disabled" if current_message_index == len(mensagens) - 1 else "normal", fg_color="gray20" if current_message_index == len(mensagens) - 1 else "#2e7d32")

    def next_message():
        nonlocal current_message_index
        if current_message_index < len(mensagens) - 1:
            current_message_index += 1
            update_content()

    def prev_message():
        nonlocal current_message_index
        if current_message_index > 0:
            current_message_index -= 1
            update_content()

    def expand():
        width, height = 10, 10
        x, y = screen_width - width, screen_height - height
        def animar():
            nonlocal width, height, x, y
            if width < screen_width or height < screen_height:
                width = min(width + 45, screen_width)
                height = min(height + 45, screen_height)
                x = screen_width - width
                y = screen_height - height
                ajuda_janela.geometry(f"{width}x{height}+{x}+{y}")
                ajuda_janela.after(5, animar)
            else:
                ajuda_janela.geometry(f"{screen_width}x{screen_height}+0+0")
                carregar_conteudo()
        animar()

    def carregar_conteudo():
        nonlocal titulo_label, texto_box, left_arrow_btn, right_arrow_btn
        
        # --- ALTERAÇÃO 2: LÓGICA DE LAYOUT MISTO ---

        # 1. Título e setas são empacotados no TOPO
        title_frame = ctk.CTkFrame(ajuda_janela, fg_color="transparent")
        title_frame.pack(side="top", fill="x", padx=100, pady=(50, 20))

        left_arrow_btn = ctk.CTkButton(title_frame, text="<", font=("Terminal", 30, "bold"), width=60, command=prev_message)
        left_arrow_btn.pack(side="left", padx=20)
        
        titulo_label = ctk.CTkLabel(title_frame, text="", font=("Terminal", 26, "bold"), text_color="#2e7d32")
        titulo_label.pack(side="left", fill="x", expand=True, padx=20)
        
        right_arrow_btn = ctk.CTkButton(title_frame, text=">", font=("Terminal", 30, "bold"), width=60, command=next_message)
        right_arrow_btn.pack(side="right", padx=20)
        
        # 2. Botão Fechar é empacotado na BASE
        fechar_btn = ctk.CTkButton(ajuda_janela, text="Fechar", fg_color="#2e7d32", hover_color="#256d1b", 
                                   font=("Terminal", 18, "bold"), command=retrair, height=40)
        fechar_btn.pack(side="bottom", pady=40)

        # 3. Caixa de texto é criada...
        texto_box = ctk.CTkTextbox(ajuda_janela, fg_color="black", text_color="white",
                                   width=800, corner_radius=20, 
                                   border_color="#2e7d32", border_width=2,
                                   font=("Terminal", 16), wrap="word")
        
        # ... e então POSICIONADA no centro do espaço restante
        texto_box.place(relx=0.5, rely=0.5, anchor="center")
        
        update_content()

    def retrair():
        width, height = screen_width, screen_height
        def animar():
            nonlocal width, height
            if width > 20 or height > 20:
                width, height = max(width - 45, 20), max(height - 45, 20)
                x, y = screen_width - width, screen_height - height
                ajuda_janela.geometry(f"{width}x{height}+{x}+{y}")
                ajuda_janela.after(5, animar)
            else:
                ajuda_janela.destroy()
        animar()

    ajuda_janela.configure(fg_color=ajuda_bg)
    expand()