import pickle
from pathlib import Path
import streamlit as st
from textwrap import dedent

# MODEL CONFIGURATION

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "stream.pkl"

FEATURES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)


# GLOBAL DESIGN

def apply_style():

    st.markdown(dedent("""
    <style>

    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(135deg,#FAF3E9,#F3E8DC,#F8F0E6);
        color: #382A25;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,#30221F,#4A3028,#684638);
    }

    [data-testid="stSidebar"] * {
        color: #FFF9F1 !important;
    }

    /* HEADINGS */
    h1, h2, h3 {
        color: #382A25 !important;
        font-weight: 800 !important;
    }

    p, li {
        color: #70594D;
    }

    /* HERO SECTIONS */
    .hero-home h1,
    .pred-hero h1,
    .insight-hero h1 {
        color: #FFFFFF !important;
    }

    .hero-home p,
    .pred-hero p,
    .insight-hero p {
        color: #F5E8DA !important;
    }

    .hero-home .eyebrow,
    .pred-hero .eyebrow,
    .insight-hero .eyebrow,
    .hero-home .section-kicker,
    .pred-hero .section-kicker,
    .insight-hero .section-kicker {
        color: #E4C49D !important;
    }

    /* CONTENT CARDS */
    .home-card, .info-card, .insight-card, .tip-card {
        background: #FFFDF8;
        border: 1px solid #EADBCB;
        border-radius: 19px;
        padding: 20px;
        box-shadow: 0 7px 22px rgba(72,45,32,0.08);
    }

    .home-card h3, .info-card h3,
    .insight-card h3, .tip-card h4 {
        color: #684638 !important;
    }

    .home-card p, .info-card p,
    .insight-card p, .tip-card p {
        color: #70594D !important;
    }

    /* RESULT PANELS */
    .result-panel, .soft-panel {
        background: linear-gradient(130deg,#F2E3D2,#F8EFE3,#EAD7C2);
        border: 1px solid #E5CFB9;
        border-radius: 21px;
        padding: 25px;
    }

    .result-title {
        color: #4A3028 !important;
    }

    .result-text {
        color: #70594D !important;
    }

    .result-number {
        color: #986344 !important;
    }

    /* METRIC CARDS */
    [data-testid="stMetric"] {
        background: #FFFDF8;
        border: 1px solid #EADBCB;
        border-radius: 17px;
        padding: 17px;
        box-shadow: 0 5px 15px rgba(72,45,32,0.05);
    }

    [data-testid="stMetricLabel"] {
        color: #806656 !important;
    }

    [data-testid="stMetricValue"] {
        color: #8B5E46 !important;
    }

    /* BUTTONS */
    .stButton button, .stFormSubmitButton button {
        background: linear-gradient(100deg,#684638,#A87550,#B7835D);
        color: #FFFFFF !important;
        border: none;
        border-radius: 11px;
        font-weight: 750;
        min-height: 45px;
    }

    .stButton button:hover, .stFormSubmitButton button:hover {
        background: #4A3028;
        color: #FFFFFF !important;
        border: 1px solid #D9B98C;
    }

    /* INPUTS */
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input {
        background: #FFFDF8;
        color: #382A25;
        border-color: #DCC5AE;
    }

    [data-testid="stSlider"] {
        color: #986344;
    }

    /* IMAGES */
    [data-testid="stImage"] img {
        border-radius: 17px;
    }

    /* FOOTER */
    .footer {
        background: linear-gradient(110deg,#30221F,#684638);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        margin-top: 30px;
    }

    .footer h3, .footer p {
        color: #FFF9F1 !important;
    }

    </style>
    """), unsafe_allow_html=True)


# SIDEBAR BRANDING

def sidebar_brand():

    with st.sidebar:
        st.html("""
        <div style="text-align:center;padding:20px 5px 25px;">
            <div style="font-size:38px;margin-bottom:8px;">🩺</div>

            <h2 style="color:#FFF9F1 !important;font-size:25px;margin:0;">
                DiaSense AI
            </h2>

            <p style="color:#EAD7C2 !important;font-size:12px;margin-top:7px;">
                SMART DIABETES INSIGHTS
            </p>

            <div style="height:3px;width:55px;background:#D9B98C;margin:15px auto;border-radius:5px;"></div>

            <p style="color:#F5E8DA !important;font-size:10px;letter-spacing:2px;">
                AI • HEALTHCARE • INTELLIGENCE
            </p>
        </div>
        """)
