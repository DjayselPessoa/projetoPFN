from time import sleep
import os
import tkinter as tk


class MainView:

    def mainView(self):
        try:
            print("Inicializado tkinter")
            
            # Pausa por 5 segundos
            sleep(5)

            # Cria uma janela com tkinter
            janela = tk.Tk()
            janela.title("Minha Interface")
            # janela.geometry("250x200")
            janela.rowconfigure(0, weight=1, minsize=100)
            janela.rowconfigure(1, weight=1, minsize=100)
            janela.columnconfigure(0, weight=1, minsize=125)
            janela.columnconfigure(1, weight=1, minsize=125)
            
            # Adiciona um label à janela na linha 0 e coluna 0
            label = tk.Label(janela, text="Olá")
            label.grid(row=0, column=0)
            # Adiciona um botão à janela
            botao = tk.Button(janela, text="Fechar", command=janela.destroy)
            botao.grid(row=1, column=1)
            # botao.pack()

            # Inicia o loop principal da interface
            janela.mainloop()

            # Pausa até pressionar alguma tecla
            os.system("pause")

            print("saindo!")
            return True
        except ValueError as e:
            print("LOG: -> ", e)
        finally:
            pass


ObjMainView = MainView()
