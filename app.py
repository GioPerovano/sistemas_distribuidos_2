from flask import Flask, render_template, jsonify
import time
from datetime import datetime

app = Flask(__name__)

tempos_chegada = []  # Lista para armazenar os tempos de chegada
diferencas_tempo = []  # Lista para armazenar as diferenças
LIMITE_AJUSTE = 0.1  # Limite para sugerir ajuste (100ms)

def formatar_tempo(timestamp):
    """ Formata o timestamp para exibir HH:MM:SS.ssssssssss (10 casas decimais) """
    dt = datetime.fromtimestamp(timestamp)
    return f"{dt.strftime('%H:%M:%S')}.{dt.microsecond:06d}{int((timestamp % 1) * 1e9) % 1_000_000:09d}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sync', methods=['GET'])
def sincronizar():
    tempo_chegada = time.time()  # Captura o tempo de chegada
    tempos_chegada.append(tempo_chegada)

    time.sleep(0.000000000000000000000000000000000000000001)

    tempo_saida = time.time()  # Captura o tempo de saída

    # Calcula a diferença real entre tempo de chegada e saída
    diferenca = tempo_saida - tempo_chegada
    diferencas_tempo.append(diferenca)

    # Calcula a média das diferenças registradas
    media_sincronizacao = sum(diferencas_tempo) / len(diferencas_tempo) if diferencas_tempo else 0

    # Verifica se o ajuste é necessário
    ajuste_necessario = diferenca > LIMITE_AJUSTE

    return jsonify({
        "mensagem": "Sinal recebido!",
        "tempo_chegada": formatar_tempo(tempo_chegada),
        "tempo_saida": formatar_tempo(tempo_saida),
        "media_sincronizacao": f"{media_sincronizacao:.10f}",
        "diferenca_tempo": f"{diferenca:.10f}",
        "ajuste_necessario": ajuste_necessario,
        "tempo_sugerido": formatar_tempo(tempo_chegada + media_sincronizacao) if ajuste_necessario else None
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
