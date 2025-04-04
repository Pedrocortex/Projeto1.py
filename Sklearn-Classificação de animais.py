


# O módulo tkinter é usado para criar interfaces gráficas
        # baseadas em janelas no Python
import tkinter as tk

# Importar o módulo messagebox do tkinter
# O messagebox é utilizado para exibir caixas de
        # diálogo de alerta e erro
from tkinter import messagebox

# Importar o módulo tree da biblioteca sklearn
# Este módulo contém implementações de algoritmos para a construção de
        # árvores de decisão, que são modelos de aprendizado supervisionado
        # usados para classificação e regressão
from sklearn import tree

# Definição das características e dos rótulos dos animais
        # para treinar o classificador
# As características consistem em uma lista de listas, onde
        # cada sublista representa um animal
# Cada sublista contém duas características
        # numéricas: peso em kg e altura em cm
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

# Rótulos correspondentes para cada conjunto de características,
        # indicando se o animal é um cachorro (1) ou um gato (0)
rotulos = [1, 0, 1, 0, 1, 0, 1, 0]

# Criação de uma instância do classificador de árvore de decisão
# O classificador é criado usando o método DecisionTreeClassifier(),
    # que configura um modelo de árvore de decisão para ser treinado
classificador = tree.DecisionTreeClassifier()

# Treinamento do classificador com os dados fornecidos
# O método fit é chamado com as características e rótulos como argumentos
# Esse método ajusta o modelo de árvore de decisão aos dados fornecidos,
    # aprendendo a diferenciar cachorros de gatos com base em peso e altura
classificador = classificador.fit(caracteristicas, rotulos)


# Definição da função prever_animal
# Esta função é responsável por capturar o peso e a altura inseridos
# pelo usuário, realizar a previsão usando o classificador e
# exibir o resultado em uma caixa de diálogo.
def prever_animal():

    try:
        # Tenta executar as instruções dentro do bloco try

        # Acessar o valor do campo de entrada 'entry_peso' e tentar
        # convertê-lo para float
        # 'entry_peso.get()' obtém o texto atual no campo de
        # entrada como uma string
        # 'float()' tenta converter a string para um número de
        # ponto flutuante (decimal)
        peso = float(entry_peso.get())

        # Acessar o valor do campo de entrada 'entry_altura' e
        # tentar convertê-lo para float
        # Funciona da mesma maneira que a conversão do peso
        altura = float(entry_altura.get())

        # Realizar a previsão usando o classificador treinado
        # 'classificador.predict()' é chamado com uma lista de
        # listas contendo o peso e a altura
        # Retorna uma lista com os rótulos previstos (1 para
        # cachorro, 0 para gato)
        previsao = classificador.predict([[peso, altura]])

        # Avaliar o resultado da previsão e exibir a mensagem apropriada
        # Se a previsão retornar 1 (cachorro), exibe uma mensagem
        # informando que o animal é um cachorro
        if previsao == 1:

            messagebox.showinfo("Resultado", "Este animal é um Cachorro!")

        # Se a previsão não for 1 (neste caso, será 0, gato), exibe uma
        # mensagem informando que o animal é um gato
        else:

            messagebox.showinfo("Resultado", "Este animal é um Gato!")

    # Bloco except para capturar e tratar exceções específicas que possam
    # ocorrer durante a execução do bloco try
    # Neste caso, captura ValueError, que pode ocorrer se 'float()' falhar
    # ao converter uma string que não representa um número
    except ValueError:

        # Se um ValueError for capturado, exibe uma mensagem de erro
        # pedindo ao usuário para inserir valores numéricos válidos
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")




