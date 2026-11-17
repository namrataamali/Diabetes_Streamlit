
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

from utils import apply_style, sidebar_brand

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="DiaSense AI | Insights",
    page_icon="📊",
    layout="wide"
)

apply_style()
sidebar_brand()

# ==========================================
# COLOUR PALETTE
# ==========================================

DARK = "#30221F"
BROWN = "#684638"
MOCHA = "#916044"
CARAMEL = "#B7835D"
GOLD = "#D9B98C"
CREAM = "#FFFDF8"
IVORY = "#FAF3E9"
TEXT = "#493329"
MUTED = "#806A5D"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.titleweight": "bold",
    "axes.labelcolor": TEXT,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "text.color": TEXT
})

# ==========================================
# PREMIUM DASHBOARD CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#FAF3E9,#F5EBDD,#F9F5EE);
}

.block-container {
    max-width: 1450px;
    padding-top: 1.4rem;
    padding-bottom: 3rem;
}

/* HERO */

.insight-hero {
    background: linear-gradient(120deg,#30221F,#54382D,#916044);
    padding: 39px 42px;
    border-radius: 25px;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(61,39,29,.16);
}

.hero-label {
    color: #EAC99F;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2.5px;
}

.insight-hero h1 {
    color: #FFFFFF !important;
    font-size: 36px !important;
    font-weight: 850 !important;
    margin: 13px 0 10px 0 !important;
}

.insight-hero p {
    color: #F3E6DA !important;
    font-size: 14px;
    line-height: 1.8;
    max-width: 800px;
}

/* HEADINGS */

.section-kicker {
    color: #A87550 !important;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2.5px;
    margin-bottom: 5px;
}

.section-title {
    color: #493329 !important;
    font-size: 25px !important;
    font-weight: 850 !important;
    margin-top: 4px;
    margin-bottom: 15px;
}

.section-description {
    color: #806A5D !important;
    font-size: 13px;
    line-height: 1.7;
    margin-bottom: 18px;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(145deg,#FFFDF8,#F5EBDD);
    border: 1px solid #E9D9C7;
    border-radius: 19px;
    padding: 20px;
    box-shadow: 0 7px 20px rgba(71,47,34,.07);
    min-height: 155px;
}

.metric-icon {
    font-size: 25px;
    margin-bottom: 7px;
}

.metric-value {
    color: #684638 !important;
    font-size: 30px;
    font-weight: 900;
    margin: 5px 0;
}

.metric-label {
    color: #60483B !important;
    font-size: 13px;
    font-weight: 800;
}

.metric-note {
    color: #947D6D !important;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 5px;
}

/* CONTENT CARDS */

.insight-card {
    background: #FFFDF8;
    border: 1px solid #E9D9C7;
    border-radius: 19px;
    padding: 20px;
    box-shadow: 0 6px 18px rgba(71,47,34,.05);
}

.insight-card h4 {
    color: #684638 !important;
    font-size: 16px;
    font-weight: 800;
}

.insight-card p {
    color: #806A5D !important;
    font-size: 13px;
    line-height: 1.7;
}

.chart-card {
    background: #FFFDF8;
    border: 1px solid #E9D9C7;
    border-radius: 20px;
    padding: 15px;
    box-shadow: 0 6px 18px rgba(71,47,34,.05);
}

/* STREAMLIT METRICS */

div[data-testid="stMetric"] {
    background: #FFFDF8;
    border: 1px solid #E9D9C7;
    padding: 14px;
    border-radius: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #806A5D !important;
}

div[data-testid="stMetricValue"] {
    color: #684638 !important;
}

/* SELECTBOX / UPLOAD */

[data-testid="stFileUploader"] {
    background: #FFFDF8;
    border: 1px dashed #C9A987;
    border-radius: 17px;
    padding: 15px;
}

[data-testid="stSelectbox"] label {
    color: #684638 !important;
    font-weight: 750 !important;
}

/* INFO PANEL */

.info-panel {
    background: linear-gradient(120deg,#F1E3D3,#FAF1E5);
    border: 1px solid #E6D2BC;
    border-radius: 17px;
    padding: 19px;
    color: #684638;
    font-size: 13px;
    line-height: 1.7;
}

/* FOOTER */

.insight-footer {
    background: linear-gradient(110deg,#30221F,#684638,#916044);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    margin-top: 35px;
}

.insight-footer h3 {
    color: #FFFFFF !important;
}

.insight-footer p {
    color: #F2E5D9 !important;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================

st.html("""
<div class="insight-hero">
    <div class="hero-label">✦ DATA • PERFORMANCE • HEALTH INTELLIGENCE</div>
    <h1>Discover the Intelligence Behind Your Health</h1>
    <p>
        Explore machine learning performance, understand health
        indicators and uncover meaningful patterns through
        interactive data visualisations.
    </p>
</div>
""")


# ==========================================
# MODEL EVALUATION RESULTS
# ==========================================

TN = 84
FP = 15
FN = 17
TP = 38

total = TN + FP + FN + TP

accuracy = (TP + TN) / total if total else 0

positive_precision = (
    TP / (TP + FP) if (TP + FP) else 0
)

positive_recall = (
    TP / (TP + FN) if (TP + FN) else 0
)

positive_f1 = (
    2 * positive_precision * positive_recall
    / (positive_precision + positive_recall)
    if (positive_precision + positive_recall) else 0
)

negative_precision = (
    TN / (TN + FN) if (TN + FN) else 0
)

negative_recall = (
    TN / (TN + FP) if (TN + FP) else 0
)

negative_f1 = (
    2 * negative_precision * negative_recall
    / (negative_precision + negative_recall)
    if (negative_precision + negative_recall) else 0
)


# ==========================================
# MODEL PERFORMANCE
# ==========================================

st.markdown("""
<div class="section-kicker">01 / MODEL PERFORMANCE</div>
<div class="section-title">Performance at a Glance</div>
<div class="section-description">
    Understand how effectively the recorded model evaluation
    classified the test observations.
</div>
""", unsafe_allow_html=True)

metrics = [
    ("🎯", f"{accuracy*100:.1f}%", "Accuracy",
     "Overall correct predictions"),

    ("💎", f"{positive_precision*100:.1f}%", "Precision",
     "Correct positive predictions"),

    ("🩺", f"{positive_recall*100:.1f}%", "Recall",
     "Positive cases identified"),

    ("⚡", f"{positive_f1*100:.1f}%", "F1 Score",
     "Balance of precision and recall")
]

cols = st.columns(4, gap="medium")

for col, (icon, value, label, note) in zip(cols, metrics):

    with col:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)

st.caption(
    "These metrics are calculated from the confusion matrix recorded "
    "in the project. They are not a fresh evaluation of the saved model."
)

st.write("")


# ==========================================
# CONFUSION MATRIX
# ==========================================

st.markdown("""
<div class="section-kicker">02 / CLASSIFICATION INTELLIGENCE</div>
<div class="section-title">Understanding Model Predictions</div>
<div class="section-description">
    The confusion matrix compares actual outcomes with the
    outcomes predicted by the model.
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.15, 1], gap="large")

with left:

    cm = [[TN, FP], [FN, TP]]

    fig, ax = plt.subplots(figsize=(7, 5))

    fig.patch.set_facecolor(CREAM)
    ax.set_facecolor(CREAM)

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap=sns.blend_palette(
            ["#F3E5D5", "#D9B98C", "#A87550", "#684638"],
            as_cmap=True
        ),
        linewidths=3,
        linecolor=CREAM,
        xticklabels=["Negative", "Positive"],
        yticklabels=["Negative", "Positive"],
        annot_kws={
            "size": 20,
            "weight": "bold",
            "color": DARK
        },
        cbar=False,
        ax=ax
    )

    ax.set_xlabel(
        "Predicted Class",
        fontsize=11,
        labelpad=12,
        color=BROWN
    )

    ax.set_ylabel(
        "Actual Class",
        fontsize=11,
        labelpad=12,
        color=BROWN
    )

    ax.set_title(
        "Confusion Matrix",
        fontsize=17,
        weight="bold",
        color=DARK,
        pad=18
    )

    ax.tick_params(axis="both", labelsize=10, colors=BROWN)

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

with right:

    confusion_cards = [
        ("✅", TN, "True Negatives",
         "Negative cases correctly classified."),

        ("💗", TP, "True Positives",
         "Positive cases correctly classified."),

        ("⚠️", FP, "False Positives",
         "Negative cases incorrectly classified as positive."),

        ("🔎", FN, "False Negatives",
         "Positive cases incorrectly classified as negative.")
    ]

    for icon, number, label, description in confusion_cards:

        st.markdown(f"""
        <div class="insight-card" style="margin-bottom:12px;">
            <h4>{icon} {number} | {label}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# CLASSIFICATION REPORT
# ==========================================

st.write("")

st.markdown("""
<div class="section-kicker">03 / DETAILED EVALUATION</div>
<div class="section-title">Classification Report</div>
<div class="section-description">
    Compare precision, recall and F1-score for both outcome classes.
</div>
""", unsafe_allow_html=True)

report = pd.DataFrame({
    "Class": ["Negative (0)", "Positive (1)"],
    "Precision": [negative_precision, positive_precision],
    "Recall": [negative_recall, positive_recall],
    "F1 Score": [negative_f1, positive_f1],
    "Support": [TN + FP, FN + TP]
})

st.dataframe(
    report.style.format({
        "Precision": "{:.2f}",
        "Recall": "{:.2f}",
        "F1 Score": "{:.2f}"
    }).background_gradient(
        cmap="YlOrBr",
        subset=["Precision", "Recall", "F1 Score"]
    ),
    use_container_width=True,
    hide_index=True
)


# ==========================================
# CLASS COMPARISON CHART
# ==========================================

fig, ax = plt.subplots(figsize=(10, 4))

metric_names = ["Precision", "Recall", "F1 Score"]

negative_values = [
    negative_precision,
    negative_recall,
    negative_f1
]

positive_values = [
    positive_precision,
    positive_recall,
    positive_f1
]

x = range(len(metric_names))
width = 0.34

ax.bar(
    [i - width/2 for i in x],
    negative_values,
    width,
    label="Negative Class",
    color="#B7835D",
    edgecolor=CREAM
)

ax.bar(
    [i + width/2 for i in x],
    positive_values,
    width,
    label="Positive Class",
    color="#684638",
    edgecolor=CREAM
)

ax.set_xticks(list(x))
ax.set_xticklabels(metric_names)
ax.set_ylim(0, 1.12)
ax.set_ylabel("Score")
ax.set_title(
    "Class-wise Performance Comparison",
    fontsize=15,
    weight="bold",
    color=DARK,
    pad=15
)

ax.legend(frameon=False, ncol=2)
ax.grid(axis="y", alpha=.15)
ax.set_axisbelow(True)
ax.set_facecolor(CREAM)
fig.patch.set_facecolor(CREAM)

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
st.pyplot(fig, use_container_width=True)
plt.close(fig)


# ==========================================
# DATASET UPLOAD AND LOADING
# ==========================================

st.write("")

st.markdown("""
<div class="section-kicker">04 / DATA EXPLORATION</div>
<div class="section-title">Your Health Data, Visualised</div>
<div class="section-description">
    Explore the original diabetes dataset through interactive
    charts and statistical comparisons.
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload your diabetes CSV dataset",
    type=["csv"],
    help="Upload diabetesLogistic.csv or your original diabetes dataset."
)

dataset = None
dataset_source = None

if uploaded_file is not None:

    try:
        dataset = pd.read_csv(uploaded_file)
        dataset_source = "Uploaded dataset"

    except Exception as e:
        st.error(f"Unable to read CSV file: {e}")

else:

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    possible_files = [
        os.path.join(base_dir, "diabetesLogistic.csv"),
        os.path.join(base_dir, "diabetes.csv"),
        os.path.join(base_dir, "diabetes_data.csv"),
        os.path.join(base_dir, "diabetes_dataset.csv"),
        "diabetesLogistic.csv",
        "diabetes.csv",
        "diabetes_data.csv",
        "diabetes_dataset.csv"
    ]

    for filename in possible_files:

        if os.path.exists(filename):

            try:
                dataset = pd.read_csv(filename)
                dataset_source = os.path.basename(filename)
                break

            except Exception:
                pass


# ==========================================
# COLUMN STANDARDISATION
# ==========================================

if dataset is not None:

    aliases = {
        "Pregnancies": [
            "pregnancies", "pregnancy"
        ],

        "Glucose": [
            "glucose", "glucoselevel", "glucose_level"
        ],

        "BloodPressure": [
            "bloodpressure", "blood_pressure", "bp"
        ],

        "SkinThickness": [
            "skinthickness", "skin_thickness"
        ],

        "Insulin": [
            "insulin", "insulinlevel"
        ],

        "BMI": [
            "bmi", "bodymassindex"
        ],

        "DiabetesPedigreeFunction": [
            "diabetespedigreefunction",
            "diabetes_pedigree_function",
            "dpf"
        ],

        "Age": [
            "age"
        ],

        "Outcome": [
            "outcome", "diabetes", "class", "target"
        ]
    }

    normalised = {
        re.sub(r"[^a-z0-9]", "", str(col).lower()): col
        for col in dataset.columns
    }

    rename_columns = {}

    for standard_name, possible_names in aliases.items():

        for alias in possible_names:

            if alias in normalised:

                rename_columns[normalised[alias]] = standard_name
                break

    dataset = dataset.rename(columns=rename_columns)

    # Convert text outcomes if needed
    if "Outcome" in dataset.columns:

        if not pd.api.types.is_numeric_dtype(dataset["Outcome"]):

            outcome_map = {
                "yes": 1,
                "positive": 1,
                "diabetic": 1,
                "true": 1,
                "no": 0,
                "negative": 0,
                "non-diabetic": 0,
                "non diabetic": 0,
                "false": 0
            }

            dataset["Outcome"] = (
                dataset["Outcome"]
                .astype(str)
                .str.lower()
                .str.strip()
                .map(outcome_map)
            )

    numeric_columns = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
        "Outcome"
    ]

    for col in numeric_columns:

        if col in dataset.columns:

            dataset[col] = pd.to_numeric(
                dataset[col],
                errors="coerce"
            )

    if "Outcome" in dataset.columns:

        dataset = dataset.dropna(subset=["Outcome"])
        dataset = dataset[dataset["Outcome"].isin([0, 1])].copy()
        dataset["Outcome"] = dataset["Outcome"].astype(int)

    st.success(f"Dataset loaded successfully: {dataset_source}")


# ==========================================
# DATASET ANALYTICS
# ==========================================

if dataset is None:

    st.markdown("""
    <div class="insight-card">
        <h4>📂 Your interactive analytics are waiting</h4>
        <p>
            Upload your diabetes CSV above to activate dataset
            distribution, health indicator comparisons and
            correlation analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif "Outcome" not in dataset.columns:

    st.warning(
        "The dataset must contain an Outcome, Diabetes, Class or Target column."
    )

else:

    total_rows = len(dataset)

    diabetes_cases = int(
        (dataset["Outcome"] == 1).sum()
    )

    non_diabetes_cases = int(
        (dataset["Outcome"] == 0).sum()
    )

    diabetes_percent = (
        diabetes_cases / total_rows * 100
        if total_rows else 0
    )

    # ======================================
    # DATASET KPI CARDS
    # ======================================

    st.markdown("""
    <div class="section-kicker">DATASET OVERVIEW</div>
    <div class="section-title">Understanding the Dataset</div>
    """, unsafe_allow_html=True)

    data_metrics = [
        ("📁", f"{total_rows:,}", "Total Records"),
        ("💗", f"{diabetes_cases:,}", "Positive Cases"),
        ("🤍", f"{non_diabetes_cases:,}", "Negative Cases"),
        ("📊", f"{diabetes_percent:.1f}%", "Positive Proportion")
    ]

    cols = st.columns(4)

    for col, (icon, value, label) in zip(cols, data_metrics):

        with col:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">{icon}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    # ======================================
    # OUTCOME DISTRIBUTION
    # ======================================

    st.markdown("""
    <div class="section-kicker">CLASS DISTRIBUTION</div>
    <div class="section-title">Diabetes Outcome Distribution</div>
    """, unsafe_allow_html=True)

    d1, d2 = st.columns([1, 1.1], gap="large")

    with d1:

        fig, ax = plt.subplots(figsize=(6, 4.5))

        values = [non_diabetes_cases, diabetes_cases]

        ax.pie(
            values,
            labels=["Negative", "Positive"],
            autopct="%1.1f%%",
            startangle=90,
            colors=[CARAMEL, DARK],
            wedgeprops={
                "width": 0.38,
                "edgecolor": CREAM,
                "linewidth": 3
            },
            textprops={
                "color": TEXT,
                "weight": "bold"
            }
        )

        ax.set_title(
            "Outcome Distribution",
            fontsize=15,
            weight="bold",
            color=DARK
        )

        fig.patch.set_facecolor(CREAM)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with d2:

        st.markdown(f"""
        <div class="insight-card" style="margin-bottom:15px;">
            <h4>🤍 Negative Class</h4>
            <div style="font-size:30px;font-weight:900;color:#A87550;">
                {non_diabetes_cases:,}
            </div>
            <p>Records with outcome 0 in the dataset.</p>
        </div>

        <div class="insight-card">
            <h4>💗 Positive Class</h4>
            <div style="font-size:30px;font-weight:900;color:#684638;">
                {diabetes_cases:,}
            </div>
            <p>Records with outcome 1 in the dataset.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ======================================
    # INTERACTIVE HEALTH INDICATORS
    # ======================================

    st.markdown("""
    <div class="section-kicker">INTERACTIVE EXPLORATION</div>
    <div class="section-title">Explore Health Indicators</div>
    <div class="section-description">
        Choose an indicator to compare its distribution across
        the two outcome groups.
    </div>
    """, unsafe_allow_html=True)

    available_features = [
        col for col in [
            "Glucose",
            "BMI",
            "Age",
            "BloodPressure",
            "Insulin",
            "SkinThickness",
            "Pregnancies",
            "DiabetesPedigreeFunction"
        ]
        if col in dataset.columns
    ]

    if available_features:

        selected_feature = st.selectbox(
            "Choose a health indicator",
            available_features
        )

        chart_data = dataset[
            [selected_feature, "Outcome"]
        ].dropna().copy()

        # Exclude zero-coded missing measurements
        if selected_feature in [
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI"
        ]:

            chart_data = chart_data[
                chart_data[selected_feature] > 0
            ]

        if not chart_data.empty:

            v1, v2 = st.columns(2, gap="large")

            with v1:

                fig, ax = plt.subplots(figsize=(7, 4.5))

                sns.histplot(
                    data=chart_data,
                    x=selected_feature,
                    hue="Outcome",
                    kde=True,
                    palette={
                        0: CARAMEL,
                        1: DARK
                    },
                    alpha=.40,
                    ax=ax
                )

                ax.set_title(
                    f"{selected_feature} Distribution",
                    fontsize=14,
                    weight="bold",
                    color=DARK
                )

                ax.set_xlabel(selected_feature)
                ax.set_ylabel("Number of Records")
                ax.set_facecolor(CREAM)
                fig.patch.set_facecolor(CREAM)

                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)

            with v2:

                fig, ax = plt.subplots(figsize=(7, 4.5))

                sns.boxplot(
                    data=chart_data,
                    x="Outcome",
                    y=selected_feature,
                    order=[0, 1],
                    palette=[CARAMEL, DARK],
                    width=.5,
                    ax=ax
                )

                ax.set_xticks([0, 1])
                ax.set_xticklabels(["Negative", "Positive"])

                ax.set_title(
                    f"{selected_feature} by Outcome",
                    fontsize=14,
                    weight="bold",
                    color=DARK
                )

                ax.set_xlabel("Diabetes Outcome")
                ax.set_ylabel(selected_feature)
                ax.set_facecolor(CREAM)
                fig.patch.set_facecolor(CREAM)

                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)

            group_means = chart_data.groupby(
                "Outcome"
            )[selected_feature].mean()

            if 0 in group_means.index and 1 in group_means.index:

                st.markdown(f"""
                <div class="info-panel">
                    <b>✨ Indicator Summary — {selected_feature}</b><br><br>
                    Negative group average:
                    <b>{group_means[0]:.2f}</b><br>
                    Positive group average:
                    <b>{group_means[1]:.2f}</b><br><br>
                    These are descriptive group averages. They do not
                    establish that the indicator causes diabetes.
                </div>
                """, unsafe_allow_html=True)

        else:

            st.warning(
                "There are no valid measurements available for this indicator."
            )

    else:

        st.warning(
            "No recognised health-indicator columns were found in this dataset."
        )

    st.write("")

    # ======================================
    # CORRELATION ANALYSIS
    # ======================================

    st.markdown("""
    <div class="section-kicker">RELATIONSHIP ANALYSIS</div>
    <div class="section-title">Health Indicator Correlation Map</div>
    <div class="section-description">
        Explore statistical relationships between numerical health features.
    </div>
    """, unsafe_allow_html=True)

    correlation_data = dataset.select_dtypes(
        include="number"
    )

    if correlation_data.shape[1] >= 2:

        correlation = correlation_data.corr()

        fig, ax = plt.subplots(figsize=(10, 7))

        sns.heatmap(
            correlation,
            annot=True,
            fmt=".2f",
            cmap=sns.blend_palette(
                ["#684638", "#D9B98C", "#FFF8EF"],
                as_cmap=True
            ),
            center=0,
            linewidths=1,
            linecolor=CREAM,
            square=True,
            annot_kws={"size": 9},
            ax=ax
        )

        ax.set_title(
            "Correlation Between Health Features",
            fontsize=16,
            weight="bold",
            color=DARK,
            pad=16
        )

        fig.patch.set_facecolor(CREAM)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        st.caption(
            "Correlation measures statistical association. "
            "It does not prove cause and effect."
        )

        if "Outcome" in correlation.columns:

            outcome_corr = (
                correlation["Outcome"]
                .drop("Outcome")
                .dropna()
            )

            outcome_corr = outcome_corr.reindex(
                outcome_corr.abs().sort_values(
                    ascending=False
                ).index
            )

            if not outcome_corr.empty:

                top_feature = outcome_corr.index[0]
                top_value = outcome_corr.iloc[0]

                st.markdown(f"""
                <div class="insight-card">
                    <h4>🔍 Key Data Observation</h4>
                    <p>
                        <b>{top_feature}</b> has the strongest absolute
                        correlation with Outcome in this dataset,
                        with a correlation coefficient of
                        <b>{top_value:.2f}</b>.
                    </p>
                    <p>
                        This represents an association, not a causal
                        relationship.
                    </p>
                </div>
                """, unsafe_allow_html=True)

    else:

        st.info(
            "Not enough numeric columns are available for correlation analysis."
        )

    # ======================================
    # DATASET PREVIEW
    # ======================================

    with st.expander("📋 View Dataset Sample"):

        st.dataframe(
            dataset.head(20),
            use_container_width=True,
            hide_index=True
        )


# ==========================================
# METHODOLOGY
# ==========================================

st.write("")

st.markdown("""
<div class="section-kicker">05 / BEHIND THE TECHNOLOGY</div>
<div class="section-title">How DiaSense AI Works</div>
<div class="section-description">
    The technologies and machine learning approach behind this application.
</div>
""", unsafe_allow_html=True)

t1, t2 = st.columns(2, gap="large")

with t1:

    st.markdown("""
    <div class="insight-card">
        <h4>🧠 Machine Learning</h4>
        <p><b>Algorithm:</b> Logistic Regression</p>
        <p><b>Learning Type:</b> Supervised Learning</p>
        <p><b>Problem:</b> Binary Classification</p>
        <p><b>Input Variables:</b> 8 Health Features</p>
        <p><b>Data Split:</b> 80% Training / 20% Testing</p>
    </div>
    """, unsafe_allow_html=True)

with t2:

    st.markdown("""
    <div class="insight-card">
        <h4>⚙️ Technology Stack</h4>
        <p><b>Programming:</b> Python</p>
        <p><b>Data Analysis:</b> Pandas, NumPy</p>
        <p><b>Visualisation:</b> Matplotlib, Seaborn</p>
        <p><b>Machine Learning:</b> Scikit-learn</p>
        <p><b>Application:</b> Streamlit</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.html("""
<div class="insight-footer">
    <h3>🩺 DiaSense AI</h3>
    <p>Healthcare Intelligence • Machine Learning • Data Analytics</p>
    <p>
        Educational project only. Not a substitute for professional
        medical advice or diagnosis.
    </p>
</div>
""")
