"""Streamlit app that predicts a student's exam score.

Loads the Linear Regression model created by notebook.ipynb and turns the
slider values into a prediction.

    streamlit run app.py
"""

import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "best_model.pkl"
METRICS_PATH = HERE / "model_metrics.json"

st.set_page_config(page_title="Student Exam Score Predictor", page_icon="🎓")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None


@st.cache_data
def load_metrics():
    if not METRICS_PATH.exists():
        return None
    return json.loads(METRICS_PATH.read_text(encoding="utf-8"))


model = load_model()
if model is None:
    st.error(f"`{MODEL_PATH.name}` is missing. Run `notebook.ipynb` to create it.")
    st.stop()

st.title("🎓 Student Exam Score Predictor")
st.caption("Linear Regression trained on 1,000 student records.")

left, right = st.columns(2)
with left:
    study_hours = st.slider("Study hours per day", 0.0, 10.0, 3.0, 0.1)
    social_media_hours = st.slider("Social media hours per day", 0.0, 8.0, 2.0, 0.1)
    netflix_hours = st.slider("Netflix hours per day", 0.0, 6.0, 1.5, 0.1)
    attendance = st.slider("Attendance percentage", 50.0, 100.0, 85.0, 0.5)
with right:
    sleep_hours = st.slider("Sleep hours per night", 3.0, 11.0, 7.0, 0.1)
    exercise_frequency = st.slider("Exercise sessions per week", 0, 6, 3)
    mental_health = st.slider("Mental health rating (1 = poor, 10 = great)", 1, 10, 5)

if st.button("Predict Exam Score", type="primary"):
    # Column names and order must match FEATURES in train.py.
    input_df = pd.DataFrame(
        [
            {
                "study_hours_per_day": study_hours,
                "social_media_hours": social_media_hours,
                "netflix_hours": netflix_hours,
                "attendance_percentage": attendance,
                "sleep_hours": sleep_hours,
                "exercise_frequency": exercise_frequency,
                "mental_health_rating": mental_health,
            }
        ]
    )

    raw_score = float(model.predict(input_df)[0])
    # A straight line can run past the ends of the 0-100 scale.
    score = min(100.0, max(0.0, raw_score))

    st.success(f"🎯 Predicted Exam Score: **{score:.1f}** / 100")
    st.progress(score / 100)

    metrics = load_metrics()
    if metrics:
        st.caption(
            f"This model is off by about {metrics['test_mae']:.1f} points on average."
        )

with st.expander("How accurate is this model?"):
    metrics = load_metrics()
    if metrics:
        a, b, c = st.columns(3)
        a.metric("R² score", f"{metrics['test_r2']:.3f}")
        b.metric("RMSE", f"{metrics['test_rmse']:.2f}")
        c.metric("Average error", f"{metrics['test_mae']:.2f} pts")
        st.write(
            f"Measured on {metrics['n_test']} students the model never saw while "
            f"training. An R² of {metrics['test_r2']:.3f} means it explains about "
            f"{metrics['test_r2'] * 100:.0f}% of the differences in exam scores."
        )
        st.write("**What the model learned** (points per unit of each input):")
        st.dataframe(
            pd.DataFrame(
                sorted(
                    metrics["coefficients"].items(),
                    key=lambda kv: abs(kv[1]),
                    reverse=True,
                ),
                columns=["Feature", "Effect on score"],
            ),
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.write("Run `notebook.ipynb` to generate the metrics file.")
