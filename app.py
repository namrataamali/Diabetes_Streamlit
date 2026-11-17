import streamlit as st
from textwrap import dedent
from utils import apply_style, sidebar_brand

st.set_page_config(
    page_title="DiaSense AI | Smart Diabetes Insights",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_style()
sidebar_brand()

# ==========================================
# PREMIUM HOMEPAGE STYLING
# ==========================================

st.markdown(dedent("""
<style>
.stApp {
    background: linear-gradient(135deg, #FAF3E9, #F7EEE3, #F3E6D8);
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* GLOBAL TEXT VISIBILITY */
h1, h2, h3, h4 {
    color: #38251F !important;
}

p, li, label, .stMarkdown {
    color: #49352C;
}

.section-kicker {
    color: #925D3E !important;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 3.5px;
    margin-bottom: 12px;
    text-align: center;
}


.section-title {
    color: #38251F !important;
    font-size: 29px;
    font-weight: 850;
    line-height: 1.3;
    margin-bottom: 10px;
}

.section-description {
    color: #5F493D !important;
    font-size: 15px;
    line-height: 1.8;
    max-width: 850px;
    margin-bottom: 25px;
}

/* HERO */
.hero-home {
    background: linear-gradient(125deg, #30221F, #51352B, #916044);
    border-radius: 25px;
    padding: 35px;
    height: 365px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 13px 35px rgba(63,39,28,0.16);
    overflow: hidden;
}

.hero-eyebrow {
    color: #E7C49E !important;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    margin-bottom: 17px;
}

.hero-home h1 {
    color: #FFFFFF !important;
    font-size: clamp(30px, 3.2vw, 46px);
    line-height: 1.15;
    font-weight: 850;
    margin: 0 0 17px;
}

.hero-home p {
    color: #FFF3E7 !important;
    font-size: 15px;
    line-height: 1.85;
}

.hero-tag {
    display: inline-block;
    color: #FFF3E7 !important;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 30px;
    padding: 8px 13px;
    font-size: 11px;
    font-weight: 700;
    margin-top: 15px;
}

.hero-image-container {
    width: 100%;
    height: 365px;
    overflow: hidden;
    border-radius: 25px;
    box-shadow: 0 13px 35px rgba(63,39,28,0.16);
    background: #E8D7C5;
}

.hero-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

/* BUTTONS */
.stButton button, .stPageLink a {
    background: linear-gradient(105deg, #684638, #A87550) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 750 !important;
    min-height: 46px;
    box-shadow: 0 5px 14px rgba(104,70,56,0.15);
    transition: all 0.25s ease;
}

.stButton button:hover, .stPageLink a:hover {
    background: #30221F !important;
    transform: translateY(-2px);
}

/* STATISTICS */
.stat-card {
    background: #FFFDF8;
    border: 1px solid #E5D3C1;
    border-radius: 18px;
    padding: 20px 15px;
    min-height: 135px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(72,45,32,0.07);
    transition: 0.25s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(72,45,32,0.12);
}

.stat-icon {
    font-size: 25px;
    margin-bottom: 8px;
}

.stat-number {
    color: #805039 !important;
    font-size: 27px;
    font-weight: 850;
}

.stat-label {
    color: #5F493D !important;
    font-size: 12px;
    font-weight: 750;
    margin-top: 7px;
}

/* FEATURE CARDS */
.feature-card {
    background: #FFFDF8;
    border: 1px solid #E5D3C1;
    border-radius: 19px;
    overflow: hidden;
    min-height: 350px;
    box-shadow: 0 7px 22px rgba(72,45,32,0.08);
    transition: 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 30px rgba(72,45,32,0.14);
}

.feature-image {
    width: 100%;
    height: 185px;
    overflow: hidden;
    background: #EADBCB;
}

.feature-image img {
    width: 100%;
    height: 185px;
    object-fit: cover;
    display: block;
    transition: transform 0.4s ease;
}

.feature-card:hover .feature-image img {
    transform: scale(1.05);
}

.feature-content {
    padding: 19px;
}

.feature-icon {
    font-size: 22px;
    margin-bottom: 8px;
}

.feature-content h3 {
    color: #684638 !important;
    font-size: 18px;
    font-weight: 850;
    margin: 0 0 9px;
}

.feature-content p {
    color: #574238 !important;
    font-size: 13px;
    line-height: 1.8;
    margin: 0;
}

/* WELLNESS PANEL */
.wellness-panel {
    background: linear-gradient(120deg, #EAD7C2, #F5E9DA, #E8D1BB);
    border: 1px solid #DCC1A8;
    border-radius: 21px;
    padding: 27px;
    min-height: 290px;
    box-shadow: 0 7px 20px rgba(72,45,32,0.07);
}

.wellness-panel h3 {
    color: #38251F !important;
    font-size: 23px;
    font-weight: 850;
    margin-bottom: 12px;
}

.wellness-panel p {
    color: #49352C !important;
    font-size: 14px;
    line-height: 1.9;
}

/* GALLERY */
.gallery-card {
    background: #FFFDF8;
    border: 1px solid #E5D3C1;
    border-radius: 17px;
    overflow: hidden;
    box-shadow: 0 6px 18px rgba(72,45,32,0.08);
    transition: 0.25s ease;
}

.gallery-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(72,45,32,0.13);
}

.gallery-image {
    height: 220px;
    width: 100%;
    overflow: hidden;
}

.gallery-image img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}

.gallery-caption {
    color: #51352B !important;
    text-align: center;
    font-size: 13px;
    font-weight: 850;
    padding: 14px 8px;
}

/* TECHNOLOGY */
.tech-card {
    background: #FFFDF8;
    border: 1px solid #E5D3C1;
    border-radius: 15px;
    padding: 18px 8px;
    text-align: center;
    min-height: 105px;
    box-shadow: 0 5px 16px rgba(72,45,32,0.07);
    transition: 0.25s ease;
}

.tech-card:hover {
    transform: translateY(-4px);
    border-color: #B7835D;
}

.tech-icon {
    font-size: 25px;
    margin-bottom: 8px;
}

.tech-name {
    color: #51352B !important;
    font-size: 13px;
    font-weight: 850;
}

/* CLOSING SECTION */
.closing-panel {
    background: linear-gradient(115deg, #30221F, #684638, #986849);
    border-radius: 22px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 9px 25px rgba(48,34,31,0.14);
}

.closing-panel h2 {
    color: #FFFFFF !important;
    font-size: 25px;
    font-weight: 850;
    margin-bottom: 10px;
}

.closing-panel p {
    color: #FFF1E3 !important;
    font-size: 14px;
    line-height: 1.8;
}

.closing-label {
    color: #E8C59F !important;
    font-size: 11px;
    font-weight: 850;
    letter-spacing: 3px;
    margin-bottom: 10px;
}

/* FOOTER */
.footer {
    background: linear-gradient(110deg, #30221F, #51352B, #684638);
    border-radius: 20px;
    padding: 26px;
    text-align: center;
    margin-top: 28px;
}

.footer h3 {
    color: #FFFFFF !important;
    font-size: 21px;
    font-weight: 850;
}

.footer p {
    color: #F5E8DA !important;
    font-size: 12px;
    line-height: 1.8;
    margin: 5px 0;
}

.footer-line {
    width: 55px;
    height: 3px;
    background: #D9B98C;
    margin: 13px auto;
    border-radius: 5px;
}

@media (max-width: 768px) {
    .hero-home {
        height: auto;
        min-height: 320px;
        padding: 26px;
    }

    .hero-image-container {
        height: 260px;
    }

    .section-title {
        font-size: 24px;
    }
}
</style>
"""), unsafe_allow_html=True)


# ==========================================
# HERO SECTION
# ==========================================

st.markdown(
    '<div class="section-kicker">WELCOME TO DIASENSE AI</div>',
    unsafe_allow_html=True
)


left, right = st.columns([1, 0.95], gap="large")

with left:
    st.markdown("""
    <div class="hero-home">
        <div class="hero-eyebrow">✦ AI-POWERED HEALTH PLATFORM</div>
        <h1>Understand Health.<br>Discover Insights.</h1>
        <p>
            Explore intelligent diabetes risk prediction and meaningful
            health insights through machine learning. Make information
            easier to understand and take a more informed approach
            towards your wellbeing.
        </p>
        <div class="hero-tag">🩺 &nbsp; SMARTER HEALTH AWARENESS</div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="hero-image-container">
        <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1000&h=750&fit=crop"
        alt="Healthcare professional">
    </div>
    """, unsafe_allow_html=True)

st.write("")

button_left, button_right, empty = st.columns([1, 1, 2])

with button_left:
    st.page_link(
        "pages/2_Prediction.py",
        label="🩺 Explore Prediction",
        use_container_width=True
    )

with button_right:
    st.page_link(
        "pages/3_Insights.py",
        label="📊 Explore Insights",
        use_container_width=True
    )


# ==========================================
# STATISTICS
# ==========================================

st.write("")
st.markdown('<div class="section-kicker">AT A GLANCE</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Your Health Intelligence Hub</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-description">
A simple platform combining machine learning, data analysis and health awareness.
</div>
""", unsafe_allow_html=True)

stat_data = [
    ("🧬", "08", "Health Input Features"),
    ("🤖", "01", "ML Algorithm"),
    ("📈", "02", "Prediction Classes"),
    ("🖥️", "03", "Interactive Pages")
]

stat_cols = st.columns(4, gap="medium")

for col, (icon, number, label) in zip(stat_cols, stat_data):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon">{icon}</div>
            <div class="stat-number">{number}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PLATFORM FEATURES
# ==========================================

st.write("")
st.markdown('<div class="section-kicker">EXPLORE THE PLATFORM</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Everything You Need in One Place</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-description">
Discover the key features designed to make health information more accessible,
interactive and understandable.
</div>
""", unsafe_allow_html=True)

features = [
    (
        "https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=800",
        "🩺",
        "AI Prediction",
        "Explore diabetes risk predictions using eight health-related input features and a trained machine learning model."
    ),
    (
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800",
        "📊",
        "Analytics & Insights",
        "Understand model performance, explore health indicators, examine data patterns and discover meaningful insights."
    ),
    (
        "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=800",
        "🌿",
        "Health Awareness",
        "Learn about healthy lifestyle choices, wellness habits and the importance of staying informed about your health."
    )
]

feature_cols = st.columns(3, gap="medium")

for col, (url, icon, title, description) in zip(feature_cols, features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-image">
                <img src="{url}" alt="{title}">
            </div>
            <div class="feature-content">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# HEALTH AWARENESS
# ==========================================

st.write("")
wellness_left, wellness_right = st.columns([1.05, 0.95], gap="large")

with wellness_left:
    st.markdown("""
    <div class="wellness-panel">
        <div class="section-kicker">HEALTH STARTS WITH AWARENESS</div>
        <h3>Small Insights.<br>Better Awareness.</h3>
        <p>
            A healthier lifestyle is built through everyday decisions.
            Balanced nutrition, regular physical activity and mindful
            habits can contribute to overall wellbeing.
        </p>
        <p>
            DiaSense AI brings health-related information together
            in an easy-to-explore digital experience.
        </p>
    </div>
    """, unsafe_allow_html=True)

with wellness_right:
    st.markdown("""
    <div class="hero-image-container" style="height:290px;">
        <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1000"
        alt="Healthy lifestyle and wellness">
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# WELLNESS GALLERY
# ==========================================

st.write("")
st.markdown('<div class="section-kicker">A HEALTHIER PERSPECTIVE</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Explore Wellness from Different Angles</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-description">
Three important aspects of everyday wellbeing that deserve attention.
</div>
""", unsafe_allow_html=True)

gallery = [
    (
        "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?w=800",
        "🏃",
        "Movement & Activity"
    ),
    (
        "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",
        "🥗",
        "Balanced Nutrition"
    ),
    (
        "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800",
        "🧘",
        "Mindfulness & Wellbeing"
    )
]

gallery_cols = st.columns(3, gap="medium")

for col, (url, icon, caption) in zip(gallery_cols, gallery):
    with col:
        st.markdown(f"""
        <div class="gallery-card">
            <div class="gallery-image">
                <img src="{url}" alt="{caption}">
            </div>
            <div class="gallery-caption">
                {icon} &nbsp; {caption}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# TECHNOLOGY OVERVIEW
# ==========================================

st.write("")
st.markdown('<div class="section-kicker">BUILT WITH TECHNOLOGY</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Powered by Data & Intelligence</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-description">
A combination of popular Python tools and technologies supports the
development of this interactive machine learning application.
</div>
""", unsafe_allow_html=True)

technologies = [
    ("🐍", "Python"),
    ("🤖", "Scikit-learn"),
    ("🐼", "Pandas"),
    ("📊", "Matplotlib"),
    ("⚡", "Streamlit")
]

tech_cols = st.columns(5, gap="medium")

for col, (icon, name) in zip(tech_cols, technologies):
    with col:
        st.markdown(f"""
        <div class="tech-card">
            <div class="tech-icon">{icon}</div>
            <div class="tech-name">{name}</div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# CLOSING SECTION - NO EXTRA BUTTONS
# ==========================================

st.write("")
st.markdown("""
<div class="closing-panel">
    <div class="closing-label">YOUR JOURNEY TO HEALTH AWARENESS</div>
    <h2>Knowledge is the First Step Towards Better Health.</h2>
    <p>
        Explore health-related information, understand data-driven insights
        and discover how machine learning can support health awareness.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <h3>🩺 DiaSense AI</h3>
    <p>SMART DIABETES INSIGHTS</p>
    <div class="footer-line"></div>
    <p>AI • HEALTHCARE • DATA INTELLIGENCE</p>
    <p>
        An educational machine learning project designed to explore
        diabetes risk prediction and health data insights.
    </p>
    <p style="margin-top:15px;font-size:11px;color:#E8C59F;">
        © 2026 DiaSense AI | Built with Python & Streamlit
    </p>
    <p style="font-size:10px;color:#F5E8DA;margin-top:10px;">
        Disclaimer: This application is for educational purposes only.
        It does not provide medical diagnosis or replace professional medical advice.
    </p>
</div>
""", unsafe_allow_html=True)
