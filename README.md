# 🩺 DiaSense AI
### Diabetes Prediction & Interactive Health Analytics

DiaSense AI is an interactive machine learning application that predicts the likelihood of diabetes using **Logistic Regression** and provides an interactive dashboard for exploring diabetes-related health data.

The application combines machine learning predictions, probability analysis, model evaluation, and health data visualisation in a modern multi-page Streamlit interface.

## ✨ Key Features

### 1. Diabetes Prediction
- Predicts diabetes outcomes using eight health-related input features.
- Uses a trained Logistic Regression model.
- Displays prediction results with probability percentages.
- Provides an interactive input interface.

### 2. Interactive Health Analytics
- Upload a diabetes dataset in CSV format.
- Explore dataset distributions and health indicators.
- Visualise relationships between health features.
- Analyse correlations through interactive charts.
- Compare health indicators across diabetes outcome groups.

### 3. Model Performance
- Confusion matrix visualisation.
- Classification performance metrics.
- Accuracy, precision, recall, and F1-score.
- Model methodology and evaluation information.

### 4. Prediction History
- Maintains prediction history during the application session.
- Download prediction records as a CSV file.
- Clear previous prediction history.

## 🧠 Machine Learning Model

**Algorithm:** Logistic Regression

**Problem Type:** Binary Classification

**Input Features:**

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

**Recorded Confusion Matrix:**

| Metric | Value |
|---|---:|
| True Negatives | 84 |
| False Positives | 15 |
| False Negatives | 17 |
| True Positives | 38 |
| Accuracy | 79.22% |
| Precision | 71.70% |
| Recall | 69.09% |
| F1-Score | 70.37% |

*These metrics are based on the recorded confusion matrix displayed in the application.*

## 🛠️ Technology Stack

- **Programming:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualisation:** Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Model Storage:** Pickle
- **Development:** Jupyter Notebook

## 📂 Project Structure

```text
Diabetes_Streamlit/
│
├── app.py
├── utils.py
├── stream.pkl
├── requirements.txt
├── machinepro.ipynb
│
└── pages/
    ├── 2_Prediction.py
    └── 3_Insights.py
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/namrataamali/Diabetes_Streamlit.git
```

### 2. Navigate to the project folder

```bash
cd Diabetes_Streamlit
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

The Insights page supports CSV dataset uploads for interactive data exploration.

Upload a compatible diabetes dataset containing the required health features and an outcome column to explore distributions, comparisons, and correlations.

## ⚠️ Disclaimer

DiaSense AI is an educational machine learning project developed for learning and demonstration purposes. Its predictions are not medical diagnoses and should not replace professional medical advice.

## 👩‍💻 Developed By

**Namrata Mali**

[GitHub Profile](https://github.com/namrataamali)

[Project Repository](https://github.com/namrataamali/Diabetes_Streamlit)
