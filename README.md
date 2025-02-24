# previsao-modelo
modelo de previsão com seus devidos pontos de extremidade configurados.


# Modelo de Previsão com API Flask

## Passo a Passo

### 1. Criando o Repositório:
- Criamos um novo repositório no GitHub chamado `previsao-modelo`.

### 2. Treinando o Modelo:
- Utilizamos o dataset **Iris** do scikit-learn e treinamos um modelo de **RandomForestClassifier**.
- O modelo foi salvo em um arquivo `modelo_previsao.pkl`.

### 3. Criando a API com Flask:
- Utilizamos Flask para criar um ponto de extremidade `/previsao` que aceita uma requisição **POST** com dados para fazer previsões.

### 4. Executando a API:
- Para rodar a API localmente, execute o comando:
  ```bash
  python app.py
  ```
- A API estará disponível em `http://127.0.0.1:5000`.

### 5. Realizando uma Requisição:
- Para realizar uma previsão, envie uma requisição **POST** para o ponto de extremidade `/previsao` com um corpo JSON contendo as características:
  ```json
  {
    "features": [5.1, 3.5, 1.4, 0.2]
  }
  ```
  A resposta será algo assim:
  ```json
  {
    "previsao": 0
  }
  ```

## Arquivos:
- `modelo_previsao.pkl`: Modelo treinado e salvo.
- `app.py`: Código da API Flask com o ponto de extremidade `/previsao`.
- `README.md`: Instruções sobre como executar o projeto.
