import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import random
import time

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Aapda Mitra",
    page_icon="🌊",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        color: #0b3d62;
        text-align: center;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .risk-high {
        background-color: #ffebee;
        border: 3px solid #d32f2f;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
    }

    .risk-medium {
        background-color: #fff8e1;
        border: 3px solid #f9a825;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
    }

    .risk-low {
        background-color: #e8f5e9;
        border: 3px solid #2e7d32;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
    }

    .risk-number {
        font-size: 48px;
        font-weight: 800;
    }

    .risk-label {
        font-size: 22px;
        font-weight: 700;
    }

    .info-box {
        background-color: white;
        border-radius: 12px;
        padding: 18px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

    .alert-box {
        background-color: #fff3e0;
        border-left: 6px solid #ef6c00;
        padding: 18px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">🌊 AI Aapda Mitra</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Village Flood Early Warning System</div>',
    unsafe_allow_html=True
)

st.caption(
    "Prototype Demo • AI + IoT + Weather Intelligence"
)

st.divider()

# --------------------------------------------------
# DEMO ML MODEL
# --------------------------------------------------

@st.cache_resource
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

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("🏘️ Village Control")

village = st.sidebar.selectbox(
    "Select Village",
    [
        "Ludhiana Rural",
        "Phillaur",
        "Jagraon",
        "Samrala",
        "Khanna"
    ]
)

sarpanch_mobile = st.sidebar.text_input(
    "Sarpanch Mobile",
    "+91 98xxxxxx12"
)

st.sidebar.divider()

st.sidebar.info(
    "Demo Mode\n\n"
    "Sensor readings are simulated for this prototype."
)

# --------------------------------------------------
# START PREDICTION
# --------------------------------------------------

st.subheader(f"📍 Monitoring: {village}")

check_button = st.button(
    "🔍 ANALYZE FLOOD RISK",
    type="primary",
    use_container_width=True
)

if check_button:

    with st.spinner("🧠 AI analyzing rainfall and river conditions..."):
        time.sleep(1.5)

        # Simulated sensor data
        current_rain = random.randint(40, 220)
        current_river = round(random.uniform(2.0, 9.0), 1)

        prediction = model.predict(
            [[current_rain, current_river]]
        )[0]

        probability = model.predict_proba(
            [[current_rain, current_river]]
        )[0][1]

    # --------------------------------------------------
    # SENSOR CARDS
    # --------------------------------------------------

    st.subheader("📡 Live Environmental Readings")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🌧️ Rainfall",
            f"{current_rain} mm",
            "Current Reading"
        )

    with col2:
        st.metric(
            "🌊 River Level",
            f"{current_river} m",
            "Current Reading"
        )

    with col3:
        st.metric(
            "🤖 AI Confidence",
            f"{int(probability * 100)}%",
            "Flood Probability"
        )

    st.divider()

    # --------------------------------------------------
    # RISK CLASSIFICATION
    # --------------------------------------------------

    if probability >= 0.70:

        risk_level = "HIGH"
        risk_class = "risk-high"
        risk_emoji = "🚨"

    elif probability >= 0.40:

        risk_level = "MEDIUM"
        risk_class = "risk-medium"
        risk_emoji = "⚠️"

    else:

        risk_level = "LOW"
        risk_class = "risk-low"
        risk_emoji = "✅"

    # --------------------------------------------------
    # BIG RISK DISPLAY
    # --------------------------------------------------

    st.markdown(
        f"""
        <div class="{risk_class}">
            <div class="risk-number">
                {risk_emoji} {int(probability * 100)}%
            </div>
            <div class="risk-label">
                FLOOD RISK: {risk_level}
            </div>
            <p>
                Village: <b>{village}</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # --------------------------------------------------
    # AI EXPLANATION
    # --------------------------------------------------

    st.subheader("🧠 Why is AI giving this warning?")

    reason1 = (
        "High rainfall detected"
        if current_rain >= 120
        else "Rainfall currently within moderate range"
    )

    reason2 = (
        "River level is elevated"
        if current_river >= 6
        else "River level currently within monitored range"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="info-box">
            🌧️ <b>Rainfall Analysis</b><br>
            {reason1}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="info-box">
            🌊 <b>River Analysis</b><br>
            {reason2}
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # EMERGENCY RESPONSE
    # --------------------------------------------------

    st.divider()

    st.subheader("🚨 Emergency Response")

    if risk_level == "HIGH":

        st.markdown(
            """
            <div class="alert-box">
            <b>HIGH RISK DETECTED</b><br>
            Immediate local authorities and village leadership
            should be notified in a real deployment.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "📞 SEND EMERGENCY ALERT",
            type="primary",
            use_container_width=True
        ):

            st.success(
                f"✅ Demo alert generated for {village}"
            )

            st.info(
                f"📱 Target: {sarpanch_mobile}"
            )

            st.warning(
                f"Message: AI Alert — {village} me flood risk "
                "detect hua hai. Kripya surakshit/uchai wali "
                "jagah par jaane ki taiyari karein."
            )

            st.caption(
                "Demo only: No real SMS or IVR call has been sent."
            )

    elif risk_level == "MEDIUM":

        st.warning(
            "⚠️ Medium risk detected. Continue monitoring "
            "rainfall and river level."
        )

    else:

        st.success(
            "✅ Current conditions show low flood risk."
        )

else:

    # --------------------------------------------------
    # INITIAL DASHBOARD
    # --------------------------------------------------

    st.info(
        "👆 Click **ANALYZE FLOOD RISK** to start the AI analysis."
    )

    st.subheader("🛡️ System Capabilities")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### 🌧️")
        st.write("Rainfall Monitoring")

    with col2:
        st.markdown("### 🌊")
        st.write("River Level Analysis")

    with col3:
        st.markdown("### 🤖")
        st.write("AI Risk Prediction")

    with col4:
        st.markdown("### 📞")
        st.write("Emergency Alert")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "AI Aapda Mitra | Prototype for Village Flood Early Warning"
)

st.caption(
    "Current demo uses simulated sensor data. "
    "Future deployment can integrate weather APIs, IoT river sensors, "
    "maps and verified emergency communication systems."
)
