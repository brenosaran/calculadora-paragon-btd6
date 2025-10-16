import pandas as pd
import numpy as np
import streamlit as st

# Função para calcular o poder baseado no nível
def poder(D):
    if D == 1:
        poder = 0
    elif D >= 2 and D <= 99:
        poder = round((50*D**3 + 5025*D**2 + 168324*D + 843000)/600)
    elif D == 100:
        poder = 200000
    else:
        poder = "Está errado"
    return poder

# Criação de tabela de poder e nível
def criar_tabela():
    poder_lista = []
    nivel = []
    for D in range(1, 101):
        poder_lista.append(poder(D))
    for D in range(1, 101):
        nivel.append(D)
    df = pd.DataFrame({'Nivel': nivel, 'Poder': poder_lista})
    return df

def sacrificio():
    # sacrifice_money = float(input('Coloque o valor do Sacrifício(Slider): '))
    sacrifice_power = (sacrifice_money/sacrifice_div)
    if sacrifice_power >= 60000:
        sacrifice_power = 60000
    else:
        sacrifice_power = sacrifice_power
    return sacrifice_power

def nivel_paragon():
    df = criar_tabela()
    if pops/180 + dinheiro_gerado/45 >= 90000:
        dinheiro_pops = 90000
    else:
        dinheiro_pops = pops/180 + dinheiro_gerado/45
    if tier5*6000 >= 50000:
        tier5_valor = 50000
    else:
        tier5_valor = tier5*6000
    # Cálculo do poder total
    sacrifice_power = sacrificio() + paragon_totem*2000 + dinheiro_pops + upgrades*100 + tier5_valor
    nivel = df[df['Poder'] <= sacrifice_power]['Nivel'].max()
    return int(nivel)

# Parâmetros de limite
sacrifice_money_limit = 60000
pops_limit = 90000
dinheiro_gerado_limit = 90000
tier5_limit = 50000

valores = {
    'Dart Monkey': {
        'Fácil': 127500,
        'Normal': 150000,
        'Difícil': 162000,
        'Extremo': 180000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-ApexPlasmaMaster.png'
    },
    'Boomerang' : {
        'Fácil': 212500,
        'Normal': 250000,
        'Difícil': 270000,
        'Extremo': 300000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\ParagonGlaiveDominus.webp'
    },
    'Bomb': {
        'Fácil': 510000,
        'Normal': 600000,
        'Difícil': 648000,
        'Extremo': 720000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-BallisticObliterationMissileBunker.png'
    },
    'Tack Shooter': {
        'Fácil': 637500,
        'Normal': 750000,
        'Difícil': 810000,
        'Extremo': 900000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-CycloneOfFireAndMetal.png'
    },
    'Monkey Sub': {
        'Fácil': 340000,
        'Normal': 400000,
        'Difícil': 432000,
        'Extremo': 480000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-NauticSiegeCore.png'
    },
    'Buccaneer': {
        'Fácil': 467500,
        'Normal': 550000,
        'Difícil': 594000,
        'Extremo': 660000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-NavarchOfTheSeas.png'
    },
    'Monkey Ace': {
        'Fácil': 765000,
        'Normal': 900000,
        'Difícil': 972000,
        'Extremo': 1080000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-GoliathDoomship.png'
    },
    'Wizard': {
        'Fácil': 680000,
        'Normal': 800000,
        'Difícil': 864000,
        'Extremo': 960000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-MagusPerfectus.png'
    },
    'Ninja': {
        'Fácil': 425000,
        'Normal': 500000,
        'Difícil': 540000,
        'Extremo': 600000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-AscendedShadow.webp'
    },
    'Spike Factory': {
        'Fácil': 637500,
        'Normal': 750000,
        'Difícil': 810000,
        'Extremo': 900000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\SpikeFactoryParagon.png'
    },
    'Engineer': {
        'Fácil': 552500,
        'Normal': 650000,
        'Difícil': 702000,
        'Extremo': 780000,
        'imagem' : 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\Paragon-MasterBuilder.png'
    }
}

imagem_modos = {
    'Fácil': 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\ModeSelectEasyBtn.webp',
    'Normal': 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\ModeSelectMediumBtn.webp',
    'Difícil': 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\ModeSelectHardBtn.webp',
    'Extremo': 'C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\ImpoppableBtn.webp'
}

st.set_page_config(page_title='Calculadora Paragon', page_icon='C:\\Users\\breno\\Documents\\streamlit\\BTD6\\images\\ParagonIcon.webp', layout='wide')
st.title('Calculadora de Nível de Paragon')

# Filtros e inputs do Streamlit
col1, col2 = st.columns(2)
with col1:
    paragon = st.selectbox('Coloque o Paragon:', valores.keys(), format_func=lambda x: x)
with col2:
    modo = st.selectbox('Coloque o Modo:', ['Fácil', 'Normal', 'Difícil', 'Extremo'])

paragon_price = valores[paragon][modo]

sacrifice_div = (paragon_price*1.05)/20000

# Interface do Streamlit
col3, col4, col_divisoria1, col5 = st.columns([10,10,2,10])

with col3:
    sacrifice_money = st.slider('Coloque o valor do Sacrifício (em moedas):', min_value=0, max_value=int(sacrifice_div*sacrifice_money_limit), value=0, step=int(sacrifice_div*paragon_price/100), key='sacrifice_money')
    paragon_totem = st.slider('Coloque a quantidade de Totem Paragon:', min_value=0, max_value=100, value=0, step=1, key='paragon_totem')
    pops = st.slider('Coloque a quantidade de bloons estourados:', min_value=0, max_value=pops_limit*180, value=0, step=180*100, key='pops')
    dinheiro_gerado = st.slider('Coloque o dinheiro gerado (em moedas):', min_value=0, max_value=dinheiro_gerado_limit*45, value=0, step=45*100, key='dinheiro_gerado')

with col4:
    upgrades = st.slider('Coloque a quantidade de Upgrades em torres:', min_value=0, max_value=100, value=0, step=1, key='upgrades')
    tier5 = st.slider('Coloque a quantidade de Torres Tier 5:', min_value=0, max_value=9, value=0, step=1, key='tier5')

with col_divisoria1:
    # Usamos st.markdown com HTML/CSS para criar uma linha vertical centralizada.
    st.markdown("<div style='writing-mode: vertical-rl; text-orientation: mixed; margin: 0 auto; font-size: 20px; color: gray;'>|</div>", unsafe_allow_html=True)

with col5:
    st.markdown(f'''
                ### O nível do seu paragon é: 
                ### **{nivel_paragon()}**
                ''')
    st.image(valores[paragon]['imagem'], width=300)
