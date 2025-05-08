import streamlit as st
from src.config import aplicar_estilos
from src.database import obter_previsao
from src.helpers import efeito_maquina_escrever, formatar_texto
import time  
from src.ascii_art import TITULO, MAGO

# Configuração inicial da página
st.set_page_config(
    page_title="Vidente do Passado",
    page_icon="🔮",
    layout="centered"
)
aplicar_estilos()

def animar_mago():
    """Exibe animação do mago"""
    
    placeholder = st.empty()
    
    for _ in range(6):  # Repete a animação 
        for frame in MAGO:
            placeholder.markdown(f"```\n{frame}```")
            time.sleep(0.1)
    
    placeholder.empty()

# Gerenciamento de estado
if 'previsao' not in st.session_state:
    st.session_state.previsao = None

# Interface principal
st.markdown(f"<div class='terminal'>{TITULO}</div>", unsafe_allow_html=True)
st.markdown("<div class='destaque'>Prevendo o passado, porque o futuro é muito fácil</div>", 
          unsafe_allow_html=True)

st.markdown("<div class='destaque'>Sente-se... respire... suas verdades serão reveladas</div>", 
          unsafe_allow_html=True)

# Campo de nome
nome = st.text_input("", placeholder="Digite seu nome (opcional)", key="nome_input")

# Botão principal
if st.button("Revelar Verdade Oculta"):
    with st.spinner("Acessando os registros akáshicos..."):
        animar_mago()
        
        # Obtém e personaliza a previsão
        previsao = obter_previsao()
        if nome:
            previsao = previsao.replace("Você", nome)
        
        
        st.session_state.previsao = formatar_texto(previsao)

# Exibe a previsão
if st.session_state.previsao:
    efeito_maquina_escrever(st.session_state.previsao)
    