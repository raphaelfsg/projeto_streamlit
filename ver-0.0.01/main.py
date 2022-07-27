import streamlit as st
import Controllers.UserController as UserController
import models.p_team as team

st.title("Project team")

with st.form(key="include_cliente", clear_on_submit=True):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira a sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Selecione a sua profissão", ["Desenvolvedor", "Designer", "Orientador"])
    input_social = st.text_input(label="Insira o endereço de sua rede social")
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    team.p_nome= input_name
    team.p_age = input_age
    team.p_occupation = input_occupation
    team.p_social = input_social

    UserController.incluir(p_team)