import streamlit as st
import pandas as pd
from datetime import datetime

from utils import load_model, apply_style, sidebar_brand, FEATURES

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="DiaSense AI | Prediction",
    page_icon="🩺",
    layout="wide"
)

apply_style()
sidebar_brand()

model = load_model()

if "history" not in st.session_state:
    st.session_state.history = []

if "latest_result" not in st.session_state:
    st.session_state.latest_result = None


# ==========================================
# PREMIUM VISUAL DESIGN
# ==========================================

st.markdown("""
<style>

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* HERO */

.assessment-hero {
    background: linear-gradient(120deg, #30221F, #54382D, #916044);
    border-radius: 25px;
    padding: 38px 42px;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(61,39,29,0.15);
}

.hero-tag {
    display: inline-block;
    color: #EAC99F;
    background: rgba(255,255,255,0.10);
    padding: 8px 15px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.assessment-hero h1 {
    color: #FFFFFF !important;
    font-size: 36px !important;
    font-weight: 850 !important;
    margin: 15px 0 8px 0 !important;
}

.assessment-hero p {
    color: #F3E6DA !important;
    font-size: 14px;
    line-height: 1.8;
    max-width: 750px;
}

.hero-symbol {
    font-size: 75px;
    text-align: center;
}

/* HEADINGS */

.section-kicker {
    color: #A87550;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2.5px;
}

.section-title {
    color: #493329;
    font-size: 23px;
    font-weight: 850;
    margin-top: 5px;
}

.section-subtitle {
    color: #806A5D;
    font-size: 13px;
    margin-bottom: 18px;
}

/* INPUT CARDS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFCF7;
    border: 1px solid #E9DCCF;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(71,47,34,0.055);
}

.metric-icon {
    font-size: 27px;
}

.metric-name {
    color: #684638;
    font-size: 14px;
    font-weight: 850;
}

.metric-description {
    color: #947D6D;
    font-size: 11px;
    min-height: 30px;
}

[data-testid="stMetricLabel"] {
    color: #927561 !important;
    font-size: 12px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #855638 !important;
    font-size: 30px !important;
    font-weight: 850 !important;
}

[data-testid="stSlider"] label {
    color: #684638 !important;
    font-weight: 750 !important;
    font-size: 12px !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] {
    padding-top: 8px;
}

[data-testid="stSlider"] [role="slider"] {
    background: #A87550 !important;
    border-color: #A87550 !important;
}

/* BUTTON */

.stButton button {
    background: linear-gradient(110deg, #684638, #A87550, #B7835D) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    min-height: 49px;
    font-weight: 850 !important;
    font-size: 14px !important;
    box-shadow: 0 6px 15px rgba(104,70,56,0.18);
}

.stButton button:hover {
    background: linear-gradient(110deg, #493027, #684638) !important;
    transform: translateY(-2px);
}

/* RESULT */

.result-panel {
    background: linear-gradient(120deg, #30221F, #654333, #916044);
    border-radius: 22px;
    padding: 28px;
    min-height: 220px;
}

.result-panel h2 {
    color: #FFFFFF !important;
    font-size: 24px !important;
}

.result-panel p {
    color: #F3E6DA !important;
    font-size: 13px;
    line-height: 1.7;
}

.result-label {
    color: #EAC99F;
    font-size: 11px;
    font-weight: 850;
    letter-spacing: 2px;
}

.result-value {
    color: #FFFFFF;
    font-size: 27px;
    font-weight: 850;
    margin: 13px 0;
}

.probability-value {
    color: #A87550;
    font-size: 38px;
    font-weight: 850;
    text-align: center;
}

.info-note {
    background: #F0E5D8;
    border: 1px solid #E5D2BE;
    border-radius: 15px;
    padding: 17px;
    color: #654C3D;
    font-size: 12px;
    line-height: 1.7;
}

.footer-box {
    background: #30221F;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    margin-top: 35px;
}

.footer-box h4 {
    color: #FFF9F1 !important;
}

.footer-box p {
    color: #EAD7C2 !important;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="assessment-hero">
    <div class="hero-tag">✦ INTELLIGENT HEALTH ASSESSMENT</div>
    <h1>Let's Understand Your Health</h1>
    <p>
        Adjust the interactive health indicators below and explore
        how a machine learning model evaluates the information.
        Your selected measurements will update instantly.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# INTRODUCTION
# ==========================================

st.markdown("""
<div class="section-kicker">YOUR PERSONAL ASSESSMENT</div>
<div class="section-title">Explore Your Health Indicators</div>
<div class="section-subtitle">
    Move the sliders to select your measurements. Each card displays your current selection.
</div>
""", unsafe_allow_html=True)


# ==========================================
# PERSONAL INFORMATION
# ==========================================

st.markdown("### 👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">🎂</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Your Age</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Select your current age in years.</div>',
                    unsafe_allow_html=True)

        age = st.slider(
            "Age",
            min_value=1,
            max_value=120,
            value=25,
            step=1,
            key="age_slider"
        )

        st.metric("SELECTED AGE", f"{age} years")

with col2:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">🤰</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Pregnancy History</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Select the number of pregnancies.</div>',
                    unsafe_allow_html=True)

        pregnancies = st.slider(
            "Number of Pregnancies",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key="pregnancy_slider"
        )

        st.metric("SELECTED COUNT", f"{pregnancies}")


# ==========================================
# BLOOD MEASUREMENTS
# ==========================================

st.write("")
st.markdown("### 🩸 Blood & Vital Measurements")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">🩸</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Glucose Level</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Blood glucose concentration.</div>',
                    unsafe_allow_html=True)

        glucose = st.slider(
            "Glucose (mg/dL)",
            min_value=0,
            max_value=300,
            value=120,
            step=1,
            key="glucose_slider"
        )

        st.metric("GLUCOSE READING", f"{glucose} mg/dL")

with col2:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">💗</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Blood Pressure</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Diastolic blood pressure measurement.</div>',
                    unsafe_allow_html=True)

        blood_pressure = st.slider(
            "Blood Pressure (mm Hg)",
            min_value=0,
            max_value=200,
            value=70,
            step=1,
            key="bp_slider"
        )

        st.metric("BLOOD PRESSURE", f"{blood_pressure} mm Hg")


# ==========================================
# BODY MEASUREMENTS
# ==========================================

st.write("")
st.markdown("### ⚖️ Body Measurements")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">📏</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Skin Thickness</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Triceps skin fold measurement.</div>',
                    unsafe_allow_html=True)

        skin_thickness = st.slider(
            "Skin Thickness (mm)",
            min_value=0,
            max_value=100,
            value=20,
            step=1,
            key="skin_slider"
        )

        st.metric("SKIN THICKNESS", f"{skin_thickness} mm")

with col2:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">⚖️</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Body Mass Index</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Select your BMI measurement.</div>',
                    unsafe_allow_html=True)

        bmi = st.slider(
            "BMI",
            min_value=0.0,
            max_value=80.0,
            value=25.0,
            step=0.1,
            key="bmi_slider"
        )

        st.metric("YOUR BMI", f"{bmi:.1f}")


# ==========================================
# ADDITIONAL INDICATORS
# ==========================================

st.write("")
st.markdown("### 🧬 Additional Health Indicators")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">💉</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Insulin Level</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Two-hour serum insulin measurement.</div>',
                    unsafe_allow_html=True)

        insulin = st.slider(
            "Insulin (mu U/ml)",
            min_value=0,
            max_value=1000,
            value=80,
            step=1,
            key="insulin_slider"
        )

        st.metric("INSULIN READING", f"{insulin} mu U/ml")

with col2:
    with st.container(border=True):
        st.markdown('<div class="metric-icon">🧬</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-name">Diabetes Pedigree Function</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="metric-description">Family-history-related model indicator.</div>',
                    unsafe_allow_html=True)

        dpf = st.slider(
            "Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.5,
            step=0.01,
            key="dpf_slider"
        )

        st.metric("PEDIGREE VALUE", f"{dpf:.2f}")


# ==========================================
# INPUT SUMMARY
# ==========================================

st.write("")
st.markdown("""
<div class="section-kicker">REVIEW YOUR SELECTION</div>
<div class="section-title">Your Health Profile</div>
<div class="section-subtitle">
    Check your selected measurements before generating a prediction.
</div>
""", unsafe_allow_html=True)

summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

with summary_col1:
    st.metric("Age", f"{age} years")

with summary_col2:
    st.metric("Glucose", f"{glucose} mg/dL")

with summary_col3:
    st.metric("BMI", f"{bmi:.1f}")

with summary_col4:
    st.metric("Insulin", f"{insulin} mu U/ml")


# ==========================================
# GENERATE PREDICTION
# ==========================================

st.write("")

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:
    predict_clicked = st.button(
        "✦  GENERATE MY PREDICTION",
        use_container_width=True
    )


# ==========================================
# MODEL PREDICTION
# ==========================================

if predict_clicked:

    input_data = pd.DataFrame(
        [[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]],
        columns=FEATURES
    )

    prediction = int(model.predict(input_data)[0])

    positive_probability = float(
        model.predict_proba(input_data)[0][1] * 100
    )

    result = {
        "Date & Time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "Prediction": (
            "Positive Class"
            if prediction == 1
            else "Negative Class"
        ),
        "Positive Class Probability": round(
            positive_probability, 2
        )
    }

    st.session_state.latest_result = result
    st.session_state.history.append(result)


# ==========================================
# RESULT DISPLAY
# ==========================================

if st.session_state.latest_result is not None:

    result = st.session_state.latest_result

    st.write("")
    st.markdown("""
    <div class="section-kicker">ASSESSMENT COMPLETED</div>
    <div class="section-title">Your Prediction Overview</div>
    <div class="section-subtitle">
        Here is the output generated by the machine learning model.
    </div>
    """, unsafe_allow_html=True)

    result_col1, result_col2 = st.columns([1.4, 1])

    with result_col1:

        st.markdown(f"""
        <div class="result-panel">
            <div class="result-label">MODEL PREDICTION</div>
            <h2>Assessment Result</h2>
            <div class="result-value">
                {"Positive Class Predicted" if result["Prediction"] == "Positive Class" else "Negative Class Predicted"}
            </div>
            <p>
                {"The model assigned your entered measurements to the positive class." if result["Prediction"] == "Positive Class" else "The model assigned your entered measurements to the negative class."}
            </p>
        </div>
        """, unsafe_allow_html=True)

    with result_col2:

        with st.container(border=True):

            st.markdown(
                '<div style="text-align:center;color:#806A5D;'
                'font-size:12px;font-weight:850;letter-spacing:1px;">'
                'POSITIVE CLASS PROBABILITY</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="probability-value">'
                f'{result["Positive Class Probability"]:.1f}%</div>',
                unsafe_allow_html=True
            )

            st.progress(
                min(
                    max(result["Positive Class Probability"] / 100, 0),
                    1
                )
            )

            st.caption(
                "Model-estimated probability for class 1."
            )

    st.write("")

    st.markdown("""
    <div class="info-note">
        <b>Medical disclaimer:</b> This application is an educational
        machine learning project. Its output is not a medical diagnosis,
        and the model probability is not a confirmed personal health risk.
        Please consult a qualified healthcare professional for medical
        assessment and advice.
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# PREDICTION HISTORY
# ==========================================

st.write("")
st.markdown("""
<div class="section-kicker">YOUR RECORDS</div>
<div class="section-title">Prediction History</div>
<div class="section-subtitle">
    View and download the predictions generated during this session.
</div>
""", unsafe_allow_html=True)

if st.session_state.history:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "⬇ Download Prediction History",
            data=history_df.to_csv(index=False).encode("utf-8"),
            file_name="DiaSense_AI_Prediction_History.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:
        if st.button(
            "🗑 Clear Prediction History",
            use_container_width=True
        ):
            st.session_state.history = []
            st.session_state.latest_result = None
            st.rerun()

else:

    with st.container(border=True):
        st.markdown("""
        <div style="text-align:center;padding:18px;">
            <div style="font-size:35px;">📋</div>
            <h4 style="color:#684638;">No Predictions Yet</h4>
            <p style="color:#806A5D;font-size:13px;">
                Your assessment records will appear here after your first prediction.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer-box">
    <h4>🩺 DiaSense AI</h4>
    <p>Intelligent Healthcare Insights • Machine Learning • Health Awareness</p>
    <p>For educational purposes only. Not a substitute for professional medical advice.</p>
</div>
""", unsafe_allow_html=True)
