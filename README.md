# ⏱️ Sincronização em Broadcast de Referência (RBS)  

Este projeto implementa a **Sincronização em Broadcast de Referência (RBS)** usando **Python (Flask)** e **HTML/JavaScript** para exemplificar a sincronização de tempos entre múltiplos dispositivos.

---

## 🚀 Como Funciona o Algoritmo RBS?
O **Reference Broadcast Synchronization (RBS)** é um algoritmo que sincroniza dispositivos **sem precisar de um relógio central**. Em vez de um servidor definir o tempo para os clientes, todos recebem um **sinal de referência** e ajustam seus relógios com base nele. Isso reduz o impacto de atrasos na rede.

🔹 **Passo a Passo:**
1. O servidor recebe uma requisição de sincronização.
2. Ele captura o **tempo de chegada** da requisição.
3. Calcula a **média dos tempos** armazenados.
4. Retorna o **tempo de saída** e a **diferença de tempo** entre a chegada e a resposta.
5. Caso a diferença seja significativa, sugere um ajuste.

Com essa abordagem, os clientes podem verificar a precisão de seus relógios e corrigir possíveis atrasos.

---

## 🛠️ Estrutura do Projeto
```
📁 sincronizacao_rbs
├── 📁 templates        # Arquivos estáticos (imagens)
│   ├── background.png  # Plano de fundo da página
│   ├── icon.png        # Ícone da página
├── 📁 templates        # Arquivo HTML
│   ├── index.html      # Interface principal já com CSS e JavaScript
├── app.py              # Servidor Flask
├── README.md           # Documentação
```

---

## 🔧 Configurando o Projeto
### 1️⃣ **Instalar Dependências**
Certifique-se de ter o Python instalado e execute:
```sh
pip install flask
```

### 2️⃣ **Executar o Servidor**
```sh
python app.py
```

### 3️⃣ **Acessar no Navegador**
Abra **http://localhost:5000** para testar.

---

## 📌 Exemplos de Retorno da API
```json
{
  "mensagem": "Sinal recebido!",
  "tempo_chegada": "14:30:51.838251",
  "tempo_saida": "14:30:51.838251",
  "media_sincronizacao": "0.2483996093",
  "diferenca_tempo": "0.0000000000",
  "ajuste_necessario": false
}
```

---

## 📜 Licença
Este projeto é de uso livre para fins acadêmicos.

---

💡 **Dúvidas? Me chama!** 🚀

