import tkinter as tk
from tkinter import messagebox
import random

roletaJanela = tk.Tk()

roletaJanela.title("ROLETA")
roletaJanela.geometry("500x500")

cores = ['vermelho', 'preto']
cor_aleatoria = random.choice(cores)
numeroAleatorio = random.randint(1, 5)
print(numeroAleatorio)
def probRoleta():

    if numeroAleatorio == "1":
        cores == 'vermelho'
    elif numeroAleatorio == "2":
        cores  == "preto"
    elif numeroAleatorio == "3":
        cores == "vermelho"
    elif numeroAleatorio == "4":
        cores == "preto"
    elif numeroAleatorio == "5":
        cores == "vermelho"


def roleta():
    def get_text2():
        valor_roleta_entry = valor_roleta.get()
        valor_roleta_final = valor_roleta_entry

    global valor_roleta_final

    def get_text3():
        cor_roleta_entry = cor_roleta.get()
        cor_roleta_final = cor_roleta_entry

    global cor_roleta_final

    def jogarRoleta():
        if valor_roleta_final == "2" and cor_roleta_final == "preto":
            winLoose = tk.Label(text="Ganhou")
        elif valor_roleta_final == "1" and cor_roleta_final == "vermelho":
            winLoose = tk.Label(text="Gannhou")
        else:
            winLoose = tk.Label(text="Perdeu")

    numeroRoleta = tk.Label(roleta, text="Número da Roleta")
    numeroRoleta.pack()
    valor_roleta = tk.Entry(roleta)
    valor_roleta.pack()
    corRoleta = tk.Label(roleta, text="Cor do Valor")
    corRoleta.pack()
    cor_roleta = tk.Entry(roleta)
    cor_roleta.pack()
    btApostar = tk.Button(roleta, text="APOSTAR")
    btApostar.pack()

    resultadoRoleta = tk.Label(roleta, text="Resultado da Roleta")
    resultadoRoleta.pack()


roletaJanela.mainloop()


