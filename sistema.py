# importar as bibliotecas
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# Criar nossa janela 
janela = Tk()
janela.title('Thiago Oliveira LTDA - Acesso Sistema')
janela.geometry('600x300')
janela.configure(background = 'white')
janela.resizable(width = False , height = False)
janela.attributes('-alpha',0.9)
#janela.iconbitmap(default='/Users/thiago/Desktop/projetos python/imagens/LogoIcon.ico')

#Carregar as imagens
logo = PhotoImage(file='/Users/thiago/Desktop/projetos python/logo.png')

# Widgets
LeftFrame = Frame(janela,width=200, height = 300, bg='MIDNIGHTBLUE', relief = 'raise')
LeftFrame.pack(side=LEFT)


RightFrame = Frame(janela,width=395, height = 300, bg='MIDNIGHTBLUE', relief = 'raise')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image = logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50 , y=100)


UserLabel = Label(RightFrame, text = 'Username:', font=('Century Gothic', 20 ), bg = 'MIDNIGHTBLUE', fg = 'white')
UserLabel.place(x=5, y=100)

UserEntry = Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text = 'Password:', font=('Century Gothic', 20 ), bg = 'MIDNIGHTBLUE', fg = 'white')
PassLabel.place(x=5, y=150)

PassEntry = Entry(RightFrame, width=30,show = '*')
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT(User,Password) FROM Users 
    WHERE (User = ? and Password = ?)
    """,(User, Pass))
    print('Selecionou')
    verifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in verifyLogin and Pass in verifyLogin()):
            messagebox.showinfo(title='Login info',message = 'Acesso Confirmado, Bem Vindo!')
    except:
        messagebox.showinfo(title='Login info',message = 'Acesso Negado, Verifique o seu cadastro!')


# Botões
LoginButton = ttk.Button(RightFrame, text = 'Login', width = 30,command= Login)
LoginButton.place(x=100,y=225)


def Register():
    # removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text= 'Name:', font=('Century Gothic', 20 ), bg = 'MIDNIGHTBLUE', fg = 'white')
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=37)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text= 'Email:', font=('Century Gothic', 20 ), bg = 'MIDNIGHTBLUE', fg = 'white')
    EmailLabel.place(x=5, y=55)

    EmaillEntry = ttk.Entry(RightFrame, width=37)
    EmaillEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmaillEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        if (Name =='' and Email == '' and Pass ==''):
            messagebox.showerror(title='Register Error', message = "Não deixe nenhum Campo Vazio. Prencha todos os campos")
        else:
            DataBaser.cursor.execute("""
        INSERT INTO Users(Name, Email, User, Password) Values(?,?,?,?)
        """,(Name, Email, User, Pass))
        # Salvando as alterações
        DataBaser.conn.commit()
        messagebox.showinfo(title='Registando informação', message='Conta criada com sucesso')
    




        
    Register = ttk.Button(RightFrame, text = 'Register', width = 30, command = RegisterToDataBase )
    Register.place(x=100,y=225)

    

    def BackTologin():
        #removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmaillEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
     #trazendo de volta os widgsts de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)
   
    Back = ttk.Button(RightFrame, text = 'Back', width = 20, command=BackTologin)
    Back.place(x=125,y=260)

RegisterButton = ttk.Button(RightFrame, text = 'Register', width = 20, command=Register)
RegisterButton.place(x=125,y=260)


    
janela.mainloop()