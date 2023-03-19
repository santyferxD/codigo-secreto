import random
import tkinter as tk
# ---------------------------------------------------------------------------------------------------

def generar_codigo():
    codigo = ""
    while len(codigo) < 4:
        digito = str(random.randint(0, 9))
        if digito not in codigo:
            codigo += digito
    return codigo
# ---------------------------------------------------------------------------------------------------

def verificar_codigo(event=None):
    codigo_usuario = entrada_codigo.get()
    if len(codigo_usuario) != 4:
        resultado.set("El código debe tener 4 dígitos")
        return
    elif not codigo_usuario.isdigit():
        resultado.set("El código solo debe contener dígitos")
        return
    elif len(set(codigo_usuario)) < 4:
        resultado.set("Los dígitos no deben repetirse")
        return
    
    
    aciertos = 0
    for i in range(4):
        if codigo_usuario[i] == codigo_secreto[i]:
            aciertos += 1
    
    
    coincidencias = 0
    for digito in codigo_usuario:
        if digito in codigo_secreto:
            coincidencias += 1
    coincidencias -= aciertos
    
    
    if aciertos == 4:
        resultado.set("¡Felicidades, has adivinado el código!")
        historial.insert(0, f"{codigo_usuario}: xxxx")
        entrada_codigo.delete(0, tk.END)
        entrada_codigo.focus()
        return
    else:
        mensaje = "x" * aciertos + "o" * coincidencias + "-" * (4 - aciertos - coincidencias)
        resultado.set(mensaje)
        historial.insert(0, f"{codigo_usuario}: {mensaje}")
        entrada_codigo.delete(0, tk.END)
        entrada_codigo.focus()
# ---------------------------------------------------------------------------------------------------


codigo_secreto = generar_codigo() 

# ---------------------------------------------------------------------------------------------------
ventana = tk.Tk()
ventana.title("Adivina el código")
ventana.geometry("400x500")


etiqueta_instrucciones = tk.Label(ventana, text="Ingresa un código de 4 dígitos sin repetir:")
entrada_codigo = tk.Entry(ventana)
entrada_codigo.bind("<Return>", verificar_codigo)
boton_verificar = tk.Button(ventana, text="Ingresar", command=verificar_codigo)
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_historial = tk.Label(ventana, text="Historial:")
historial = tk.Listbox(ventana, width=50, height=10)


etiqueta_instrucciones.pack()
entrada_codigo.pack()
boton_verificar.pack()
etiqueta_resultado.pack()
etiqueta_historial.pack()
historial.pack()


ventana.mainloop()
