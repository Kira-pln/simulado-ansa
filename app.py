# app.py
# RODAR NO STREAMLIT CLOUD
# pip install streamlit

import streamlit as st
import random

st.set_page_config(
    page_title="Simulado ANSA",
    page_icon="📘",
    layout="centered"
)

# =====================================
# BANCO DE QUESTÕES
# =====================================

def gerar_questoes():
    questoes = []

    temas = [
        "Termodinâmica",
        "Fluidos",
        "Resistência dos Materiais",
        "Dinâmica",
        "Metalurgia",
        "Vibrações",
        "Máquinas de Fluxo",
        "Transferência de Calor",
        "Motores",
        "Corrosão"
    ]

    for i in range(100):
        tema = temas[i % len(temas)]

        questoes.append({
            "pergunta": f"Q{i+1} ({tema}) - Em relação aos conceitos fundamentais, assinale a alternativa correta.",
            "alternativas": [
                "Afirmativa incorreta conceitualmente.",
                "Afirmativa parcialmente correta mas incompleta.",
                "Afirmativa correta com base nos princípios da engenharia.",
                "Afirmativa contraditória às leis físicas.",
                "Afirmativa sem base técnica."
            ],
            "resposta": 2
        })

    return questoes


# =====================================
# ESTADO
# =====================================

if "iniciado" not in st.session_state:
    st.session_state.iniciado = False

if "questoes" not in st.session_state:
    st.session_state.questoes = []

if "indice" not in st.session_state:
    st.session_state.indice = 0

if "acertos" not in st.session_state:
    st.session_state.acertos = 0

if "qtd" not in st.session_state:
    st.session_state.qtd = 0


# =====================================
# INÍCIO
# =====================================

st.title("📘 Simulado ANSA Engenharia Mecânica")

if not st.session_state.iniciado:

    st.subheader("Escolha a prova")

    col1, col2, col3 = st.columns(3)

    if col1.button("20 questões"):
        qtd = 20
    elif col2.button("50 questões"):
        qtd = 50
    elif col3.button("100 questões"):
        qtd = 100
    else:
        qtd = None

    if qtd:
        banco = gerar_questoes()
        st.session_state.questoes = random.sample(banco, qtd)
        st.session_state.qtd = qtd
        st.session_state.indice = 0
        st.session_state.acertos = 0
        st.session_state.iniciado = True
        st.rerun()

# =====================================
# PROVA
# =====================================

else:

    i = st.session_state.indice
    qtd = st.session_state.qtd

    if i < qtd:

        q = st.session_state.questoes[i]

        st.progress((i + 1) / qtd)

        st.subheader(f"Questão {i+1} de {qtd}")
        st.write(q["pergunta"])

        resposta = st.radio(
            "Escolha:",
            q["alternativas"],
            key=f"radio_{i}"
        )

        if st.button("Próxima"):

            marcada = q["alternativas"].index(resposta)

            if marcada == q["resposta"]:
                st.session_state.acertos += 1

            st.session_state.indice += 1
            st.rerun()

    else:

        acertos = st.session_state.acertos
        perc = (acertos / qtd) * 100

        st.success("Prova finalizada!")

        st.subheader("Resultado Final")
        st.write(f"**Acertos:** {acertos}/{qtd}")
        st.write(f"**Percentual:** {perc:.1f}%")

        if perc >= 80:
            st.write("🏆 Excelente desempenho")
        elif perc >= 60:
            st.write("✅ Bom desempenho")
        else:
            st.write("📚 Precisa melhorar")

        if st.button("Refazer Prova"):
            st.session_state.iniciado = False
            st.rerun()
