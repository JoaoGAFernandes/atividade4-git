from cadastro import *
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
  

lista=[]
def cadastraInstrumento():
    Nome=entryNome.get()
    Idade=entryIdade.get()
    Email=entryEmail.get()
    tipo=varTipo.get()
    erro=0
    
    if tipo=="Violino":
        if Nome=="":
            messagebox.showinfo("ERRO!","NOME DEVE SER PREENCHIDO")
        erro==1

    if tipo=="Violino":
        if Idade=="":
            messagebox.showinfo("ERRO!","IDADE DEVE SER PREENCHIDO")
        erro==1

    if tipo=="Violino":
        if Email=="":
            messagebox.showinfo("ERRO!","EMAIL DEVE SER PREENCHIDO")
        erro==1

    else:
        c=Cadastro(Nome, Idade, Email)
        salvar(c)
        messagebox.showinfo("Cadastro", f"Pedido de {tipo} Realizado com sucesso!")

    if tipo=="Viola":
        if Nome=="":
             messagebox.showinfo("ERRO!","NOME DEVE SER PREENCHIDO")
        erro==1

    if tipo=="Viola":
        if Idade=="":
            messagebox.showinfo("ERRO!","IDADE DEVE SER PREENCHIDO")
        erro==1

    if tipo=="Viola":
        if Email=="":
            messagebox.showinfo("ERRO!","EMAIL DEVE SER PREENCHIDO")
        erro==1

    else:
        c=Cadastro (Nome, Idade, Email)
        salvar(c)
        messagebox.showinfo("Cadastro", f"Pedido de {tipo} realizado com sucesso!")
        
    if tipo=="Cello":
        if Nome=="":
             messagebox.showinfo("ERRO!","NOME DEVE SER PREENCHIDO")
        erro==1

    if tipo=="Cello":
        if Idade=="":
            messagebox.showinfo("ERRO!","IDADE DEVE SER PREENCHIDO")
        erro==1

    if tipo=="Cello":
        if Email=="":
            messagebox.showinfo("ERRO!","EMAIL DEVE SER PREENCHIDO")
        erro==1

    else:
        c=Cadastro (Nome, Idade, Email)
        salvar(c)
        messagebox.showinfo("Cadastro", f"Pedido de {tipo} realizado com sucesso!")
      
      
        

def salvar(obj):
    lista.append(obj)
    
def atualizaListabox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())



janela = tk.Tk()
janela.title("Catalogo de Instrumentos")
janela.geometry("500x300")


janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1,text="Cadastro")
janelinha.add(tab2,text="Lista")

label1=tk.Label(tab1, text="Nome:", font=("",15))
label1.grid(row=0, column=0, sticky="w", padx=10)

entryNome=tk.Entry(tab1, font=("",15))
entryNome.grid(row=0, column=1, sticky="nsew", padx=10,pady=5)

label2=tk.Label(tab1, text="Idade:", font=("",15))
label2.grid(row=1, column=0, sticky="w", padx=10)

entryIdade=tk.Entry(tab1, font=("",15))
entryIdade.grid(row=1, column=1, sticky="nsew", padx=10,pady=5)

label3=tk.Label(tab1, text="Email:", font=("",15))
label3.grid(row=2, column=0, sticky="w", padx=10)

entryEmail=tk.Entry(tab1, font=("",15))
entryEmail.grid(row=2, column=1, sticky="nsew", padx=10,pady=5)

tk.Label(tab1, text="tipo", font=("", 15)).grid(row=4, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Violino")

tk.Radiobutton(tab1, text="Violino", font=("",15), variable=varTipo, value="Violino").grid(row=4, column=1, sticky="w", padx=10)

tk.Radiobutton(tab1, text="Viola", font=("",15), variable=varTipo, value="Viola").grid(row=4, column=1, sticky="e", padx=10)

tk.Radiobutton(tab1, text="Cello", font=("",15), variable=varTipo, value="Cello").grid(row=4, column=1, sticky="n", padx=10)


tk.Button(tab1, text="Cadastrar", font=("", 15),command=cadastraInstrumento).grid(row=5, columnspan=2)

listbox=tk.Listbox(tab2)
listbox.config(font=("",15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar", font=("",15),command=atualizaListabox).grid(row=1, column=0)

janela.mainloop()