# Definição da função mostrar_dicas
# Esta função é responsável por exibir exemplos de dados e resultados
# esperados no campo de texto da interface gráfica.
def mostrar_dicas():

    # String multilinha contendo exemplos de dados com os
    # resultados correspondentes
    # Cada linha descreve o peso e a altura de um animal seguido pelo
    # resultado da classificação (Cachorro ou Gato)
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

    # Limpar o campo de texto antes de inserir novos dados
    # 'campo_dicas.delete(1.0, tk.END)' remove todo o texto
    # atual do widget 'campo_dicas'
    # 1.0 indica o início do texto (linha 1, coluna 0),
    # e tk.END indica o final do texto
    campo_dicas.delete(1.0, tk.END)

    # Inserir os exemplos de dados no campo de texto
    # 'campo_dicas.insert(tk.END, exemplos)' adiciona o texto da
    # variável 'exemplos' ao final do campo de texto
    campo_dicas.insert(tk.END, exemplos)


# Criar a janela principal da interface gráfica
        # usando o módulo tkinter
janela = tk.Tk()

# Definir o título da janela
# 'janela.title("Classificação de Animais")' configura o
        # texto que aparece na barra de título da janela
janela.title("Classificação de Animais")


# Criação de um rótulo para o campo de entrada de peso usando a
        # classe Label do módulo tkinter
# O primeiro argumento 'janela' especifica que este rótulo
        # pertence à janela principal criada anteriormente
# O argumento 'text="Peso (kg):"' define o texto que aparecerá no
        # rótulo, indicando ao usuário que aqui ele deve inserir o
        # peso do animal em quilogramas
rotulo_peso = tk.Label(janela,
                       text="Peso (kg):")

# Posicionamento do rótulo na janela usando o gerenciador de layout grid
# 'row=0' e 'column=0' posicionam o rótulo na primeira linha e na
        # primeira coluna da grade
# 'padx=10' e 'pady=10' adicionam um espaço de 10 pixels em torno do
        # rótulo, tanto na horizontal (x) quanto na vertical (y), para
        # estética e melhor separação dos elementos
rotulo_peso.grid(row=0,
                 column=0,
                 padx=10,
                 pady=10)

# Criação de um campo de entrada para o peso usando a
        # classe Entry do módulo tkinter
# O argumento 'janela' novamente especifica que este campo de
        # entrada pertence à janela principal
entry_peso = tk.Entry(janela)

# Posicionamento do campo de entrada na janela usando o
        # gerenciador de layout grid
# 'row=0' e 'column=1' posicionam o campo de entrada ao lado do
        # rótulo na mesma linha, mas na segunda coluna
# 'padx=10' e 'pady=10' são usados novamente para manter uma
        # aparência uniforme e espaço adequado entre os elementos
entry_peso.grid(row=0,
                column=1,
                padx=10,
                pady=10)

# Criação de um rótulo para o campo de entrada de altura usando a
        # classe Label do módulo tkinter
# O primeiro argumento 'janela' especifica que este rótulo pertence à
        # janela principal criada anteriormente
# O argumento 'text="Altura (cm):"' define o texto que aparecerá no
        # rótulo, indicando ao usuário que aqui ele deve inserir a
        # altura do animal em centímetros
rotulo_altura = tk.Label(janela,
                         text="Altura (cm):")

# Posicionamento do rótulo na janela usando o gerenciador
        # de layout grid
# 'row=1' e 'column=0' posicionam o rótulo na segunda
        # linha e na primeira coluna da grade
# 'padx=10' e 'pady=10' adicionam um espaço de 10 pixels em torno do
        # rótulo, tanto na horizontal (x) quanto na vertical (y),
        # para uma separação estética e funcional adequada dos elementos
rotulo_altura.grid(row=1,
                   column=0,
                   padx=10,
                   pady=10)

# Criação de um campo de entrada para a altura usando a
        # classe Entry do módulo tkinter
# O argumento 'janela' especifica novamente que este campo
        # de entrada pertence à janela principal
entry_altura = tk.Entry(janela)

# Posicionamento do campo de entrada na janela usando o
        # gerenciador de layout grid
