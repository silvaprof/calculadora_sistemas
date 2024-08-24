from tkinter import *
from tkinter import ttk



class JanelaPrincipal:

    def __init__(self, janela):
        self.janela = janela
        janela.title("Calculadora de Sistemas")


        #Primeira equacao

        # Cria entrada da variavel a 
        self.a = Entry(janela, width=5)
        self.a.grid(row=2, column=0, padx=10, pady=10)

        #Cria label x
        self.x_1 = Label(janela, text="x")
        self.x_1.grid(row=2, column=1, padx=10, pady=10, sticky='e')


        #Cria label +
        self.plus_1 = Label(janela, text="+")
        self.plus_1.grid(row=2, column=2, padx=10, pady=10, sticky='e')


        # Cria entrada da variavel b
        self.b = Entry(janela, width=5)
        self.b.grid(row=2, column=3, padx=10, pady=10)

        #Cria label y
        self.y_1 = Label(janela, text="y")
        self.y_1.grid(row=2, column=4, padx=10, pady=10, sticky='e')

        #Cria label =
        self.igual_1 = Label(janela, text="=")
        self.igual_1.grid(row=2, column=5, padx=10, pady=10, sticky='e')

        # Cria entrada da variavel c
        self.c = Entry(janela, width=5)
        self.c.grid(row=2, column=6, padx=10, pady=10)






        #Segunda equacao
        
        # Cria entrada da variavel d
        self.d = Entry(janela, width=5)
        self.d.grid(row=3, column=0, padx=10, pady=10)

        #Cria label x
        self.x_2 = Label(janela, text="x")
        self.x_2.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        #Cria label +
        self.plus_2 = Label(janela, text="+")
        self.plus_2.grid(row=3, column=2, padx=10, pady=10, sticky='e')

        # Cria entrada da variavel e
        self.e = Entry(janela, width=5)
        self.e.grid(row=3, column=3, padx=10, pady=10)

        #Cria label y
        self.y_2 = Label(janela, text="y")
        self.y_2.grid(row=3, column=4, padx=10, pady=10, sticky='e')

        #Cria label =
        self.igual_2 = Label(janela, text="=")
        self.igual_2.grid(row=3, column=5, padx=10, pady=10, sticky='e')

        # Cria entrada da variavel f
        self.f = Entry(janela, width=5)
        self.f.grid(row=3, column=6, padx=10, pady=10)






        # Cria um botão para exibir o resultado
        self.botao = Button(janela, text="Calcular", command=self.calcular_resultado)
        self.botao.grid(row=9, column=0, columnspan=2, pady=20)





    def calcular_resultado(self):

        try:        
            #Coleta as variaveis
            a = float(self.a.get())
            b = float(self.b.get())
            c = float(self.c.get())
            d = float(self.d.get())
            e = float(self.e.get())
            f = float(self.f.get())


            #Calcula a incógnita x
            x = self.calc_x(a,b,c,d,e,f)

            y = self.calc_y(a,b,c,d,e,f)

            #Exibe o resultado
            self.exibir_resultado(x, y, a, b, c, d, e, f)
        except ZeroDivisionError:
            self.exibir_erro("Erro: Sistema Impossível ou Indeterminado.")
        except ValueError:
            self.exibir_erro("Erro: Valores inválidos.")



    def exibir_resultado(self, x, y, a, b, c, d, e, f):

        janela_resultado = Toplevel(self.janela)

        janela_resultado.title("Resultado do sistema")



        equacao = f"[{a}] x + [{b}] y = [{c}]\n[{d}] x + [{e}] y = [{f}]"
        resultado_texto = f"O valor de x é {x:.2f} e o valor de y é {y:.2f}"

        # Labels para mostrar a equação e o resultado
        Label(janela_resultado, text="Equações:").pack(pady=5)
        Label(janela_resultado, text=equacao).pack(pady=5)

        Label(janela_resultado, text="Resultado:").pack(pady=5)
        Label(janela_resultado, text=resultado_texto).pack(pady=5)

        # Botão para fechar a nova tela
        Button(janela_resultado, text="Fechar", command=janela_resultado.destroy).pack(pady=10)


    def exibir_erro(self, mensagem):
        erro_janela = Toplevel(self.janela)
        erro_janela.title("Erro")

        Label(erro_janela, text=mensagem).pack(pady=20)
        Button(erro_janela, text="Fechar", command=erro_janela.destroy).pack(pady=10)






    #Funcao para calcular a incógnita x
    def calc_x(self, a, b, c, d, e, f):

        x = (c-(b*((a*f)-(d*c))/((-d*b)+(e*a)))/a)


        return x



    #Funcao para calcular a incognita y
    def calc_y(self,a,b,c,d,e,f):

        y =((a*f)-(d*c))/((-d*b)+(e*a))

        return y




#Rodando aplicacao
root = Tk()
janela = JanelaPrincipal(root)
root.mainloop()

