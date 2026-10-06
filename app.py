import streamlit as st
import pickle
import numpy as np


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# COLOR PALETTE
# ============================================================

BACKGROUND = "#E6D2BF"
DARK_BROWN = "#4A2C1A"
BROWN = "#6B4226"
MEDIUM_BROWN = "#8B5E3C"
BORDER_BROWN = "#B88968"
CARD = "#FFF9F3"
WHITE = "#FFFFFF"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    .stApp {{
        background-color: {BACKGROUND};
    }}

    .main {{
        background-color: {BACKGROUND};
    }}


    /* =====================================================
       MAIN TEXT
       ===================================================== */

    p {{
        color: {DARK_BROWN} !important;
    }}

    h1 {{
        color: {DARK_BROWN} !important;
        font-weight: 800 !important;
    }}

    h2, h3, h4 {{
        color: {DARK_BROWN} !important;
        font-weight: 700 !important;
    }}

    label {{
        color: {DARK_BROWN} !important;
        font-weight: 700 !important;
    }}


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {{
        background-color: #D8BFA8;
        border-right: 2px solid {BORDER_BROWN};
    }}

    section[data-testid="stSidebar"] p {{
        color: {DARK_BROWN} !important;
    }}

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {DARK_BROWN} !important;
    }}

    section[data-testid="stSidebar"] .stCaption {{
        color: {DARK_BROWN} !important;
    }}


    /* =====================================================
       INPUT LABELS
       ===================================================== */

    .stNumberInput label {{
        color: {DARK_BROWN} !important;
        font-weight: 700 !important;
    }}


    /* =====================================================
       INPUT BOXES
       ===================================================== */

    .stNumberInput input {{
        background-color: {WHITE} !important;
        color: {DARK_BROWN} !important;
        border: 2px solid {BORDER_BROWN} !important;
        border-radius: 10px !important;
    }}

    .stNumberInput input:focus {{
        border: 2px solid {BROWN} !important;
        box-shadow: 0 0 5px rgba(107, 66, 38, 0.25) !important;
    }}


    /* =====================================================
       INFO / HELP TOOLTIP
       ===================================================== */

    [data-testid="stTooltipContent"] {{
        background-color: {BROWN} !important;
        color: {WHITE} !important;
        border: 1px solid {BORDER_BROWN} !important;
        border-radius: 10px !important;
        box-shadow: 0px 5px 15px rgba(74, 44, 26, 0.30) !important;
    }}

    [data-testid="stTooltipContent"] p {{
        color: {WHITE} !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
    }}


    /* =====================================================
       BUTTON
       ===================================================== */

    .stButton > button {{
        background-color: {BROWN} !important;
        color: {WHITE} !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        padding: 14px 20px !important;
        width: 100%;
        box-shadow: 0px 5px 12px rgba(74, 44, 26, 0.25);
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        background-color: {DARK_BROWN} !important;
        color: {WHITE} !important;
        transform: translateY(-1px);
    }}


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {{
        border: none;
        border-top: 2px solid {BORDER_BROWN};
        margin-top: 20px;
        margin-bottom: 20px;
    }}


    /* =====================================================
       RESULT BOXES
       ===================================================== */

    div[data-testid="stAlert"] {{
        border-radius: 12px !important;
    }}


    /* =====================================================
       PROGRESS BAR
       ===================================================== */

    div[data-testid="stProgressBar"] > div > div {{
        background-color: {BROWN} !important;
    }}


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer-text {{
        text-align: center;
        color: {DARK_BROWN} !important;
        font-size: 13px;
        margin-top: 20px;
        margin-bottom: 10px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

with open("stream.pkl", "rb") as file:
    model = pickle.load(file)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🩺 Diabetes AI")

st.sidebar.divider()

st.sidebar.subheader("About the App")

st.sidebar.write(
    "This application uses a Machine Learning model "
    "to predict diabetes based on patient health information."
)

st.sidebar.subheader("🤖 Model")

st.sidebar.write("Logistic Regression")

st.sidebar.subheader("📋 Features")

st.sidebar.write(
    """
    • Pregnancies

    • Glucose Level

    • Blood Pressure

    • Skin Thickness

    • Insulin

    • BMI

    • Diabetes Pedigree Function

    • Age
    """
)

st.sidebar.divider()

st.sidebar.caption(
    "Built using Python, Machine Learning & Streamlit"
)


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🩺 Diabetes Prediction System")

st.write(
    "Enter patient health information to generate "
    "a Machine Learning based prediction."
)

st.divider()


# ============================================================
# PATIENT INFORMATION
# ============================================================

st.subheader("👤 Patient Information")

st.write(
    "Please enter the patient's health details below. "
    "Make sure the values are accurate."
)


# ============================================================
# INPUT FEATURES
# ============================================================

col1, col2 = st.columns(2)


# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    Pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=1,
        step=1,
        help="Number of times the patient has been pregnant."
    )

    Glucose = st.number_input(
        "Glucose Level (mg/dL)",
        min_value=0,
        max_value=250,
        value=120,
        step=1,
        help="Blood glucose concentration."
    )

    BloodPressure = st.number_input(
        "Blood Pressure (mm Hg)",
        min_value=0,
        max_value=200,
        value=70,
        step=1,
        help="Blood pressure measurement."
    )

    SkinThickness = st.number_input(
        "Skin Thickness (mm)",
        min_value=0,
        max_value=100,
        value=20,
        step=1,
        help="Triceps skin-fold thickness measurement."
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    Insulin = st.number_input(
        "Insulin (µU/mL)",
        min_value=0,
        max_value=900,
        value=80,
        step=1,
        help="Serum insulin measurement."
    )

    BMI = st.number_input(
        "BMI (kg/m²)",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1,
        help="Body Mass Index."
    )

    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5,
        step=0.01,
        help="Score representing diabetes-related family history."
    )

    Age = st.number_input(
        "Age (years)",
        min_value=1,
        max_value=120,
        value=30,
        step=1,
        help="Patient's age."
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.write("")

if st.button("🔍  Predict Diabetes"):

    # --------------------------------------------------------
    # CREATE INPUT DATA
    # --------------------------------------------------------

    input_data = np.array([[
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]])


    # --------------------------------------------------------
    # MAKE PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(input_data)


    # --------------------------------------------------------
    # GET PROBABILITY
    # --------------------------------------------------------

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0][1]
    else:
        probability = None


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    st.divider()

    st.subheader("📊 Prediction Result")


    if prediction[0] == 1:

        st.error("⚠️ The model predicts: Diabetes")

        if probability is not None:

            st.write(
                f"Estimated diabetes probability: "
                f"**{probability * 100:.2f}%**"
            )

            st.progress(float(probability))

    else:

        st.success("✅ The model predicts: No Diabetes")

        if probability is not None:

            st.write(
                f"Estimated diabetes probability: "
                f"**{probability * 100:.2f}%**"
            )

            st.progress(float(probability))


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<p class="footer-text">'
    '🩺 Diabetes Prediction System | '
    'Machine Learning Project<br>'
    'For educational and demonstration purposes only.'
    '</p>',
    unsafe_allow_html=True
)