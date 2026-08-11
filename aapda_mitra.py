import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import plotly.graph_objects as go
import plotly.express as px
import random
import time

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Aapda Mitra Command Center",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #f4f7fb;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #073b66;
        margin-bottom: 0px;
    }

    .subtitle {
        color: #5b6573;
        font-size: 17px;
        margin-bottom: 10px;
    }

    .online {
        background: #dff7e8;
        color: #137333;
        padding: 8px 15px;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
    }

    .risk-high {
        background: linear-gradient(135deg, #7f0000, #d32f2f);
        color: white;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
    }

    .risk-medium {
        background: linear-gradient(135deg, #e65100, #ff9800);
        color: white;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
    }

    .risk-low {
        background: linear-gradient(135deg, #1b5e20, #43a047);
        color: white;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
    }

    .risk-percent {
        font-size: 55px;
        font-weight: 900;
    }

    .risk-title {
        font-size: 24px;
        font-weight: 800;
    }

    .panel {
        background: white;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #e2e7ee;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.05);
    }

    .alert-panel {
        background: #fff3f3;
        border-left: 6px solid #d32f2f;
        border-radius: 10px;
        padding: 18px;
    }

    .success-panel {
        background: #edf8f0;
        border-left: 6px solid #2e7d32;
        border-radius: 10px;
        padding: 18px;
    }

    .ai-panel {
        background: #eef5ff;
        border-left: 6px solid #1976d2;
        border-radius: 10px;
        padding: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================

header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.markdown(
        '<div class="main-title">🌊 AI AAPDA MITRA</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-Powered Village Flood Early Warning & Response System'
        '</div>',
        unsafe_allow_html=True
    )

with header_col2:
    st.markdown(
        '<div class="online">🟢 SYSTEM ONLINE</div>',
        unsafe_allow_html=True
    )

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏘️ Command Center")

village = st.sidebar.selectbox(
    "Select Village",
    [
        "Phillaur",
        "Ludhiana Rural",
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

st.sidebar.subheader("⚙️ Demo Controls")

demo_mode = st.sidebar.checkbox(
    "Enable Demo Mode",
    value=True
)

force_high = st.sidebar.checkbox(
    "🚨 Force HIGH Risk Demo",
    value=False
)

st.sidebar.divider()

st.sidebar.info(
    "Prototype Mode\n\n"
    "Rainfall, river and wind readings are simulated. "
    "Real deployment would use verified weather and IoT data."
)

# ============================================================
# ML MODEL
# ============================================================

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

# ============================================================
# ANALYZE BUTTON
# ============================================================

st.subheader(f"📍 Monitoring Village: {village}")

analyze = st.button(
    "🔍 ANALYZE CURRENT FLOOD RISK",
    type="primary",
    use_container_width=True
)

# ============================================================
# INITIAL SCREEN
# ============================================================

if not analyze:

    st.info(
        "👆 Select a village and click "
        "**ANALYZE CURRENT FLOOD RISK** to start."
    )

    st.subheader("🛡️ AI Aapda Mitra Capabilities")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("### 🌧️")
        st.write("Rainfall Monitoring")

    with c2:
        st.markdown("### 🌊")
        st.write("River Level Analysis")

    with c3:
        st.markdown("### 🤖")
        st.write("AI Flood Prediction")

    with c4:
        st.markdown("### 📞")
        st.write("Emergency Response")

    st.divider()

    st.markdown(
        """
        ### 🎯 Mission

        **Predict floods early. Alert villages faster. Save lives.**

        The prototype combines rainfall data, river-level information
        and machine-learning-based risk prediction into one village
        disaster-management dashboard.
        """
    )

# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    with st.spinner("🧠 AI analyzing environmental conditions..."):
        time.sleep(1)

        if force_high:
            current_rain = random.randint(160, 220)
            current_river = round(random.uniform(7.0, 9.0), 1)
            wind_speed = random.randint(55, 85)
        else:
            current_rain = random.randint(40, 220)
            current_river = round(random.uniform(2.0, 9.0), 1)
            wind_speed = random.randint(15, 75)

        prediction = model.predict(
            [[current_rain, current_river]]
        )[0]

        probability = model.predict_proba(
            [[current_rain, current_river]]
        )[0][1]

        if force_high:
            probability = max(probability, 0.87)

    # ========================================================
    # RISK CLASSIFICATION
    # ========================================================

    if probability >= 0.70:
        risk_level = "HIGH"
        risk_class = "risk-high"
        risk_emoji = "🚨"
        risk_color = "#d32f2f"

    elif probability >= 0.40:
        risk_level = "MEDIUM"
        risk_class = "risk-medium"
        risk_emoji = "⚠️"
        risk_color = "#f57c00"

    else:
        risk_level = "LOW"
        risk_class = "risk-low"
        risk_emoji = "✅"
        risk_color = "#2e7d32"

    # ========================================================
    # TOP METRICS
    # ========================================================

    st.subheader("📡 Live Environmental Intelligence")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric(
            "🌧️ Rainfall",
            f"{current_rain} mm",
            "Current"
        )

    with m2:
        st.metric(
            "🌊 River Level",
            f"{current_river} m",
            "Current"
        )

    with m3:
        st.metric(
            "💨 Wind Speed",
            f"{wind_speed} km/h",
            "Current"
        )

    with m4:
        st.metric(
            "🤖 AI Confidence",
            f"{int(probability * 100)}%",
            "Flood Probability"
        )

    st.divider()

    # ========================================================
    # RISK + GAUGE
    # ========================================================

    left, right = st.columns([1, 1.5])

    with left:

        st.markdown(
            f"""
            <div class="{risk_class}">
                <div class="risk-percent">
                    {risk_emoji} {int(probability * 100)}%
                </div>
                <div class="risk-title">
                    FLOOD RISK: {risk_level}
                </div>
                <br>
                Village: <b>{village}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=probability * 100,
                title={"text": "AI Flood Risk Score"},
                gauge={
                    "axis": {
                        "range": [0, 100]
                    },
                    "bar": {
                        "color": risk_color
                    },
                    "steps": [
                        {
                            "range": [0, 40],
                            "color": "#c8e6c9"
                        },
                        {
                            "range": [40, 70],
                            "color": "#ffe0b2"
                        },
                        {
                            "range": [70, 100],
                            "color": "#ffcdd2"
                        }
                    ]
                }
            )
        )

        gauge.update_layout(
            height=260,
            margin=dict(l=20, r=20, t=50, b=10)
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    st.divider()

    # ========================================================
    # 6-HOUR FORECAST
    # ========================================================

    st.subheader("📈 6-Hour Flood Risk Forecast")

    hours = [
        "Now",
        "+1h",
        "+2h",
        "+3h",
        "+4h",
        "+5h",
        "+6h"
    ]

    base_risk = probability * 100

    forecast = [
        max(5, min(99, base_risk + random.randint(-5, 3)))
        for _ in hours
    ]

    forecast[0] = base_risk

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=hours,
            y=forecast,
            mode="lines+markers",
            line=dict(
                color=risk_color,
                width=5
            ),
            marker=dict(
                size=10
            ),
            fill="tozeroy",
            fillcolor="rgba(211,47,47,0.10)"
        )
    )

    fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="#d32f2f",
        annotation_text="High Risk Threshold"
    )

    fig.update_layout(
        yaxis=dict(
            title="Flood Risk (%)",
            range=[0, 100]
        ),
        xaxis=dict(
            title="Time"
        ),
        height=360,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ========================================================
    # MAP / VILLAGE STATUS
    # ========================================================

    st.subheader("🗺️ Village Risk Overview")

    village_data = pd.DataFrame(
        {
            "Village": [
                "Phillaur",
                "Ludhiana Rural",
                "Jagraon",
                "Samrala",
                "Khanna"
            ],
            "Risk": [
                random.randint(20, 95),
                random.randint(20, 80),
                random.randint(20, 90),
                random.randint(10, 75),
                random.randint(10, 65)
            ]
        }
    )

    selected_index = village_data[
        village_data["Village"] == village
    ].index[0]

    village_data.loc[selected_index, "Risk"] = int(
        probability * 100
    )

    village_data["Status"] = village_data["Risk"].apply(
        lambda x:
        "HIGH" if x >= 70
        else "MEDIUM" if x >= 40
        else "LOW"
    )

    fig_map = px.scatter(
        village_data,
        x="Village",
        y="Risk",
        size="Risk",
        color="Status",
        color_discrete_map={
            "HIGH": "#d32f2f",
            "MEDIUM": "#f57c00",
            "LOW": "#2e7d32"
        },
        hover_data=["Risk"],
        title="Demo Village Risk Map"
    )

    fig_map.update_layout(
        yaxis_title="Flood Risk (%)",
        xaxis_title="Village",
        yaxis=dict(range=[0, 100]),
        height=380,
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )

    # ========================================================
    # AI EXPLANATION
    # ========================================================

    st.subheader("🧠 AI Decision Explanation")

    reason_rain = min(
        100,
        int((current_rain / 220) * 100)
    )

    reason_river = min(
        100,
        int((current_river / 9) * 100)
    )

    reason_history = random.randint(60, 90)

    e1, e2, e3 = st.columns(3)

    with e1:
        st.metric(
            "🌧️ Rainfall Factor",
            f"{reason_rain}%"
        )

    with e2:
        st.metric(
            "🌊 River Factor",
            f"{reason_river}%"
        )

    with e3:
        st.metric(
            "📚 Historical Pattern",
            f"{reason_history}%"
        )

    st.markdown(
        f"""
        <div class="ai-panel">
        <b>🤖 AI Assessment</b><br><br>
        The model is evaluating rainfall intensity and river level
        together to estimate the probability of flooding.
        <br><br>
        <b>Current prediction:</b> {risk_level} flood risk
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # EMERGENCY RESPONSE
    # ========================================================

    st.divider()

    st.subheader("🚨 Emergency Response Center")

    e1, e2, e3 = st.columns(3)

    with e1:

        st.markdown(
            """
            <div class="panel">
            <h3>📞 Sarpanch</h3>
            <b>STATUS:</b> READY
            </div>
            """,
            unsafe_allow_html=True
        )

    with e2:

        st.markdown(
            """
            <div class="panel">
            <h3>📢 Village Broadcast</h3>
            <b>STATUS:</b> READY
            </div>
            """,
            unsafe_allow_html=True
        )

    with e3:

        st.markdown(
            """
            <div class="panel">
            <h3>🚑 Rescue Team</h3>
            <b>STATUS:</b> ON STANDBY
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if risk_level == "HIGH":

        st.markdown(
            """
            <div class="alert-panel">
            <b>🚨 HIGH RISK ALERT</b><br>
            Immediate emergency communication is recommended
            in a real deployment.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        alert_button = st.button(
            "🚨 SEND EMERGENCY ALERT",
            type="primary",
            use_container_width=True
        )

        if alert_button:

            st.success(
                f"✅ Emergency alert generated for {village}"
            )

            st.info(
                f"📱 Sarpanch: {sarpanch_mobile}"
            )

            st.warning(
                f"🚨 ALERT MESSAGE\n\n"
                f"AI Aapda Mitra Warning: {village} me "
                f"flood risk HIGH hai. Kripya surakshit "
                f"uchai wali jagah par jaane ki taiyari karein."
            )

            st.caption(
                "DEMO ONLY — No real SMS, IVR or emergency "
                "communication has been sent."
            )

    elif risk_level == "MEDIUM":

        st.warning(
            "⚠️ Medium risk. Continue monitoring conditions."
        )

    else:

        st.markdown(
            """
            <div class="success-panel">
            <b>🟢 CURRENT STATUS: STABLE</b><br>
            No immediate high flood risk detected.
            </div>
            """,
            unsafe_allow_html=True
        )

    # ========================================================
    # ALERT PREVIEW
    # ========================================================

    st.divider()

    st.subheader("📱 Village Alert Preview")

    alert_col1, alert_col2 = st.columns(2)

    with alert_col1:

        st.markdown(
            f"""
            <div class="panel">

            <h3>🚨 AI Aapda Mitra Alert</h3>

            <b>Village:</b> {village}<br><br>

            <b>Flood Risk:</b> {risk_level}<br>

            <b>Probability:</b> {int(probability * 100)}%<br>

            <b>River Level:</b> {current_river} m<br>

            <b>Rainfall:</b> {current_rain} mm<br><br>

            ⚠️ Please remain alert and follow
            local emergency instructions.

            </div>
            """,
            unsafe_allow_html=True
        )

    with alert_col2:

        st.markdown(
            """
            <div class="panel">

            <h3>🛡️ Response Plan</h3>

            1️⃣ Alert village leadership<br><br>

            2️⃣ Notify residents<br><br>

            3️⃣ Prepare evacuation routes<br><br>

            4️⃣ Keep rescue teams ready<br><br>

            5️⃣ Monitor river and rainfall continuously

            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🌊 AI Aapda Mitra | Prototype Command Center"
)

st.caption(
    "Demo data is simulated. Real deployment requires "
    "validated weather data, calibrated sensors and "
    "authorized emergency communication systems."
)
