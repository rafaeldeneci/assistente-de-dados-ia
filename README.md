# assistente-dados-ia


● Agente de IA para consulta de dados de clientes de telecom em linguagem natural, desenvolvido com   
  Google ADK, Gemini e Streamlit.


● Acesse o app: [assistente-de-dados-ia.streamlit.app](https://assistente-de-dados-ia.streamlit.app/)


● tecnologias utilizadas:

- Python
- Google ADK
- Gemini
- Streamlit
- SQLite

● como rodar localmente:

1 - Clone o repositório

2 - Instale as dependências: `pip install -r requirements.txt`

3 - Crie um `.env` com sua chave: `GOOGLE_API_KEY=sua_chave`

4 - Gere o banco de dados: `python main.py`

5 - Rode o app: `streamlit run app.py`


● ideia do projeto:

Agente de IA que responde perguntas de maneira humana e natural sobre uma base de clientes de telecom. Ao invés de filtrar dados manualmente no sistema, você pergunta ao agente "clientes ativos em São Gonçalo" o agente consulta o banco de dados e responde.


● Sobre o projeto

No projeto foi utilizado Google ADK para a criação do agente, Gemini como modelo
de linguagem e Streamlit para a interface. Os dados ficam num banco SQLite local com
100 clientes fictícios gerados por script, cobrindo cidades, planos e status variados.

● O contexto de telecom foi escolhido propositalmente, já que a IPNET by Vivo atua no ecossistema da  maior telecom do país.