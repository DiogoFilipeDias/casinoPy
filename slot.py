import  tkinter as tk
import random

slotJanela = tk.Tk()
slotJanela.title("SLOT")
slotJanela.geometry("500x500")

slot1random = ['777', 'MEGA', 'BONUS']


slot2random = ['777', 'MEGA', 'BONUS']


slot3random = ['777', 'MEGA', 'BONUS']

ResultadoTexto = tk.Label(text="")
diviao = tk.Label(text="#########################")

def slotWin():
    print("#########################")
    global radomSlot1
    radomSlot1 = random.choice(slot1random)
    print("RESULTADO SLOT1", radomSlot1)
    global randomSlot2
    radomSlot2 = random.choice(slot2random)
    print("RESULTADO SLOT2", radomSlot2)
    global randomSlot2
    radomSlot3 = random.choice(slot3random)
    print("RESULTADO SLOT3", radomSlot3)
    print("#########################")
    print("\n")

    if radomSlot1 == '777' and radomSlot2 == '777' and slot3random == '777':
        print("GANHOU O JACKPOT!")
    elif radomSlot1 == 'MEGA' and radomSlot2 == 'MEGA' and radomSlot3 == 'MEGA':
        print("GANHOU 250K €")
    elif radomSlot1 == 'BONUS' and radomSlot2 == 'BONUS' and radomSlot3 == 'BONUS':
        print("GANHOU 50K €")
    else:
        print("Perdeu")



btApostar = tk.Button(slotJanela, text="Jogar", command=slotWin)
btApostar.pack()





slotJanela.mainloop()