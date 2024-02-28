import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre_ganador = " "
        edad_promedio = 0
        total_votos = 0
        nombre_perdedor = " "
        edad_perdedor = 0
        votos_ganador = 0
        votos_perdedor = 0
        condicional = 0
        contador = 0
        control = 0
        continuar = "s"
        while continuar == "s" or continuar == "S" :
            contador = contador + 1
            nombre = prompt("Nombre ","Introduzca el nombre del candidato")
        
            edad = int(prompt("Edad"," Introduzca edad del candidato"))
            while edad < 24 :
                alert("Dato Incorrecto","La edad del candidato debe ser mayor o igual a 25 años")
                edad =int(prompt("Edad","Introduzca edad del candidato"))
                      
            votos = int(prompt("Votos","Introduzca la cantidad de votos"))
            if votos < 0 :
                while votos < 0 :
                    alert("Dato Incorrecto","La cantidad de votos debe ser mayor o igual a cero")
                    votos =int(prompt("Votos","Introduzca la cantidad de votos"))
                    if condicional == 0 :
                        votos_perdedor = votos
                        edad_perdedor = edad
                        condicional = 1 
            else :
                if control == 0 :
                    votos_perdedor = votos
                    edad_perdedor = edad
                    nombre_perdedor = nombre
                    control = 1
                if votos > votos_ganador :
                    nombre_ganador = nombre
                if votos < votos_perdedor :
                    votos_perdedor = votos
                    edad_perdedor = edad
                    nombre_perdedor = nombre

            edad_promedio = edad_promedio + edad
            total_votos = total_votos + votos
            continuar = prompt("Desea continuar","S/N")
                                    

        edad_promedio = edad_promedio/contador
        edad_perdedor = str(edad_perdedor)
        total_votos = str(total_votos)
        edad_promedio = str(edad_promedio)
        alert ("Mayor cantidad de votos", "El ganador es: "+ nombre_ganador )
        alert ("Menos Votos"," EL candidato con menos votos es: "+ nombre_perdedor + " con una edad de: " +edad_perdedor)
        alert ("Promedio","El promedio de edades es de: "+ edad_promedio + " años")
        alert ("Cantidad", "La cantidad total de votos es: "+ total_votos)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
