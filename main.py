import tkinter as tk
from tkinter import messagebox
import subprocess


def run_roleta():
    subprocess.run(['python', 'roleta.py'])
def roletaImagem(event):
    run_roleta()

def get_text():
    #verificar idade
    text_box_value=text_box.get()
    x=text_box_value
    if x > "18":
        games = tk.Toplevel(window)
        games.geometry("800x800")
        label4 = tk.Label(games,text="Bem vindo ao Casino Online")
        label4.pack()
        roletaIMG = tk.PhotoImage(file="imgs/roletaimg.png")
        small_roleta = roletaIMG.subsample(2,2)
        label5=tk.Label(games, image=small_roleta)
        label5.bind("<Button-1>", roletaImagem)
        label5.pack()
        games.mainloop()
    else:
        messagebox.showwarning(title="REJEITADO",message="Lamento, mas menores de idade não podem jogar :(")



window = tk.Tk()

window.title("Dados")
window.geometry("500x500")

label = tk.Label(window, text = "Bem-Vindo")

label2 = tk.Label(window, text="Insira a sua idade")

text_box = tk.Entry(window)
button=tk.Button(window, text="Get Text", command=get_text)
button.pack()

label3=tk.Label()
label3.pack()

text_box.pack()
label.pack()
label2.pack()
window.mainloop()

