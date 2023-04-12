import tkinter as tk
from tkinter import messagebox



def get_text():
    #verificar idade
    text_box_value=text_box.get()
    x=text_box_value
    if x > "18":
        games = tk.Toplevel(window)
        games.geometry("1500x1000")
        label4 = tk.Label(games,text="Bem vindo ao Casino Online")
        label4.pack()
        roletaIMG = tk.PhotoImage(file="imgs/roletaimg.png")
        small_roleta = roletaIMG.subsample(2,2)
        label5=tk.Label(games, image=small_roleta)
        label5.pack()
        label5.bind("<Button-1>", lambda event: roleta())

        #ROLETA

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
                    winLoose=tk.Label(text="Gannhou")
                else:
                    winLoose=tk.Label(text="Perdeu")



            roletaJogo = tk.Toplevel(games)
            roletaJogo.geometry("800x800")
            numeroRoleta= tk.Label(roletaJogo,text="Número da Roleta")
            numeroRoleta.pack()
            valor_roleta = tk.Entry(roletaJogo)
            valor_roleta.pack()
            corRoleta = tk.Label(roletaJogo,text="Cor do Valor")
            corRoleta.pack()
            cor_roleta = tk.Entry(roletaJogo)
            cor_roleta.pack()
            btApostar=tk.Button(roletaJogo,text="APOSTAR")
            btApostar.pack()


            resultadoRoleta = tk.Label(roletaJogo, text="Resultado da Roleta")
            resultadoRoleta.pack()

            #FIM-ROLETA
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

