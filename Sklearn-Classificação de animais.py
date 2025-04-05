
import tkinter as tk
from tkinter import messagebox
from sklearn import tree

caracteristicas = [
    [20, 50], # Peso 20kg, Altura 50cm
    [5, 25],  # Peso 5kg, Altura 25cm
    [30, 60], # Peso 30kg, Altura 60cm
    [4, 20],  # Peso 4kg, Altura 20cm
    [35, 70], # Peso 35kg, Altura 70cm
    [3, 18],  # Peso 3kg, Altura 18cm
    [28, 55], # Peso 28kg, Altura 55cm
    [6, 30]   # Peso 6kg, Altura 30cm
]
rotulos = [1, 0, 1, 0, 1, 0, 1, 0]
classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(caracteristicas, rotulos)
def prever_animal():

    try:

        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        previsao = classificador.predict([[peso, altura]])
            
        if previsao == 1:
            messagebox.showinfo("Resultado", "Este animal é um Cachorro!")

        else:
            messagebox.showinfo("Resultado", "Este animal é um Gato!")


    except ValueError:

        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")



def mostrar_dicas():

    exemplos = """
    Exemplos de dados e resultados:
    --------------------------------
    Peso: 20kg, Altura: 50cm -> Cachorro
    Peso: 5kg, Altura: 25cm -> Gato
    Peso: 30kg, Altura: 60cm -> Cachorro
    Peso: 4kg, Altura: 20cm -> Gato
    Peso: 28kg, Altura: 55cm -> Cachorro
    Peso: 6kg, Altura: 30cm -> Gato
    """
    campo_dicas.delete(1.0, tk.END)
    campo_dicas.insert(tk.END, exemplos)
janela = tk.Tk()
janela.title("Classificação de Animais")
rotulo_peso = tk.Label(janela,
                       text="Peso (kg):")
rotulo_peso.grid(row=0,
                 column=0,
                 padx=10,
                 pady=10)
entry_peso = tk.Entry(janela)

entry_peso.grid(row=0,
                column=1,
                padx=10,
                pady=10)

rotulo_altura = tk.Label(janela,
                         text="Altura (cm):")
rotulo_altura.grid(row=1,
                   column=0,
                   padx=10,
                   pady=10)

entry_altura = tk.Entry(janela)

entry_altura.grid(row=1,
                  column=1,
                  padx=10,
                  pady=10)

botao_prever = tk.Button(janela,
                         text="Prever",
                         command=prever_animal)

botao_prever.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx=10,
                  pady=10)

botao_dica = tk.Button(janela,
                       text="Dica de Exemplos",
                       command=mostrar_dicas)

botao_dica.grid(row=3,
                column=0,
                columnspan=2,
                padx=10,
                pady=10)

campo_dicas = tk.Text(janela,
                      height=8,
                      width=40)

campo_dicas.grid(row=4,
                 column=0,
                 columnspan=2,
                 padx=10,
                 pady=10)

janela.mainloop()
