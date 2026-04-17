import streamlit as st

st.set_page_config(page_title="Motor de Decisão T.A", page_icon="⚙️")

st.title("⚙️ Motor de Decisão T.A")

problema = st.text_input("Descreva o problema:")

col1, col2, col3 = st.columns(3)
with col1: gravidade = st.number_input("Gravidade", 1, 5, 1)
with col2: urgencia = st.number_input("Urgência", 1, 5, 1)
with col3: tendencia = st.number_input("Tendência", 1, 5, 1)

importancia = st.number_input("Importância", 1, 5, 1)
probabilidade = st.number_input("Probabilidade Risco", 1, 5, 1)
impacto_risco = st.number_input("Impacto Risco", 1, 5, 1)

if st.button("PROCESSAR"):
    gut = gravidade * urgencia * tendencia
    risco = probabilidade * impacto_risco
    
    total = gut + risco
    
    if total >= 120: res, cor = "CRÍTICA", "🔴"
    elif total >= 70: res, cor = "ALTA", "🟠"
    else: res, cor = "MÉDIA/BAIXA", "🟡"
    
    st.header(f"{cor} Prioridade: {res}")
  
