Dashboard de Dados Acadêmicos

Painel interativo para análise de dados 
Desenvolvido com Python e Streamlit.

## O que o projeto faz
- Mostra total de alunos, ativos, evasões e CR médio
- Gráficos de distribuição por situação, curso e renda
- Filtros por curso e semestre
- Tabela com todos os dados

## Tecnologias utilizadas
- Python 3
- Streamlit
- Pandas
- Plotly
- SQLite

## Executar a dashboard
1. Instale o necessario:
pip install streamlit pandas plotly sqlalchemy
3. Gere os dados aleatorios:
python gerar_dados.py
4. Rode o dashboard:
streamlit run app.py