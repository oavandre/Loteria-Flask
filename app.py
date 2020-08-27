import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('model_mega2.pkl', 'rb'))


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    numeros_desenas = [int(x) for x in request.form.values()]
    final_prev = [np.array(numeros_desenas)]
    resultado = model.predict(final_prev)

    valida_duplicado= len(numeros_desenas) != len(set(numeros_desenas))


    if valida_duplicado :
        return render_template('index.html', mensagem_probabilidade='Não pode repetir Numero')
    else:
        return render_template('index.html', mensagem_probabilidade='Probabilidade de ganhar:  {} %'.format(resultado))




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
