<div align="center">

# 🎓 Student Exam Score Predictor

**Predict a student's exam score from their daily habits — powered by Linear Regression.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://hassan9255-student-score-prediction-app-lo6er5.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

**R² = 0.90** · Average error of just **4.1 points** out of 100

[**Try the live app →**](https://student-score-prediction-jne8k6eufr92baygyousen.streamlit.app/)

</div>

---

## 📖 Overview

How much does an extra hour of studying actually raise your exam score? What does
scrolling social media cost you?

This project answers those questions with a **Linear Regression** model trained on
1,000 student records. It ships as an interactive **Streamlit** web app where you
move seven sliders and get a predicted exam score instantly.

The whole analysis — exploring the data, choosing features, training, evaluating
and comparing against other algorithms — lives in a single readable notebook.

---

## 🎯 Results

Scored on **200 students the model never saw during training**.

| Metric | Score | What it means |
|:---|:---:|:---|
| **R²** | **0.8996** | Explains 90% of the variation in exam scores |
| **RMSE** | 5.07 points | Typical size of an error |
| **MAE** | 4.11 points | Average miss, on a 0–100 scale |
| **Cross-validated R²** | 0.8984 ± 0.016 | Confirms it wasn't a lucky split |
| **Training R²** | 0.9009 | Matches test score → no overfitting |

> **In plain English:** the app's prediction is usually within **about 4 points**
> of the student's real score.

<details>
<summary><b>Why R² and not "accuracy"?</b></summary>

<br>

Accuracy is a *classification* metric — the share of predictions that are exactly
right. This is a *regression* problem producing a number on a continuous scale, so
a prediction is essentially never exactly correct; it's just close. R² is the
standard measure of fit for regression, and MAE gives the friendlier
"off by about 4 points" reading.

</details>

---

## 💡 What the model learned

Linear Regression is fully transparent — the entire model is seven numbers.

| Feature | Effect on exam score |
|:---|:---|
| 📚 **Study hours per day** | **+9.54** points per hour |
| 📱 Social media hours per day | −2.70 points per hour |
| 📺 Netflix hours per day | −2.32 points per hour |
| 😴 Sleep hours per night | +1.99 points per hour |
| 🧠 Mental health rating | +1.95 points per point |
| 🏃 Exercise sessions per week | +1.32 points per session |
| ✅ Attendance percentage | +0.15 points per percent |

> **Key insight:** one extra hour of study per day outweighs roughly
> **three and a half hours** of avoided social media.

---

## 🚀 Quick start

```bash
# 1. Clone the repo
git clone https://github.com/hassan9255/Student-Score-Prediction.git
cd Student-Score-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Retrain the model — best_model.pkl is already included
jupyter notebook notebook.ipynb   # then Run All

# 4. Launch the web app
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 📁 Project structure

```
Student-Score-Prediction/
├── notebook.ipynb                  # 📊 Full analysis: EDA → training → evaluation
├── app.py                          # 🎨 Streamlit web app
├── best_model.pkl                  # 🤖 Trained Linear Regression model
├── model_metrics.json              # 📈 Scores and coefficients
├── student_habits_performance.csv  # 📦 Dataset (1,000 students)
├── requirements.txt                # 🧩 Pinned dependencies
└── README.md                       # 📝 You are here
```

---

## 🔬 How it works

<table>
<tr><td width="40"><b>1</b></td><td><b>Load & inspect</b><br>1,000 rows, 16 columns. Check for missing values and duplicates.</td></tr>
<tr><td><b>2</b></td><td><b>Explore</b><br>Correlation heatmap, scatter plots with trend lines, box plots for categories.</td></tr>
<tr><td><b>3</b></td><td><b>Select features</b><br>Three candidate feature sets are <i>measured</i>, not guessed. Seven habit columns win.</td></tr>
<tr><td><b>4</b></td><td><b>Split</b><br>80/20 train/test with a fixed <code>random_state</code> so results reproduce exactly.</td></tr>
<tr><td><b>5</b></td><td><b>Train</b><br>Linear Regression fitted on the training set <i>only</i>.</td></tr>
<tr><td><b>6</b></td><td><b>Evaluate</b><br>Score on the untouched test set, then cross-validate as a second opinion.</td></tr>
<tr><td><b>7</b></td><td><b>Save</b><br>Refit on all 1,000 rows and export with <code>joblib</code>.</td></tr>
</table>

### Feature selection, measured

Only 7 of the 16 columns are used. The rest were tested and made the model
*worse* — extra columns carrying no signal just add noise to fit.

| Feature set | Columns | CV R² |
|:---|:---:|:---:|
| **7 habit columns** ✅ | 7 | **0.8984** |
| Habits + age | 8 | 0.8983 |
| Everything (one-hot encoded) | 23 | 0.8947 |

### Why Linear Regression?

Tree-based models were tried and every one scored **worse**:

| Model | Test R² |
|:---|:---:|
| **Linear Regression** ✅ | **0.900** |
| Gradient Boosting | 0.888 |
| Random Forest | 0.849 |
| Extra Trees | 0.849 |

Exam score here is close to a straight-line combination of the habit columns.
Tree models approximate a straight line with staircase steps, and with only 1,000
rows they spend their flexibility fitting noise. The simplest model is both the
**most accurate** and the **easiest to explain**.

---

## 🧰 Tech stack

| Category | Tools |
|:---|:---|
| **Language** | Python 3.10+ |
| **Data** | pandas · NumPy |
| **Machine Learning** | scikit-learn (Linear Regression) · joblib |
| **Visualization** | matplotlib · seaborn |
| **Web app** | Streamlit |
| **Deployment** | Streamlit Community Cloud |

---

## 📊 Dataset

[**Student Habits vs Academic Performance**](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance) — Kaggle · 1,000 rows × 16 columns

Covers study time, screen time, sleep, exercise, attendance, mental health rating
and demographics, with the final exam score as the target.

---

## 🔮 Possible improvements

- [ ] Add prediction intervals so the app shows a range, not just a point estimate
- [ ] Collect more rows — 1,000 is small for detecting weaker effects
- [ ] Add a "what if" mode showing how the score changes if study time increases
- [ ] Unit tests for the prediction pipeline

---

<div align="center">

**Built as a portfolio project.** Feedback and pull requests welcome.

⭐ Star this repo if you found it useful

</div>
