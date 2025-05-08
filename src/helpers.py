import time
import streamlit as st
import random
from src.ascii_art import  LISTA_ASCIIS



def formatar_texto(texto, largura=20):

    palavras = texto.split()
    linhas = []
    linha_atual = ''
    
    # Quebra o texto em linhas mantendo palavras inteiras
    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 > largura:
            if linha_atual:
                linhas.append(linha_atual.center(largura))
                linha_atual = ''
            
            # Caso a palavra seja maior que a largura
            if len(palavra) > largura:
                for i in range(0, len(palavra), largura):
                    parte = palavra[i:i+largura]
                    linhas.append(parte.center(largura))
                continue
                
        linha_atual = f"{linha_atual} {palavra}".strip()
    
    if linha_atual:
        linhas.append(linha_atual.center(largura))
    
    # Preenche e limita a 4 linhas
    linhas = linhas[:4]  # Mantém apenas 4 linhas máximas
    while len(linhas) < 4:
        linhas.append(" " * largura)
    
    template_lista = random.choice(LISTA_ASCIIS)
    
    return template_lista.format(
        linha1=linhas[0],
        linha2=linhas[1],
        linha3=linhas[2],
        linha4=linhas[3]
    )

def efeito_maquina_escrever(texto):
    """Simula efeito de digitação"""
    placeholder = st.empty()
    texto_construido = ""
    
    for i, char in enumerate(texto):
        texto_construido += char
        estilo = "font-size: 1.1em;" if i % 2 == 0 else "font-size: 1.1em;"
        placeholder.markdown(
            f"<div class='terminal' style='{estilo}'>{texto_construido}</div>", 
            unsafe_allow_html=True
        )
        time.sleep(0.01)
    
    return texto_construido