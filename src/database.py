import json
import random
from pathlib import Path

def carregar_previsoes():
    """Carrega todas as previsões do arquivo JSON"""
    data_path = Path(__file__).parent.parent / 'data' / 'previsoes.json'
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def obter_previsao():
    """Seleciona uma previsão aleatória de qualquer categoria"""
    previsoes = carregar_previsoes()
    todas = [item for sublist in previsoes.values() for item in sublist]
    return random.choice(todas)