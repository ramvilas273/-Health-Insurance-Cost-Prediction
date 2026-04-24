# 📊 Health Insurance Cost Prediction

A Machine Learning project that predicts **medical insurance charges** based on user inputs like age, BMI, smoking status, etc.  
This project also includes a **Streamlit web application** for real-time predictions.

---

## 🚀 Project Overview

Insurance cost prediction is important for companies to manage risk and pricing.  
This project builds multiple ML models and selects the best-performing one to accurately predict insurance charges.

---

## 📁 Dataset

- File: `insurance.csv`

### Features:
- `age` – Age of the person  
- `sex` – Gender  
- `bmi` – Body Mass Index  
- `children` – Number of dependents  
- `smoker` – Smoking status  

### Target:
- `charges` – Insurance cost  

---

## ⚙️ Workflow

1. Data Cleaning  
2. Exploratory Data Analysis (EDA)  
3. Encoding Categorical Variables  
4. Feature Scaling  
5. Model Training  
6. Model Evaluation  
7. Model Selection  
8. Deployment (Streamlit App)  

---

## 🤖 Models Used

- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  
- Support Vector Regressor (SVR)  

---

## 📈 Model Performance

| Model              | R² Score | MAE     | RMSE    |
|------------------|---------|---------|---------|
| XGBoost          | **0.90** | 2510.50 | 4269.96 |
| Random Forest    | 0.89    | 2594.52 | 4550.28 |
| Linear Regression| 0.80    | 4198.11 | 5991.82 |
| SVR              | 0.41    | 5162.46 | 10416.26 |

✅ **Best Model: XGBoost**

---

## 🧠 Key Insights

- Smoking has a **major impact** on insurance cost  
- BMI and age significantly affect charges  
- Tree-based models perform better than linear models  
- XGBoost achieved the best accuracy  

---

## 💻 Streamlit App

The project includes an interactive web app where users can:

- Enter personal details  
- Get instant insurance cost predictions  

---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/insurance-cost-prediction.git
cd insurance-cost-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

---

## 📦 Required Files

- `app.py`  
- `insurance.csv`  
- `best_model.pkl`  
- `scaler.pkl`  
- `label_encoders_sex.pkl`  
- `label_encoders_smoker.pkl`  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Streamlit  

---

## 📌 Future Improvements

- Add more features  
- Hyperparameter tuning  
- Deploy to cloud  
- Add model explainability (SHAP)  

---

## 👨‍💻 Author

**Ram Vilas**  
Data Science Enthusiast  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
