"""
Sistema Empresarial de Conversão de Chapas
Versão Moderna - Interface Profissional

Autor: Gustavo Alves
"""

import tkinter as tk
from tkinter import ttk, messagebox


# =========================
# Dados
# =========================

FORNECEDORES = {
    "Valinhos": {"B": 350, "C": 370},
    "São Carlos": {"B": 345, "C": 390},
    "Novaki": {"B": 325, "C": 335},
    "Woodlog": {"B": 330, "C": 382},
}


# =========================
# Função de Cálculo
# =========================

def calcular():
    try:
        fornecedor = fornecedor_var.get()
        tipo_onda = onda_var.get()

        if fornecedor not in FORNECEDORES:
            raise ValueError("Selecione um fornecedor válido.")

        if tipo_onda not in FORNECEDORES[fornecedor]:
            raise ValueError("Selecione o tipo de onda.")

        gramatura = FORNECEDORES[fornecedor][tipo_onda]

        largura_mm = float(entry_largura.get())
        comprimento_mm = float(entry_comprimento.get())
        peso_total_kg = float(entry_peso.get())

        if largura_mm <= 0 or comprimento_mm <= 0:
            raise ValueError("Medidas devem ser maiores que zero.")

        if peso_total_kg <= 0:
            raise ValueError("Peso total deve ser maior que zero.")

        # Fórmula correta
        peso_unitario = (largura_mm * comprimento_mm * gramatura) / 1_000_000_000
        quantidade = peso_total_kg / peso_unitario

        resultado_text.set(
            f"Gramatura aplicada: {gramatura} g/m²\n"
            f"Peso unitário: {peso_unitario:.6f} KG\n"
            f"Quantidade estimada: {quantidade:.0f} chapas"
        )

    except ValueError as e:
        messagebox.showerror("Erro de Validação", str(e))
    except Exception as e:
        messagebox.showerror("Erro inesperado", str(e))


def limpar():
    entry_largura.delete(0, tk.END)
    entry_comprimento.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_text.set("")


# =========================
# Interface
# =========================

root = tk.Tk()
root.title("Sistema Empresarial - Conversão de Chapas")
root.geometry("600x500")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Título
titulo = tk.Label(
    root,
    text="Sistema Empresarial de Conversão de Chapas",
    font=("Segoe UI", 16, "bold"),
    bg="#f4f6f9",
    fg="#1f2937"
)
titulo.pack(pady=20)

# Frame principal
frame = tk.Frame(root, bg="white", bd=0)
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Seção Dados
secao_dados = tk.Label(frame, text="Dados do Recebimento", font=("Segoe UI", 12, "bold"), bg="white")
secao_dados.pack(anchor="w", pady=(10, 5))

dados_frame = tk.Frame(frame, bg="white")
dados_frame.pack(pady=5)

fornecedor_var = tk.StringVar()
onda_var = tk.StringVar()

ttk.Label(dados_frame, text="Fornecedor:").grid(row=0, column=0, sticky="w", pady=5)
ttk.Combobox(dados_frame, textvariable=fornecedor_var, values=list(FORNECEDORES.keys()), state="readonly", width=20).grid(row=0, column=1, pady=5)

ttk.Label(dados_frame, text="Tipo de Onda:").grid(row=1, column=0, sticky="w", pady=5)
ttk.Combobox(dados_frame, textvariable=onda_var, values=["B", "C"], state="readonly", width=20).grid(row=1, column=1, pady=5)

ttk.Label(dados_frame, text="Largura (mm):").grid(row=2, column=0, sticky="w", pady=5)
entry_largura = ttk.Entry(dados_frame, width=22)
entry_largura.grid(row=2, column=1, pady=5)

ttk.Label(dados_frame, text="Comprimento (mm):").grid(row=3, column=0, sticky="w", pady=5)
entry_comprimento = ttk.Entry(dados_frame, width=22)
entry_comprimento.grid(row=3, column=1, pady=5)

ttk.Label(dados_frame, text="Peso Total (KG):").grid(row=4, column=0, sticky="w", pady=5)
entry_peso = ttk.Entry(dados_frame, width=22)
entry_peso.grid(row=4, column=1, pady=5)

# Botões
btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=15)

ttk.Button(btn_frame, text="Calcular", command=calcular).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="Limpar", command=limpar).grid(row=0, column=1, padx=10)

# Resultado
secao_resultado = tk.Label(frame, text="Resultado", font=("Segoe UI", 12, "bold"), bg="white")
secao_resultado.pack(anchor="w", pady=(20, 5))

resultado_text = tk.StringVar()
resultado_label = tk.Label(
    frame,
    textvariable=resultado_text,
    bg="#e5e7eb",
    fg="#111827",
    font=("Consolas", 11),
    justify="left",
    padx=15,
    pady=15,
    width=60,
    height=6
)
resultado_label.pack(pady=5)

root.mainloop()

