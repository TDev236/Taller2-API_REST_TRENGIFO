from flask import Flask, jsonify, render_template

app = Flask(__name__)

#Aqui definimos las clases de los animales

class Gato:
    def hacer_sonido(self):
        return "Miau"

class Perro:
    def hacer_sonido(self):
        return "Guau"
    
class Huron:
    def hacer_sonido(self):
        return "Ñiaa"

class BoaConstrictor:
    def hacer_sonido(self):
        return "Sssss"
    

#Rutas de la API

@app.route("/sonido/gato", methods=["GET"])
def sonido_gato():
    gato = Gato()
    return jsonify({"animal": "Gato", "sonido": gato.hacer_sonido()})

@app.route("/sonido/perro", methods=["GET"])
def sonido_perro():
    perro = Perro()
    return jsonify({"animal": "Perro", "sonido": perro.hacer_sonido()})

@app.route("/sonido/huron", methods=["GET"])
def sonido_huron():
    huron = Huron()
    return jsonify({"animal": "Huron", "sonido": huron.hacer_sonido()})

@app.route("/sonido/boa", methods=["GET"])
def sonido_boa():
    boa = BoaConstrictor()
    return jsonify({"animal": "Boa Constrictor", "sonido": boa.hacer_sonido()})

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)