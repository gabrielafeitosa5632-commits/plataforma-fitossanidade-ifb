import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

# 1. Configuração da Página
st.set_page_config(page_title="Plataforma Fitossanitária", layout="wide")

# 2. Título e Texto de Apresentação
st.title("🌱 Plataforma para Avaliação e Quantificação de Doenças Fitossanitárias")

st.info("""
**Apresentação:**
Olá, somos estudantes do 8º período do curso de Agronomia do Instituto Federal de Brasília (IFB), Campus Planaltina. 
Sob a orientação do professor **Nilton Nélio Cometti**, desenvolvemos esta plataforma utilizando interface em Python, 
com o objetivo de demonstrar sua aplicabilidade em diferentes culturas agrícolas.
""")

st.markdown("---")

# 3. Seção das Pesquisadoras (Fotos mais juntas)
# Criamos 5 colunas e usamos as do meio (2 e 4) para as fotos ficarem centralizadas e próximas
_, col_foto1, _, col_foto2, _ = st.columns([1, 2, 0.5, 2, 1])

with col_foto1:
    try:
        img1 = Image.open("foto 1.jpg")
        st.image(img1, caption="Gabriela Feitosa", use_container_width=True)
    except:
        st.error("Arquivo 'foto 1.jpg' não encontrado.")

with col_foto2:
    try:
        img2 = Image.open("foto2.jpeg")
        st.image(img2, caption="Fabiula Máximo", use_container_width=True)
    except:
        st.error("Arquivo 'foto2.jpeg' não encontrado.")

st.markdown("---")

# 4. Base de Dados (Severidade conforme fornecido)
dados_milho = pd.DataFrame({
    'Amostra': ['img1', 'img2', 'img3', 'img4', 'img5'],
    'Saudável (%)': [21.36, 60.26, 55.82, 23.73, 44.08],
    'Sintomático (%)': [78.63, 39.73, 44.17, 76.26, 55.91]
})

dados_batata = pd.DataFrame({
    'Amostra': ['img1', 'img2', 'img3', 'img4', 'img5'],
    'Saudável (%)': [12.42, 96.81, 50.93, 62.71, 8.75],
    'Sintomático (%)': [87.57, 3.18, 49.06, 37.28, 91.24]
})

dados_cafe = pd.DataFrame({
    'Amostra': ['img1', 'img2', 'img3', 'img4', 'img5'],
    'Saudável (%)': [91.38, 74.59, 48.12, 63.88, 29.76],
    'Sintomático (%)': [8.61, 25.40, 51.87, 36.11, 70.23]
})

# 5. Funções de Visualização
def mostrar_analise(df, titulo_cultura):
    st.header(f"Análise: {titulo_cultura}")
    c_tab, c_graf = st.columns([1, 2])
    
    with c_tab:
        st.write("**Dados Quantitativos**")
        st.dataframe(df, hide_index=True)
    
    with c_graf:
        st.write("**Proporção de Severidade**")
        fig, ax = plt.subplots(figsize=(8, 4))
        df.set_index('Amostra').plot(kind='bar', stacked=True, ax=ax, color=['#2ecc71', '#e74c3c'])
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)
    
    col_b, col_h = st.columns(2)
    with col_b:
        st.write("**Distribuição (Boxplot)**")
        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df[['Saudável (%)', 'Sintomático (%)']], palette="Set2", ax=ax2)
        st.pyplot(fig2)
    with col_h:
        st.write("**Mapa de Calor**")
        fig3, ax3 = plt.subplots()
        sns.heatmap(df[['Saudável (%)', 'Sintomático (%)']], annot=True, cmap="YlOrRd", ax=ax3)
        st.pyplot(fig3)

# Abas por cultura
tab1, tab2, tab3 = st.tabs(["🌽 Milho", "🥔 Batata", "☕ Café"])
with tab1: mostrar_analise(dados_milho, "Ferrugem do Milho")
with tab2: mostrar_analise(dados_batata, "Requeima da Batata")
with tab3: mostrar_analise(dados_cafe, "Bicho Mineiro do Café")

# 6. Banco de Imagens
st.markdown("---")
st.header("🖼️ Banco de Imagens Analisadas")
# Filtra arquivos que começam com 'amostra' na pasta
fotos_amostra = [f for f in os.listdir('.') if f.lower().startswith('amostra')]

if fotos_amostra:
    col_img = st.columns(4)
    for i, nome in enumerate(fotos_amostra):
        with col_img[i % 4]:
            st.image(nome, caption=nome, use_container_width=True)
else:
    st.warning("Nenhuma imagem com nome iniciado em 'amostra' foi encontrada na pasta.")