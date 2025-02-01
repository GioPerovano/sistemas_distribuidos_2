from flask import Flask, render_template, jsonify
import time
from datetime import datetime

app = Flask(__name__)

tempos = []  # Lista para armazenar os tempos de chegada
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
    tempo_chegada = time.time()  # Captura o tempo exato de chegada com alta precisão
    tempos.append(tempo_chegada)

    # Cálculo da média: diferença entre os tempos consecutivos
    if len(tempos) > 1:
        diferencas = [tempos[i] - tempos[i - 1] for i in range(1, len(tempos))]
        media_sincronizacao = sum(diferencas) / len(diferencas)
    else:
        media_sincronizacao = 0  # Primeira sincronização, sem referência

    tempo_saida = time.time()  # Tempo de saída ao responder

    # Verifica se o ajuste é necessário
    diferenca = abs(tempo_chegada - tempo_saida)
    ajuste_necessario = diferenca > LIMITE_AJUSTE

    return jsonify({
        "mensagem": "Sinal recebido!",
        "tempo_chegada": formatar_tempo(tempo_chegada),
        "tempo_saida": formatar_tempo(tempo_saida),
        "media_sincronizacao": f"{media_sincronizacao:.10f}",
        "diferenca_tempo": f"{diferenca:.10f}",  # Diferença com 10 casas decimais
        "ajuste_necessario": ajuste_necessario,
        "tempo_sugerido": formatar_tempo(tempo_chegada + media_sincronizacao) if ajuste_necessario else None
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
