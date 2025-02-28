from tkinter import * #importa todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de mensagens do tkinter 
from tkinter import ttk #importa o modulo de widgets tematicos do tkinter 
from database import database # importa a classe database do modulo database

#Criar janela 
jan = Tk() #cria uma instancia da janela principal 

jan.title("SL Sytens - Painel de Acesso") #Define o titulo da janela 

jan.geometry("600x300") #Define o tamanho da janela 

jan.configure(background="white") #Define a cor de fundo da janela 

jan.resizable(width=False, height=False) #Impede que a janela seja redimensionada

#Comando para deixar a tela transparente
jan.attributes("-alpha", 0.9) #Define a transparencia da janela (0.0 a 1.0)

#Definir icone da janela
#jan.iconbitmap(default="") define a logo(colocar depois)

#Carregar imagem
#logo = PhotoImage(file="")# Carrega a imagem do logo 

#Criar Frame 
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTLBLUE", relief="raise")#Cria um frame a esquerda
LeftFrame.pack(side=LEFT)# Posiciona o frame à esquerda

RightFrame = Frame(jan, width=200, height=300,bg="MIDNIGHTLBLUE", relief="raise")# Cria um frame a direita 
RightFrame.pack(side=LEFT) #Posiciona o frame a direita

#Adicinar logo
#LogoLabel = Label(LeftFrame, image=logo, bg= "MIDNIGHTLBLUE" )# Cria um Label para imagem da logo
#LogoLabel.place(x=50, y=100) #Posiciona o label no frame esquerdo

# Adicionar Campos de usuario e senha 
UsuarioLabel = Label(RightFrame, text="Usuario: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")

#Cria uma label para o usuario 
UsuarioLabel.place(x=5, y=100)# Posiciona o label no frame direito 

UsuarioEntry = ttk.Entry(RightFrame, width=30) #Cria um capos de entrada para o usuario 

UsuarioEntry.place(x=120, y=115) #Posiciona o campo de entrada

SenhaLabel = Label(RightFrame, text= "Senha: ", font= ("Century Gothic", 20),  bg="MIDNIGHT", fg= "White")
#Cria uma label para a senha 
SenhaLabel.place(x=5, y=150) #Posiciona o label no frame direito 

#a