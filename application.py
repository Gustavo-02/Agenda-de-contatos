from tkinter import *
import tkinter.messagebox
import Agenda_BackEnd




class Agenda:
    def __init__(self, tela):
        self.tela = tela
        self.tela.title("Agenda de Contatos")
        self.tela.geometry("820x686+300+0")
        self.tela.resizable(width = False, height = False)
        self.tela.iconbitmap('imagenparaicone.ico')


        CntID = StringVar()
        Nome = StringVar()
        Sobrenome = StringVar()
        Email = StringVar()
        Telefone = StringVar()
        Idade = StringVar()
        Cpf = StringVar()
        Sexo = StringVar()


        #------------------------------------------------------------Variaveis-----------------------------------------------------------------------------------------
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Sair da agenda", "Deseja mesmo sair da agenda ?")
            if iExit > 0:
                tela.destroy()
                return 

        def LimparDados():
            self.textID.delete(0,END)
            self.textNome.delete(0,END)
            self.textSobreN.delete(0,END)
            self.textEmail.delete(0,END)
            self.textTel.delete(0,END)
            self.textIdade.delete(0,END)
            self.textCpf.delete(0,END)
            self.textSexo.delete(0,END)

        def AdicionarContato():
            if(len(CntID.get()) != 0):
                Agenda_BackEnd.AddContato(CntID.get(), Nome.get(), Sobrenome.get(), Email.get(), Telefone.get(), Idade.get(), Cpf.get(), Sexo.get())
                listaContatos.delete(0,END)
                listaContatos.insert(END,(CntID.get(), Nome.get(), Sobrenome.get(), Email.get(), Telefone.get(), Idade.get(), Cpf.get(), Sexo.get()))

        def Exibisao():
            listaContatos.delete(0, END)
            for row in Agenda_BackEnd.view():
                listaContatos.insert(END,row,str(""))

        def ContatoRec(event):
            global sd 
            searchCnt = listaContatos.curselection()[0]
            sd = listaContatos.get(searchCnt)
            self.textID.delete(0,END)
            self.textID.insert(END, sd[1])
            self.textNome.delete(0,END)
            self.textNome.insert(END, sd[2])
            self.textSobreN.delete(0,END)
            self.textSobreN.insert(END, sd[3])
            self.textEmail.delete(0,END)
            self.textEmail.insert(END, sd[4])
            self.textTel.delete(0,END)
            self.textTel.insert(END, sd[5])
            self.textIdade.delete(0,END)
            self.textIdade.insert(END, sd[6])
            self.textCpf.delete(0,END)
            self.textCpf.insert(END, sd[7])
            self.textSexo.delete(0,END)
            self.textSexo.insert(END, sd[8])


        def Del():
            if(len(CntID.get()) != 0):
                Agenda_BackEnd.deletar(sd[0])
                LimparDados()
                Exibisao()


        def BuscarContato():
            listaContatos.delete(0,END)
            for row in Agenda_BackEnd.busca(CntID.get(), Nome.get(), Sobrenome.get(), Email.get(), Telefone.get(), Idade.get(), Cpf.get(), Sexo.get()):
                listaContatos.insert(END,row,str(""))

        def atualizarContato():
            if(len(CntID.get()) != 0):
                Agenda_BackEnd.deletar(sd[0])
            if(len(CntID.get()) != 0):
                Agenda_BackEnd.AddContato(CntID.get(), Nome.get(), Sobrenome.get(), Email.get(), Telefone.get(), Idade.get(), Cpf.get(), Sexo.get())
                listaContatos.delete(0, END)
                listaContatos.insert(END, (CntID.get(), Nome.get(), Sobrenome.get(), Email.get(), Telefone.get(), Idade.get(), Cpf.get(), Sexo.get()))




         #-------------------------------------------------FRAMES----------------------------------------------------------------------------------

        MainFrame = Frame(tela, bd=10, width = 760, height = 600, relief = RIDGE, bg = 'black')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd = 7, width = 855, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd= 5, width = 855, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 770, height = 400, padx =2, bg = 'grey',relief = RIDGE)
        LeftFrame.pack(side = LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width = 600, height = 180, padx = 12, pady = 9, relief = RIDGE)
        LeftFrame1.pack(side = TOP)

        RightFrame = Frame(TopFrame3, bd = 5, width = 100, height = 400, padx =2, bg = 'grey',relief = RIDGE)
        RightFrame.pack(side = RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width = 90, height = 300, padx = 2, pady = 2, relief = RIDGE)
        RightFrame1.pack(side = TOP)

        #-------------------------------------------------Lebels e Vars----------------------------------------------------------------------------------


        self.lbTitulo = Label(TitleFrame, font=('arial 40 bold'), text = "Cadastro de contato", bd = 7)
        self.lbTitulo.grid(row = 0, column = 0, padx =132)


        self.lblID = Label(LeftFrame1, font=('arial 12 bold'), text = "ID :", bd = 7)
        self.lblID.grid(row = 1, column = 0, sticky = W, padx = 5)
        self.textID = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = CntID)
        self.textID.grid(row = 1, column = 1, sticky = W, padx = 5)

        self.lblNome = Label(LeftFrame1, font=('arial 12 bold'), text = "Nome :", bd = 7)
        self.lblNome.grid(row = 2, column = 0, sticky = W, padx = 5)
        self.textNome = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Nome)
        self.textNome.grid(row = 2, column = 1, sticky = W, padx = 5)

        self.lblSobreN = Label(LeftFrame1, font=('arial 12 bold'), text = "Sobrenome :", bd = 7)
        self.lblSobreN.grid(row = 3, column = 0, sticky = W, padx = 5)
        self.textSobreN = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Sobrenome)
        self.textSobreN.grid(row = 3, column = 1, sticky = W, padx = 5)

        self.lblEmail = Label(LeftFrame1, font=('arial 12 bold'), text = "Email :", bd = 7)
        self.lblEmail.grid(row = 4, column = 0, sticky = W, padx = 5)
        self.textEmail = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Email)
        self.textEmail.grid(row = 4, column = 1, sticky = W, padx = 5)

        self.lblCpf = Label(LeftFrame1, font=('arial 12 bold'), text = "CPF :", bd = 7)
        self.lblCpf.grid(row = 5, column = 0, sticky = W, padx = 5)
        self.textCpf = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Cpf)
        self.textCpf.grid(row = 5, column = 1, sticky = W, padx = 5)

        self.lblTel = Label(LeftFrame1, font=('arial 12 bold'), text = "Telefone :", bd = 7)
        self.lblTel.grid(row = 6, column = 0, sticky = W, padx = 5)
        self.textTel = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Telefone)
        self.textTel.grid(row = 6, column = 1, sticky = W, padx = 5)

        self.lblSexo = Label(LeftFrame1, font=('arial 12 bold'), text = "Sexo :", bd = 7)
        self.lblSexo.grid(row = 7, column = 0, sticky = W, padx = 5)
        self.textSexo = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Sexo)
        self.textSexo.grid(row = 7, column = 1, sticky = W, padx = 5)

        self.lblIdade = Label(LeftFrame1, font=('arial 12 bold'), text = "Idade :", bd = 7)
        self.lblIdade.grid(row = 8, column = 0, sticky = W, padx = 5)
        self.textIdade = Entry(LeftFrame1, font=('arial 12 bold'), bd = 5, width = 44, justify = 'left', textvariable = Idade)
        self.textIdade.grid(row = 8, column = 1, sticky = W, padx = 5)
    
    
        #----------------------------------------------------Lista----------------------------------------------------------------------------------------------------- 

        scrollbar = Scrollbar (LeftFrame, orient = VERTICAL)
        scrollbar.pack(side = RIGHT, fill = Y)
        

        listaContatos = Listbox(LeftFrame, width = 62, height = 12, font = ('arial', 12, 'bold'), yscrollcommand = scrollbar.set)
        listaContatos.bind('<<ListboxSelect>>', ContatoRec)
        listaContatos.pack(side = RIGHT, fill = Y)
        scrollbar.config(command = listaContatos.yview)



        #----------------------------------------------Botoes--------------------------------------------------------------------------------------------------------
        self.btnAdiciona = Button(RightFrame1, font=('arial 16 bold'), text = "Adicionar", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = AdicionarContato).grid(row = 0, column = 0, padx = 1)
                
        self.btnExibir = Button(RightFrame1, font=('arial 16 bold'), text = "Exibir", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = Exibisao).grid(row = 1, column = 0, padx = 1)

        self.btnUpdate = Button(RightFrame1, font=('arial 16 bold'), text = "Atualizar", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = atualizarContato).grid(row = 2, column = 0, padx = 1)

        self.btnDeletar = Button(RightFrame1, font=('arial 16 bold'), text = "Deletar", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = Del).grid(row = 3, column = 0, padx = 1)

        self.btnProcurar = Button(RightFrame1, font=('arial 16 bold'), text = "Procurar", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = BuscarContato).grid(row = 4, column = 0, padx = 1)

        self.btnResetar = Button(RightFrame1, font=('arial 16 bold'), text = "Resetar", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = LimparDados).grid(row = 5, column = 0, padx = 1)

        self.btnSair = Button(RightFrame1, font=('arial 16 bold'), text = "Sair", bd = 4, pady = 1, padx = 24, width = 8, 
                        height = 2, command = iExit).grid(row = 6, column = 0, padx = 1)



if __name__ == '__main__':
    tela = Tk()
    application = Agenda(tela)
    tela.mainloop()