import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="AutoCadastro PRO",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "carros.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1492144534655-ae79c964c9d7"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_FROTA = (
    "https://images.unsplash.com/"
    "photo-1502877338535-766e1452684a"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F0F0E5 0%,
            #E1E4C8 50%,
            #D4DCB5 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #162630,
            #223944
        );

    border-right:
        2px solid #77864B;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #BFCB9C !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #26311F !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #46513B !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(14,28,38,0.97) 0%,
            rgba(14,28,38,0.86) 45%,
            rgba(14,28,38,0.18) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #A4D080 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #E8EDDE !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #6E8040;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(111,128,63,0.30);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #26311F !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #566248 !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #152631,
            #233C48
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #E2E9DA !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.85);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #B8C391;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}


/* =========================================================
LABELS DOS CAMPOS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #26311F !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #202820 !important;

    -webkit-text-fill-color:
        #202820 !important;

    border:
        2px solid #7C8956 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #556B2F !important;

    box-shadow:
        0 0 0 3px rgba(85,107,47,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #6A7060 !important;
    opacity: 1 !important;
}


/* =========================================================
SELECTBOX - CORREÇÃO DEFINITIVA
========================================================= */

/* Caixa principal */

[data-baseweb="select"] > div {
    background-color: #2F323C !important;

    border:
        2px solid #687548 !important;

    border-radius: 12px !important;
}


/* TEXTO DO VEÍCULO SELECIONADO */

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}


/* Input interno */

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}


/* Valor selecionado */

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}


/* Seta */

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}


/* Hover */

[data-baseweb="select"] > div:hover {
    border-color: #A4B66A !important;
}


/* =========================================================
MENU ABERTO DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #2F323C !important;
}

[data-baseweb="menu"] {
    background-color: #2F323C !important;
}

[role="option"] {
    background-color: #2F323C !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #52632D !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #52632D,
            #788B48
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(82,99,45,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #3E4E23,
            #647738
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #B8C391;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #536044 !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Marca",
        "Modelo",
        "Ano",
        "Cor",
        "Placa",
        "Quilometragem",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# Garantir colunas necessárias

colunas_necessarias = [
    "Marca",
    "Modelo",
    "Ano",
    "Cor",
    "Placa",
    "Quilometragem",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


# Converter valores

df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Quilometragem"] = pd.to_numeric(
    df["Quilometragem"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
🚗 AutoCadastro
</div>

<div class="logo-subtitle">
GESTÃO INTELIGENTE DE VEÍCULOS
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Carro",
        "🚙 Carros Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "AutoCadastro PRO • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Sua frota.<br>
Seu controle.
</div>

<div class="hero-text">
Tenha todos os seus veículos organizados em um único lugar.<br>
Cadastre, consulte e acompanhe sua frota de forma simples,
rápida e profissional.
</div>

<div class="hero-badge">
🚗 GESTÃO INTELIGENTE
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
"""
<div class="page-title">
📊 Visão geral da sua frota
</div>

<div class="page-subtitle">
Acompanhe seus veículos e mantenha tudo organizado.
</div>
""",
        unsafe_allow_html=True
    )

    total_carros = len(df)

    valor_total = df["Valor"].sum()

    km_total = df["Quilometragem"].sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🚗
</div>

<div class="card-number">
{total_carros}
</div>

<div class="card-label">
VEÍCULOS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR TOTAL DA FROTA
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🛣️
</div>

<div class="card-number">
{km_total:,.0f} km
</div>

<div class="card-label">
QUILOMETRAGEM REGISTRADA
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
🚀 Controle profissional
</h2>

<p>
O AutoCadastro PRO permite manter todos os seus veículos
organizados em um único lugar.
</p>

<p>
Cadastre, consulte, pesquise e acompanhe as informações
da sua frota de maneira moderna e profissional.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_FROTA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR CARRO
# =========================================================

elif menu == "➕ Cadastrar Carro":

    st.markdown(
"""
<div class="page-title">
➕ Novo veículo
</div>

<div class="page-subtitle">
Adicione um novo veículo ao seu AutoCadastro PRO.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_carro",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            marca = st.text_input(
                "🏷️ Marca"
            )

            modelo = st.text_input(
                "🚗 Modelo"
            )

            ano = st.number_input(
                "📅 Ano",
                min_value=1900,
                max_value=2035,
                value=2024,
                step=1
            )

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Verde Oliva",
                    "Preto",
                    "Branco",
                    "Prata",
                    "Cinza",
                    "Vermelho",
                    "Azul",
                    "Amarelo",
                    "Outro"
                ]
            )


        with col2:

            placa = st.text_input(
                "🔢 Placa"
            )

            quilometragem = st.number_input(
                "🛣️ Quilometragem",
                min_value=0,
                value=0,
                step=100
            )

            valor = st.number_input(
                "💰 Valor do Veículo",
                min_value=0.0,
                value=0.0,
                step=1000.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR VEÍCULO"
        )


    if cadastrar:

        if (
            marca.strip()
            and modelo.strip()
            and placa.strip()
        ):

            novo_carro = pd.DataFrame(
                [{
                    "Marca": marca.strip(),
                    "Modelo": modelo.strip(),
                    "Ano": int(ano),
                    "Cor": cor,
                    "Placa": placa.strip().upper(),
                    "Quilometragem": int(quilometragem),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_carro
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🚗 Veículo cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha Marca, Modelo e Placa."
            )


# =========================================================
# CARROS CADASTRADOS
# =========================================================

elif menu == "🚙 Carros Cadastrados":

    st.markdown(
"""
<div class="page-title">
🚙 Minha frota
</div>

<div class="page-subtitle">
Consulte e pesquise todos os veículos cadastrados.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🚗 Nenhum veículo cadastrado
</h2>

<p>
Sua garagem ainda está vazia.
Cadastre seu primeiro veículo para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar veículo",
            placeholder="Digite marca, modelo, placa ou cor..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        opcoes_carros = df.index.tolist()


        carro_excluir = st.selectbox(
            "🗑️ Selecione um veículo para excluir",
            options=opcoes_carros,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Modelo']} - "
                f"{df.loc[indice, 'Placa']}"
        )


        if st.button(
            "🗑️ EXCLUIR VEÍCULO"
        ):

            df = df.drop(
                carro_excluir
            )

            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🚗 Veículo excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

🚗 AutoCadastro PRO<br>
Gestão inteligente de veículos

</div>
""",
    unsafe_allow_html=True
)
