import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import data

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
    st.write("O projeto utilizando a plataforma Stilingue, onde coleta comentários e utiliza o GPT para classificar esses comentários em temas e tags predefinidos. O objetivo principal é avaliar o desempenho do GPT em comparação com a análise feita por um analista humano, medindo a precisão e eficiência da ferramenta automatizada em relação ao trabalho manual de um profissional. Isso ajuda a entender o potencial de automação no processo de categorização de dados de redes sociais e outros meios.")
    st.write("Para a realização da análise, foram utilizados 192 comentários de redes sociais relacionados à marca Brahma. A árvore de tags conta com 21 temas disponíveis para a classificação dos comentários e 190 tags.")


col1, col2 = st.columns([1,4])
with col1:
    escolha = st.selectbox("Selecione a IA", ("GPT-4o", "Gemini-Pro"))

#Gráfico de pizza
col1, col2 = st.columns(2)
with col1:
    # Dados de exemplo
    labels = ['Não Utilizados', 'Utilizados']
    if escolha == "GPT-4o":
        values = [2, 19]
    else:
        values = [4, 17]

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
    labels = ['Não Utilizadas', 'Utilizadas']
    if escolha == "GPT-4o":
        values = [132, 58]
    else:
        values = [149, 41]

    # Criando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    fig.update_traces(marker=dict(colors=['gold', 'lightgreen'], 
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



# Gráfico de barras
redes = ["Instagram", "Twitter", "Facebook", "Youtube", "Portais"]
totais = [132, 28, 19, 11, 2]

# Criar gráfico interativo de barras
fig = go.Figure([go.Bar(x=redes, y=totais, marker=dict(cornerradius=30))])

# Título e rótulos
fig.update_layout(
    title='De quais redes sociais foram coletados os comentários?',
    xaxis_title='',
    yaxis_title='',
    template='plotly_white'

)

st.plotly_chart(fig)



#Acuracy
st.write("## Acuracidade")
metodos = ['Analista Humano', 'GPT-4o', 'Gemini-Pro']
acuracidade = [100, 42, 55]  # 100% para o analista humano e 40% para o GPT

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
    A análise comparativa entre o desempenho do GPT e de um analista humano revelou importantes insights sobre o potencial de automação no processo de categorização de comentários em redes sociais. Com base nos 192 comentários de redes sociais relacionados à marca Brahma e utilizando 21 temas e 190 tags para classificação, verificamos que o GPT-4o alcançou uma acuracidade de 42%, enquanto o modelo Gemini-Pro obteve 55%, ambos significativamente abaixo da precisão atingida pelo analista humano (100%).

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
