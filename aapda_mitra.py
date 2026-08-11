import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import random

st.set_page_config(
    page_title="AI Aapda Mitra",
    page_icon="🌊",
    layout="centered"
)

st.title("🌊 AI Aapda Mitra")
st.subheader("Gaon ke liye Flood Prediction System")
st.caption("Powered by AI | Viksit Bharat")

@st.cache_data
def train_model():
    data = {
        "rainfall": [20, 50, 80, 120, 30, 150, 200, 60, 180, 90],
        "river_level": [2.1, 3.0, 4.5, 6.0, 2.5, 7.2, 8.5, 3.5, 7.8, 4.8],
        "flood": [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    }

    df = pd.DataFrame(data)

    X = df[["rainfall", "river_level"]]
    y = df["flood"]

    model = LogisticRegression()
    model.fit(X, y)

    return model


model = train_model()

col1, col2 = st.columns(2)

with col1:
    village = st.selectbox(
        "Gaon Chuno",
        ["Ludhiana Rural", "Phillaur", "Jagraon", "Samrala", "Khanna"]
    )

with col2:
    sarpanch_mobile = st.text_input(
        "Sarpanch Mobile",
        "+91 98xxxxxx12"
    )

st.divider()

if st.button("🔍 Abhi Check Karo - Predict Flood Risk"):

    current_rain = random.randint(40, 220)
    current_river = round(random.uniform(2.0, 9.0), 1)

    prediction = model.predict(
        [[current_rain, current_river]]
    )[0]

    probability = model.predict_proba(
        [[current_rain, current_river]]
    )[0][1]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Current Rainfall",
            f"{current_rain} mm"
        )

    with col2:
        st.metric(
            "River Level",
            f"{current_river} m"
        )

    st.divider()

    if prediction == 1 and probability > 0.7:

        st.error(
            f"🚨 KHATRA! {village} me "
            f"{int(probability * 100)}% Flood ka chance"
        )

        st.warning(
            "2-3 ghante me 1-2 ft paani aa sakta hai."
        )

        st.info(
            "Kripya uchai wali jagah par jaane ke liye taiyar rahein."
        )

        if st.button("📞 Auto Alert Bhejo Sarpanch ko"):
            st.success(
                f"✅ Demo IVR Call + SMS bhej diya gaya: "
                f"{sarpanch_mobile}"
            )

            st.info(
                f"Message: AI Alert: {village} me flood risk. "
                "Kripya uchai wali jagah par jayen."
            )

    elif prediction == 1:

        st.warning(
            f"⚠️ Saavdhan! {village} me "
            f"{int(probability * 100)}% Flood chance."
        )

        st.info(
            "River level aur rainfall par nazar rakhein."
        )

    else:

        st.success(
            f"✅ Safe! {village} me abhi "
            "flood ka high risk detect nahi hua."
        )

st.divider()

st.write(
    "**Tech Stack:** Python, Scikit-learn, Streamlit"
)

st.write(
    "**Demo:** Random sensor data"
)

st.caption(
    "Real system me IMD API + IoT River Sensor + "
    "WhatsApp/IVR API integrate ki ja sakti hai."
)
