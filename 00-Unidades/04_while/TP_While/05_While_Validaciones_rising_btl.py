import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = (self.txt_apellido.get())
        edad = int(self.txt_edad.get())
        if edad < 18 or edad > 90 :
            condicional1 = 0
            while condicional1 == 0 :
                self.txt_edad.delete(0,"end")
                alert("DATO INCORRECTO","El valor de la edad debe estar entre 18 y 90 ambos inclusive")
                edad= int(self.txt_edad.get())
                if edad >17 and edad < 91 :
                    condicional1 = 1
        civil = (self.combobox_tipo.get())
        legajo1 = int(self.txt_legajo.get())
        legajo2 = legajo1//1000

        if legajo1 > 9999 or legajo2 == 0 :
            condicional2 =0
            while condicional2 == 0 :
                self.txt_legajo.delete(0,"end")
                alert("DATO INCORRECTO","El valor del legajo debe ser mayor que 999 y menor que 10000")
                legajo1= int(self.txt_legajo.get())
                legajo2 =legajo1//1000
                if legajo1 >999 and legajo1 < 10000 :
                    condicional2 = 1
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
