from flask import Flask, request, jsonify
import pickle
import numpy as np

# Carregar o modelo
with open('modelo_previsao.pkl', 'rb') as f:
    model = pickle.load(f)

# Inicializar o Flask
app = Flask(__name__)

# Ponto de extremidade para fazer previsões
@app.route('/previsao', methods=['POST'])
def previsao():
    try:
        # Obter os dados da requisição
        data = request.get_json(force=True)
        input_features = np.array(data['features']).reshape(1, -1)

        # Fazer a previsão
        prediction = model.predict(input_features)
        
        return jsonify({'previsao': int(prediction[0])})

    except Exception as e:
        return jsonify({'erro': str(e)})

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
