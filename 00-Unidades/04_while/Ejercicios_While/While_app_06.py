import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Valeria Andreina
apellido:Gonzalez Perez
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        condicion = 0
        while condicion == 0 :
            numero1 = int(prompt("Primer numero","Introduzca el primer numero"))
            numero2 = int(prompt("Segundo numero","Introduzca el segundo numero"))
            numero3 = int(prompt("Tercer numero","Introduzca el tercer numero"))
            numero4 = int(prompt("Cuarto numero","Introduzca el cuarto numero"))
            numero5 = int(prompt("Quinto numero","Introduzca el quinto numero"))
            condicion = 1
        sumatoria = numero1+numero2+numero3+numero4+numero5
        prom = sumatoria/5
        self.txt_suma_acumulada.delete(0,"end")
        self.txt_suma_acumulada.insert(0,sumatoria)
        self.txt_promedio.delete(0,"end")
        self.txt_promedio.insert(0,prom)
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
