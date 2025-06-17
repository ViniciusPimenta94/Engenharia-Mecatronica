# Trabalho de Conclusão de Curso de Engenharia Mecatrônica — Coleta e Visualização de Dados

Este projeto é dividido em duas partes principais:
1. **Coleta de dados com Arduino via porta serial**.
2. **Visualização dos dados simulados em um mapa de calor com Python e Seaborn**.

---

## 📦 Estrutura do Projeto

- `Arduino.py`: Script que realiza conexão com o Arduino pela porta COM3, lê os dados via `serial`, imprime em tempo real e salva em um arquivo `.txt`.
- `heatmap.py`: Gera um mapa de calor com dados simulados de sensores, usando `numpy` e `seaborn`.

---

## 🛠 Requisitos

- Python 3.x
- Arduino conectado via porta `COM3`
- Bibliotecas:
  - `pyserial`
  - `numpy`
  - `seaborn`
  - `matplotlib`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

### 🔌 1. Coleta de Dados

Conecte o Arduino e execute:

```bash
python Arduino.py
```

- Os dados serão exibidos no console e salvos em `Dados Arduíno.txt`.

### 🌡 2. Mapa de Calor (Visualização)

Execute:

```bash
python heatmap.py
```

- Um mapa de calor será gerado com valores simulados para teste.

---

## ⚠️ Observações

- O código assume que o Arduino está na porta `COM3`. Ajuste conforme necessário.
- O script `heatmap.py` usa dados aleatórios apenas como demonstração. Você pode adaptar para usar os dados reais coletados.

---

## 📄 Licença

MIT
