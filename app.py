import streamlit as st
import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import Content, Part
from agente.agent import root_agent
from dotenv import load_dotenv
load_dotenv()

# tudo que precisa persistir fica no session_state
if 'loop' not in st.session_state:
    st.session_state.loop = asyncio.new_event_loop()

if 'runner' not in st.session_state:
    st.session_state.runner = InMemoryRunner(
        agent=root_agent,
        app_name='assistente_de_telecom'
    )

if 'sessao_criada' not in st.session_state:
    async def criar_sessao():
        await st.session_state.runner.session_service.create_session(
            app_name='assistente_de_telecom',
            user_id='usuario',
            session_id='sessao_1'
        )
    st.session_state.loop.run_until_complete(criar_sessao())
    st.session_state.sessao_criada = True

async def chamar_agente(prompt: str):
    mensagem = Content(role="user", parts=[Part(text=prompt)])
    resposta_final = ""
    async for evento in st.session_state.runner.run_async(
        user_id="usuario",
        session_id="sessao_1",
        new_message=mensagem
    ):
        if evento.is_final_response() and evento.content and evento.content.parts:
            resposta_final = evento.content.parts[0].text
    return resposta_final


st.title('Assistente de busca de telecom')

if 'historico' not in st.session_state:
    st.session_state.historico = []
if 'processando' not in st.session_state:
    st.session_state.processando = False

for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

prompt = st.chat_input('como posso te ajudar hoje?', disabled=st.session_state.processando)

if prompt and not st.session_state.processando:
    st.session_state.processando = True
    st.session_state.historico.append({'role': 'user', 'content': prompt})
    st.session_state.prompt_pendente = prompt
    st.rerun()

if st.session_state.processando and 'prompt_pendente' in st.session_state:
    with st.spinner('pensando...'):
        resposta = st.session_state.loop.run_until_complete(
            chamar_agente(st.session_state.prompt_pendente)
        )

    st.session_state.historico.append({'role': 'assistant', 'content': resposta})
    del st.session_state.prompt_pendente
    st.session_state.processando = False
    st.rerun()