import numpy as np  # dinossauro bebado
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#pimba

def evolucao_patrimonial(e):
    x = 0
    n = int(numerodemeses.get())+1
    j = float(jurosmensais.get())/100
    t = list(range(0, n))  # x do gráfico
    y = []  # y do gráfico (investido)
    ap = []  # y do gráfico (aportado)
    jurostotalMontante = ""
    while x <= float(numerodemeses.get()):
        montante = (float(valorinicial.get()))*((1+j)**x)
        jurostotal = ((float(valoraporte.get())*((1+j)**x - 1)))/j
        y.append(jurostotal+montante)
        apo = float(valoraporte.get())*x + float(valorinicial.get())
        ap.append(apo)
        ap1 = float(valoraporte.get())*(float(numerodemeses.get()))
        ap2 = float(valorinicial.get())
        jurostotalMontante = jurostotalMontante + \
            (f"Mês: {x}, Valor: R${jurostotal+montante:.2f} \n")
        x += 1
    texto_valor["text"] = (jurostotalMontante)
    texto_valoraportado.grid(column=0, row=5)
    texto_valoraportado["text"] = (f"Valor aportado: R$ {(ap1 + ap2 ):.2f}")
    texto_valortotal["text"] = (
        f"Valor total: R$ {(jurostotal + montante):.2f}")

    figura = plt.Figure(figsize=(8, 4), dpi=60)
    grafico = figura.add_subplot(111)

    grafico.set_title('Evolução patrimonial')
    grafico.set_ylabel('Valor')
    grafico.set_xlabel('Meses')
    grafico.plot(t, y, color="green")
    grafico.plot(t, ap, color="orange")

    canva = FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(column=10, row=0)


janela = Tk()
janela.title("Evolução patrimonial")


texto_orientacao = Label(janela, text="Valor inicial: ")
texto_orientacao.grid(column=0, row=0)
valorinicial = Entry(janela)
valorinicial.grid(column=1, row=0)


texto_orientacao2 = Label(janela, text="Juros mensal: ")
texto_orientacao2.grid(column=0, row=1)
jurosmensais = Entry(janela)
jurosmensais.grid(column=1, row=1)

texto_orientacao3 = Label(janela, text="Aportes mensais: ")
texto_orientacao3.grid(column=0, row=2)
valoraporte = Entry(janela)
valoraporte.grid(column=1, row=2)

texto_orientacao4 = Label(janela, text="Número de meses: ")
texto_orientacao4.grid(column=0, row=3)
numerodemeses = Entry(janela)
numerodemeses.grid(column=1, row=3)

texto_valor = Label(janela, text="")
texto_valor.grid(column=0, row=4)

texto_valoraportado = Label(janela, text="")

texto_valortotal = Label(janela, text="")
texto_valortotal.grid(column=0, row=6)

janela.bind('<Return>', evolucao_patrimonial)


janela.mainloop()