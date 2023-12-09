import tkinter as tk
import random

# Configurações
largura = 400
altura = 400
divisoes = 10
numeros_por_lista = 12
numero_maximo = 400

# Geração de números aleatórios para as listas x e y
lista_x = [random.uniform(0, numero_maximo) - 2 for _ in range(numeros_por_lista)]
lista_y = [random.uniform(0, numero_maximo) - 2 for _ in range(numeros_por_lista)]

# Função para calcular as cotas do tabuleiro
def calcular_cotas(lista):
    maximo = max(lista)
    minimo = min(lista)
    cota = (maximo - minimo) / divisoes
    return cota

# Função para desenhar círculos nas coordenadas especificadas
def desenhar_circulos():
    for i in range(numeros_por_lista):
        x = lista_x[i] 
        y = lista_y[i]
        canvas.create_oval(x - 5, y - 5,x + 5,y + 5, fill="black")

# Criar a janela e o canvas
janela = tk.Tk()
janela.title("Tabuleiro")
canvas = tk.Canvas(janela, width=largura, height=altura, bg="yellow")
canvas.pack()

# Desenhar divisões do tabuleiro
for i in range(0, largura, largura // divisoes):
    canvas.create_line(i, 0, i, altura, fill="black")

for j in range(0, altura, altura // divisoes):
    canvas.create_line(0, j, largura, j, fill="black")

# Chamar a função para desenhar os círculos
desenhar_circulos()

# Iniciar o loop da interface gráfica
janela.mainloop()

