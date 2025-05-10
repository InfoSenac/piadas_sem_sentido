import streamlit as st
import requests
from deep_translator import GoogleTranslator
from streamlit_lottie import st_lottie


@st.cache_data
def obter_resposta():
    api_url = 'https://api.api-ninjas.com/v1/jokes'
    resposta = requests.get(
        api_url, 
        headers={
            'X-Api-Key': st.secrets["API_KEY"]
        }
    )
    return resposta


def retornar_resposta(resposta):
    if resposta.status_code == requests.codes.ok:
        return resposta.json()[0]['joke']
    else:
        return resposta.status_code, resposta.text


def mostrar_resposta():
    idioma = st.radio(
        label='***Escolha um idioma:***',
        options=[
            'Português',
            'Inglês'
        ]
    )

    if idioma == 'Português':
        st.write(GoogleTranslator(
                source='en', 
                target='pt'
            ).translate('## ' + retornar_resposta(obter_resposta())))
    else:
        st.write('## ' + retornar_resposta(obter_resposta()))

    st.button(
    label='Outra Piada', 
    type='primary',
    on_click=st.cache_data.clear
    )

    st_lottie("https://lottie.host/a5fb7cda-05a3-4122-ad45-8552bb141df8/66S5qqrFpl.json")

st.title('Piadas sem sentido')

mostrar_resposta()
