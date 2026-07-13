from flask import Flask, render_template, request
#Esta linea permite usar flask y acceder a los templates donde esta el html de la aplicación
app = Flask(__name__) #en flaks se usa esta line por definicion para una app

gastos = [] # lista vacia a la cual se van agregando las cosas

# Funciones: Las funciones que necesita la app para funcionar
def agregar_gasto(gastos, descripcion, monto):
    nuevo_gasto = {
        "descripcion": descripcion,
        "monto": monto
    }

    #

    gastos.append(nuevo_gasto)

def calcular_total(gastos):
    total = 0
    for gasto in gastos:
        total += gasto["monto"]
    return total

# ____________________________________________

@app.route("/") #al entrar a la pagina se ejecuta el siguiente codigo de abajo
def menu():
    return render_template("menu.html") #entra la carpeta templates abuscar el html del menu

#html no me deja aclarar lo que hace cada linea de codigo

@app.route("/agregar", methods=["GET", "POST"]) #detecta que presionamos el boton agregar y nos envia a esa pagina
def agregar():

    if request.method == "POST":
        descripcion = request.form["descripcion"]
        monto = int(request.form["monto"])

        agregar_gasto(gastos, descripcion, monto)

    return render_template("agregar.html") #Aparece el formulario para agregar el gasto

@app.route("/gastos")
def ver_gastos():

    total = calcular_total(gastos)

    return render_template(
        "gastos.html",
        gastos=gastos,
        total=total
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    #La ia me dijo que es importante agregar esta linea si se trabaja con codesandbox, como una verificacion
    #o un codigo de seguridad para que se ejecute bien