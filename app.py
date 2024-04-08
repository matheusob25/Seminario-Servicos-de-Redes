from flask import Flask, jsonify
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Modelo de IA simples para demonstração
# Supõe-se que o modelo já foi treinado anteriormente
model = LinearRegression()
model.coef_ = [0.1]  # Exemplo de coeficiente do modelo treinado

@app.route('/balanceamento')
def balanceamento():
    # Lógica de balanceamento de carga com IA
    # Aqui, estamos apenas simulando o uso do modelo treinado para tomar uma decisão
    latencia_desejada = 20  # Latência desejada pelo usuário (exemplo)
    previsao_latencia = model.predict([[latencia_desejada]])
    
    # Lógica de roteamento baseada na previsão de latência
    if previsao_latencia > 0.5:  # Exemplo de limiar de decisão
        conteiner_destino = 'app_container_1'
    else:
        conteiner_destino = 'app_container_2'
    
    return jsonify({'conteiner_destino': conteiner_destino})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