# 'row=1' e 'column=1' posicionam o campo de entrada ao lado do
        # rótulo na mesma linha, mas na segunda coluna
# 'padx=10' e 'pady=10' são usados novamente para manter uma
        # estética uniforme e garantir espaço adequado entre os elementos
entry_altura.grid(row=1,
                  column=1,
                  padx=10,
                  pady=10)

# Criação de um botão para realizar a previsão
# A classe Button do módulo tkinter é utilizada para criar
        # um botão na interface gráfica
# 'janela' é o argumento que especifica a qual janela o
        # botão pertence
# 'text="Prever"' define o texto que será exibido no
        # botão, orientando o usuário sobre sua função
# 'command=prever_animal' associa este botão à função
        # prever_animal, que é chamada quando o botão é clicado
botao_prever = tk.Button(janela,
                         text="Prever",
                         command=prever_animal)

# Posicionamento do botão na janela usando o gerenciador
        # de layout grid
# 'row=2' e 'column=0' colocam o botão na terceira linha e
        # na primeira coluna
# 'columnspan=2' faz com que o botão se estenda por duas colunas,
        # aumentando sua largura para abranger toda a área designada
# 'padx=10' e 'pady=10' adicionam espaço ao redor do botão,
        # separando-o de outros elementos e melhorando a aparência geral
botao_prever.grid(row=2,
                  column=0,
                  columnspan=2,
                  padx=10,
                  pady=10)

# Criação de um botão para mostrar exemplos de dados
# Similar ao botão de previsão, mas este está associado à
        # função mostrar_dicas
# 'text="Dica de Exemplos"' informa ao usuário que este botão
        # pode ser usado para obter exemplos de como os dados
        # devem ser inseridos
# 'command=mostrar_dicas' vincula o botão à função mostrar_dicas,
        # que exibe exemplos de dados no campo de texto quando clicado
botao_dica = tk.Button(janela,
                       text="Dica de Exemplos",
                       command=mostrar_dicas)

# Posicionamento do botão de dicas na janela
# 'row=3' e 'column=0' colocam o botão na quarta linha, na
        # mesma coluna que o botão de previsão
# Assim como o botão anterior, 'columnspan=2' permite que o
        # botão cubra duas colunas
# Os espaçamentos 'padx' e 'pady' são consistentes com a
        # configuração do outro botão, mantendo a interface uniforme
botao_dica.grid(row=3,
                column=0,
                columnspan=2,
                padx=10,
                pady=10)

# Criação de um campo de texto para exibir exemplos de
        # dados e dicas
# A classe Text do módulo tkinter é usada para criar uma
        # área de texto multi-linha onde textos mais longos podem ser exibidos
# 'janela' é o argumento que define a qual janela o
        # campo de texto pertence
# 'height=8' define a altura do campo de texto em
        # linhas de texto
# 'width=40' define a largura do campo de texto em
        # caracteres de largura média
campo_dicas = tk.Text(janela,
                      height=8,
                      width=40)

# Posicionamento do campo de texto na janela usando o
        # gerenciador de layout grid
# 'row=4' coloca o campo de texto na quinta linha da grade
# 'column=0' inicia o campo de texto na primeira coluna
# 'columnspan=2' faz com que o campo de texto se estenda
        # por duas colunas, proporcionando espaço adequado
        # para a exibição de textos mais extensos
# 'padx=10' e 'pady=10' adicionam espaço ao redor do campo de
        # texto para separá-lo de outros elementos e melhorar a estética
campo_dicas.grid(row=4,
                 column=0,
                 columnspan=2,
                 padx=10,
                 pady=10)

# Inicialização da aplicação Tkinter
# 'janela.mainloop()' entra no loop de eventos da
        # interface gráfica
# Esse loop espera por eventos do usuário, como cliques de
        # botão ou entradas de teclado, e responde a eles
        # conforme definido.
janela.mainloop()