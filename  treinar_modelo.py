from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Carregar dataset Iris
data = load_iris()
X = data.data
y = data.target

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar o modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Salvar o modelo treinado
with open('modelo_previsao.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo treinado e salvo com sucesso!")
