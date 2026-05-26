import streamlit as st
import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import Content, Part
from agente.agent import root_agent
from dotenv import load_dotenv
load_dotenv()


runner = InMemoryRunner(
    agent=root_agent,
    app_name='assistente_de_telecom'
)


async def chamar_agente(prompt: str, session_id: str):
    await runner.session_service.create_session(
    app_name='assistente_de_telecom',
    user_id='usuario',
    session_id=session_id

    )

    mensagem = Content(role="user",parts=[Part(text=prompt)])
    resposta_final=""


    async for evento in runner.run_async(
        user_id="usuario",
        session_id=session_id,
        new_message=mensagem
    ):
       if evento.is_final_response() and evento.content and evento.content.parts:
         resposta_final = evento.content.parts[0].text

    return resposta_final



st.title('assistende de busca telecom')

if 'historico' not in st.session_state:
    st.session_state.historico = []
if 'session_id' not in st.session_state:
    st.session_state.session_id = "sessão_1"

for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

prompt = st.chat_input('como poderia te ajudar hoje?')


if prompt:
    st.session_state.historico.append({'role':'user', 'content':prompt})
    with st.chat_message('user'):
        st.write(prompt)

    resposta = asyncio.run(
        chamar_agente(prompt, st.session_state.session_id)
    )

    st.session_state.historico.append({'role':'assistant', 'content':resposta})
    with st.chat_message('assistant'):
        st.write(resposta)




