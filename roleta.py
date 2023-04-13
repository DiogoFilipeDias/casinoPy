import tkinter as tik
from tkinter import messagebox
import random

roletaJanela = tik.Tk()

roletaJanela.title("ROLETA")
roletaJanela.geometry("500x500")

cores = ['vermelho', 'preto']
cor_aleatoria = random.choice(cores)
print(cor_aleatoria)
numeroAleatorio = random.randint(1, 5)
print(numeroAleatorio)

global valor_roleta_final2
global cor_roleta_final2
def roleta():


    def get_text2():
        valor_roleta_entry = valor_roleta.get()
        valor_roleta_final = valor_roleta_entry
        valor_roleta_final2 == valor_roleta_final
        return  valor_roleta_final2


    def get_text3():

        cor_roleta_entry = cor_roleta.get()
        cor_roleta_final = cor_roleta_entry
        return cor_roleta_final




def jogarRoleta():
    if valor_roleta_final2 == numeroAleatorio and cor_roleta_final2 == cor_aleatoria:
         if numeroAleatorio == "1" and cor_aleatoria == "vermelho":
            print("Ganhou")
         else:
                print("perdeu")
    else:
        print("Jogue novamente")

numeroRoleta = tik.Label(roletaJanela, text="Número da Roleta")
numeroRoleta.pack()
valor_roleta = tik.Entry(roletaJanela)
valor_roleta.pack()
corRoleta = tik.Label(roletaJanela, text="Cor do Valor")
corRoleta.pack()
cor_roleta = tik.Entry(roletaJanela)
cor_roleta.pack()
btApostar = tik.Button(roletaJanela, text="APOSTAR", command=jogarRoleta)
btApostar.pack()

resultadoRoleta = tik.Label(roletaJanela, text="Resultado da Roleta")
resultadoRoleta.pack()


roletaJanela.mainloop()


