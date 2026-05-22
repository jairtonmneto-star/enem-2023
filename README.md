#Analise de Dados do enem de 2023 
Dashboard interativo com análise de 2,6 milhões de participantes do ENEM 2023.
Aonde p1 analiso os dados e limpo a base de dados para o dahsboard eu pegar os dados e ver as informacoes que necessito 
## Principais Insights
- SP lidera com média 544 pontos, MA tem a menor média com 483
- Escola privada tem média 82 pontos acima da pública
- Diferença de 145 pontos entre menor e maior renda familiar

## Tecnologias
Python, Pandas, Streamlit, Plotly

## Como rodar
```bash
pip install pandas streamlit plotly
streamlit run dahsboard_enem.py
```

## Como obter os dados

1. Acesse: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
2. Baixe os microdados do ENEM 2023
3. Extraia o CSV para a mesma pasta do projeto
4. Renomeie para `MICRODADOS_ENEM_2023.csv`
5. Execute: `streamlit run dahsboard_enem.py`
