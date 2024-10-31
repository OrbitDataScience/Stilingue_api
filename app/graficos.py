import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import data
import plotly.express as px

st.set_page_config(page_title="Análise IA Stilingue", page_icon=":bar_chart:", layout="wide")

st.markdown(
    """
    <style>
        header {
            display: none!important;
        }
        .st-emotion-cache-1jicfl2 {
            padding: 3rem 5rem 3rem;
        }
        h1 {
            text-decoration: underline;
        }
        h3 {
            margin-top:20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)

with col1:
    st.write("# Análise IA Stilingue")


with col2:
    st.write("### Resumo do estudo")
    st.write("O projeto utilizando a plataforma Stilingue, onde coleta comentários e utiliza o GPT para classificar esses comentários em temas e tags predefinidos. O objetivo principal é avaliar o desempenho da IA em comparação com a análise feita por um analista humano, medindo a precisão e eficiência da ferramenta automatizada em relação ao trabalho manual de um profissional. Isso ajuda a entender o potencial de automação no processo de categorização de dados de redes sociais e outros meios.")
    st.write("Para a realização da análise, foram utilizados 146 comentários de redes sociais relacionados à marca Guaraná. A árvore de tags conta com 21 temas disponíveis para a classificação dos comentários e 190 tags.")


col1, col2 = st.columns([1,4])
with col1:
    escolha = st.selectbox("Selecione a IA", ("GPT-4o", "Gemini-Pro", "Analista Humano"))

#Gráfico de pizza
col1, col2 = st.columns(2)
with col1:
    # Dados de exemplo
    labels = ['Não Utilizados', 'Utilizados']
    if escolha == "GPT-4o":
        values = [7, 14]
    elif escolha == "Gemini-Pro":
        values = [9, 12]
    else:
        values = [12, 9]

    # Criando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    fig.update_traces(marker=dict(colors=['gold', 'lightgreen'], 
                              line=dict(color='#000000', width=2)))

    fig.update_layout(title='Temas Disponíveis x Utilizados')
    
    fig.update_layout(legend=dict(
        orientation='v',
        y=1,
        xanchor='right',
        x=0
    ))
    # Mostrando o gráfico
    st.plotly_chart(fig)
    

with col2:
     # Dados de exemplo
    labels = ['Utilizadas', 'Não Utilizadas']
    if escolha == "GPT-4o":
        values = [30, 160]
    elif escolha == "Gemini-Pro":
        values = [29, 161]
    else:
        values = [35, 155]

    # Criando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    fig.update_traces(marker=dict(colors=['lightgreen','gold'], 
                              line=dict(color='#000000', width=2)))

    fig.update_layout(title='Tags Disponíveis x Utilizadas')
    
    fig.update_layout(legend=dict(
        orientation='v',
        y=1,
        xanchor='right',
        x=1
    ))
    # Mostrando o gráfico
    st.plotly_chart(fig)


if escolha == "GPT-4o":

    df_tags = pd.DataFrame(columns=['Redes Sociais', 'Quantidade de acertos', 'Quantidade de erros'])
    df_tags.loc[0] = ['Instagram', 6, 13]
    df_tags.loc[1] = ['Facebook', 4, 9]
    df_tags.loc[2] = ['Twitter', 18, 32]
    df_tags.loc[3] = ['Youtube', 1, 2]
    df_tags.loc[4] = ['TikTok', 19, 28]
    df_tags.loc[5] = ['Bluesky', 4, 10]

    

elif escolha == "Gemini-Pro":

    df_tags = pd.DataFrame(columns=['Redes Sociais', 'Quantidade de acertos', 'Quantidade de erros'])
    df_tags.loc[0] = ['Instagram', 4, 13]
    df_tags.loc[1] = ['Facebook', 5, 10]
    df_tags.loc[2] = ['Twitter', 20, 33]
    df_tags.loc[3] = ['Youtube', 0, 2]
    df_tags.loc[4] = ['TikTok', 19, 27]
    df_tags.loc[5] = ['Bluesky', 6, 7]

else:
    df_tags = pd.DataFrame(columns=['Redes Sociais', 'Quantidade de acertos', 'Quantidade de erros'])
    df_tags.loc[0] = ['Instagram', 17, 0]
    df_tags.loc[1] = ['Facebook', 15, 0]
    df_tags.loc[2] = ['Twitter', 53, 0]
    df_tags.loc[3] = ['Youtube', 2, 0]
    df_tags.loc[4] = ['TikTok', 46, 0]
    df_tags.loc[5] = ['Bluesky', 13, 0]


fig2 = go.Figure(
        data=[
            go.Bar(x=df_tags['Redes Sociais'], y=df_tags['Quantidade de acertos'], name="Acertos"),
            go.Bar(x=df_tags['Redes Sociais'], y=df_tags['Quantidade de erros'], name="Erros"),
        ],
        layout=dict(
            barcornerradius=15,
            title='Quantidade de acertos e erros por rede social [Tags]',
            colorway=['#90EE90','#FFD700'],
        ),
    )

st.plotly_chart(fig2)
#Principais acertos
#EXP - Situação de consumo
#EXP - Desejo de consumo
#COMP - Comparação de concorrente


#principal erro
#LIQ - Sabor
#LIQ - Qualidade genérica

col1,col2,col3 = st.columns([1,2,1])
with col2:
    # TABELA
    fig = go.Figure(data=[go.Table(
        header=dict(values=['<b>Tags</b>', '<b>Acertos</b>', '<b>Erros</b>'],
                    line_color='darkslategray',
                    fill_color='black',
                    align='left',
                    font=dict(color='white', size=16)               
        ),
        cells=dict(values=[['EXP - Desejo de consumo', 'EXP - Situação de consumo', 'COMP - Comparação de concorrente', 'HMA - Outras bebidas'], # 1st column
                        [24, 7, 15, 0],
                        [5, 16, 3, 25]                      
                        ],
                line_color='darkslategray',
                fill_color='black',
                align='left',
                font=dict(size=15),
                height=30
        ),
                columnwidth = [150, 50, 50],
    )])

    fig.update_layout(width=900, height=400, title='Tabela de acertos e erros das principais tags')

    st.plotly_chart(fig)

#Acuracy
st.write("## Acuracidade")
metodos = ['Analista Humano', 'GPT-4o', 'Gemini-Pro']
acuracidade = [100, 33, 37]  # 100% para o analista humano e 40% para o GPT

# Criar gráfico interativo de barras
fig = go.Figure([go.Bar(x=metodos, y=acuracidade, text=acuracidade, textposition='auto', marker_color=['white', 'green', 'blue'])])

# Título e rótulos
fig.update_layout(
    title='Comparação de Acuracidade: Analista Humano vs IAs',
    xaxis_title='',
    yaxis_title='Acuracidade (%)',
    template='plotly_white'
)

# Exibir gráfico com Streamlit
st.plotly_chart(fig)


col1, col2 = st.columns(2)
with col1:
    #Conclusão
    st.write("## Conclusão do estudo")    
    st.write("""
    A análise comparativa entre o desempenho do GPT e de um analista humano revelou importantes insights sobre o potencial de automação no processo de categorização de comentários em redes sociais. Com base nos 146 comentários de redes sociais relacionados à marca Guaraná e utilizando 21 temas e 190 tags para classificação, verificamos que o GPT-4o alcançou uma acuracidade de 33%, enquanto o modelo Gemini-Pro obteve 37%, ambos significativamente abaixo da precisão atingida pelo analista humano (100%).

    Esses resultados indicam que, embora a IA seja promissora para tarefas de categorização, ela ainda apresenta limitações em termos de precisão quando comparada ao trabalho manual de um profissional especializado. A análise também sugere que, no atual estágio de desenvolvimento, a utilização de IA como suporte no processo de categorização pode ser benéfica, porém, a supervisão humana é essencial para garantir a qualidade e confiabilidade das classificações.

    O estudo aponta para a necessidade de melhorias nos modelos de IA, bem como para a possibilidade de integrar soluções híbridas, onde a IA auxilie na redução do tempo de categorização, enquanto o controle de qualidade permaneça sob a responsabilidade de um analista humano. Essa abordagem otimizada pode contribuir para aumentar a eficiência e a escalabilidade do processo, sem comprometer a precisão necessária para a análise de dados em redes sociais.
    """)

with col2:
    st.write("## Problemas encontrados")  
    st.write("""
    Os problemas encontrados na extração de comentários via API da Stilingue foram:
    - A base de comentários vem 'suja', com muitos comentários repetidos e sem relevância para a análise.
    - Dificuldade de utilização dos filtros disponíveis na plataforma.

    Os problemas encontrados na classificação de comentários com IA foram:
    - Limitação no tamanho do prompt.
    - Dificuldade de compreensão do contexto de alguns comentários.
    """)
