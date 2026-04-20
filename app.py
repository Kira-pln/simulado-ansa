import streamlit as st
import random

st.set_page_config(page_title="Simulado ANSA", layout="centered")

# QUESTÕES REAIS
questoes = [
{
"pergunta":"A frequência natural de um sistema massa-mola depende principalmente de:",
"opcoes":["A massa e da rigidez","Somente da massa","Somente do amortecimento","Temperatura","Pressão"],
"resposta":0
},
{
"pergunta":"Na equação de Bernoulli, considera-se conservação de:",
"opcoes":["Carga elétrica","Energia mecânica","Calor","Entropia","Massa específica"],
"resposta":1
},
{
"pergunta":"No ciclo Otto ideal, a adição de calor ocorre a:",
"opcoes":["Volume constante","Pressão constante","Temperatura constante","Entropia constante","Vazão constante"],
"resposta":0
},
{
"pergunta":"Em uma bomba centrífuga, o componente que transfere energia ao fluido é:",
"opcoes":["Rotor","Filtro","Mancal","Base","Parafuso"],
"resposta":0
},
{
"pergunta":"A corrosão galvânica ocorre entre metais:",
"opcoes":["Iguais","Nobres","Diferentes em meio eletrolítico","Temperados","Puros"],
"resposta":2
}
]

if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.acertos = 0
    random.shuffle(questoes)
    st.session_state.questoes = questoes

qtd = len(st.session_state.questoes)
i = st.session_state.indice

if i < qtd:

    q = st.session_state.questoes[i]

    st.title("📘 Simulado ANSA")
    st.progress((i+1)/qtd)
    st.subheader(f"Questão {i+1} de {qtd}")

    st.write(q["pergunta"])

    resposta = st.radio(
        "Escolha uma alternativa:",
        ["A) "+q["opcoes"][0],
         "B) "+q["opcoes"][1],
         "C) "+q["opcoes"][2],
         "D) "+q["opcoes"][3],
         "E) "+q["opcoes"][4]]
    )

    if st.button("Próxima"):

        marcada = ["A","B","C","D","E"].index(resposta[0])

        if marcada == q["resposta"]:
            st.session_state.acertos += 1

        st.session_state.indice += 1
        st.rerun()

else:

    nota = (st.session_state.acertos/qtd)*100

    st.title("Resultado Final")
    st.write(f"Acertos: {st.session_state.acertos}/{qtd}")
    st.write(f"Nota: {nota:.1f}%")

    if st.button("Refazer"):
        st.session_state.indice = 0
        st.session_state.acertos = 0
        random.shuffle(questoes)
        st.session_state.questoes = questoes
        st.rerun()
