import streamlit as st

def aplicar_estilos():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono&family=VT323&display=swap');
        
        :root {
            --cor-primaria: green;
            --cor-secundaria: green;
            --fundo-escuro: black;
            --gradiente-mistico: linear-gradient(
                45deg,
                #51647a 0%,
                #31ada1 50%,
                #59d999 100%
            );
        }
        
        html, body, [class*="css"] {
            font-family: 'VT323', monospace;
            letter-spacing: 2px;
            background: var(--fundo-escuro);
            color: var(--cor-secundaria);
            text-shadow: 0 0 8px var(--cor-secundaria);
        }
        
        .destaque {
            color: var(--cor-primaria) !important;
            animation: glow 2s infinite;
        }
        
        @keyframes glow {
            0% { text-shadow: 0 0 5px var(--cor-primaria); }
            50% { text-shadow: 0 0 20px var(--cor-primaria); }
            100% { text-shadow: 0 0 5px var(--cor-primaria); }
        }
        
        .container-mistico {
            border: 2px solid;
            border-image: var(--gradiente-mistico) 1;
            padding: 20px;
            margin: 20px 0;
            position: relative;
        }
        
        .stButton>button {
            background: var(--gradiente-mistico) !important;
            border: none !important;
            color: #000 !important;
            font-weight: bold;
            transition: transform 0.3s;
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px var(--cor-primaria);
        }
        
        .terminal {
            font-family: 'VT323', monospace !important;
            white-space: pre-wrap;
        }
        .stMarkdown pre {
            background: transparent !important;
            padding: 0 !important;
            margin: 0 !important;
        }    
    </style>
    """, unsafe_allow_html=True)