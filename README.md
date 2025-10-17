# 🎓 Student Exam Score Prediction App

A **Streamlit-based Machine Learning Web App** that predicts a student's **exam score** based on various behavioral and lifestyle factors such as **study habits, attendance, sleep patterns, and mental health**.

---

## 🚀 Live Demo
🔗 **Streamlit App:** [student-score-prediction-app-lo6er5.streamlit.app](https://hassan9255-student-score-prediction-app-lo6er5.streamlit.app/)

---

## 📊 Dataset
📦 Dataset Source (Kaggle):  
👉 [Student Habits vs Academic Performance](https://www.kaggle.com/) *(You can add the exact dataset URL if available)*

The dataset contains information about students’ study habits, attendance, mental health, sleep duration, and corresponding academic performance metrics.

---

## 🧠 Features & Workflow
- ✅ Load and explore dataset (check for missing values, duplicates, and descriptive statistics)  
- 📈 Visualize distributions, correlations, and feature relationships  
- 🔢 Encode categorical variables  
- 🤖 Train multiple regression models:  
  - Linear Regression  
  - Decision Tree Regressor  
  - Random Forest Regressor  
- ⚙️ Hyperparameter tuning for model optimization  
- 🏆 Model selection based on **RMSE** and **R² Score**  
- 💾 Save the best model using **joblib**  
- 🌐 Streamlit interface to take user inputs and display predictions dynamically  

---

## 🧰 Tools & Technologies Used
| Category | Tools |
|-----------|--------|
| **Programming Language** | Python |
| **Libraries** | pandas, numpy, scikit-learn, matplotlib, seaborn, joblib, streamlit |
| **Machine Learning** | Linear Regression, Decision Tree, Random Forest |
| **Deployment** | Streamlit Cloud |
| **Environment** | Jupyter Notebook, VS Code |

---

## 📁 Project Structure


Student-Score-Prediction/

- app.py                          # 🎯 Main Streamlit web app (frontend + model prediction)
- best_model.pkl                  # 💾 Trained machine learning model saved using joblib
- student_habits_performance.csv  # 📊 Dataset from Kaggle (Student Habits vs Academic Performance)
- requirements.txt                # 🧩 List of dependencies required for running the project
- README.md                       # 📝 Project documentation (this file)
