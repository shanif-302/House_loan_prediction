import streamlit as st
import pickle
import numpy as np
from pathlib import Path


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    color:#CBD5E1;
    font-size:18px;
    margin-bottom:25px;
}

.prediction{
    background:#16a34a;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:32px;
    color:white;
    font-weight:bold;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "HSP.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# -----------------------------
# Title
st.markdown(
    "<div class='main-title'>🏠 House Price Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Predict the estimated price of your dream house.</div>",
    unsafe_allow_html=True
)

# CSS

st.markdown("""
<style>

/* Make all widget labels consistent */
[data-testid="stWidgetLabel"] p {
    color: #F8FAFC !important;
    font-size: 16px !important;
    font-weight: normal !important;
    font-family: "Source Sans Pro", sans-serif !important;
}

/* Toggle text */
[data-testid="stToggle"] p {
    color: #F8FAFC !important;
    font-size: 16px !important;
    font-weight: normal !important;
}

/* Selectbox text */
[data-testid="stSelectbox"] label p {
    color: #F8FAFC !important;
    font-size: 16px !important;
    font-weight: normal !important;
}

</style>
""", unsafe_allow_html=True)



# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📋 Model Information")

st.sidebar.info("""
**Machine Learning Model**

• House Price Prediction

• Input Features : 13

• Developed using Scikit-Learn

• Streamlit Dashboard
""")

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "Area (sq ft)",
        min_value=500,
        max_value=20000,
        value=5000,
        step=100
    )
    furnishing = st.selectbox(
        "Furnishing Status",
        (
            "Furnished",
            "Semi-Furnished",
            "Unfurnished"
        )
    )

    bedrooms = st.slider(
        "Bedrooms",
        1,
        10,
        3
    )

    bathrooms = st.slider(
        "Bathrooms",
        1,
        10,
        2
    )

    stories = st.slider(
        "Stories",
        1,
        5,
        2
    )

    parking = st.slider(
        "Parking Spaces",
        0,
        5,
        1
    )

with col2:

    mainroad = st.segmented_control(
    "Main Road",
    options=["No", "Yes"],
    default="No"
) == "Yes"
    
    guestroom = st.segmented_control(
    "Guest Room",
    options=["No", "Yes"],
    default="No"
) == "Yes"

    basement = st.segmented_control(
    "Basement",
    options=["No", "Yes"],
    default="No"
) == "Yes"

    hotwaterheating = st.segmented_control(
    "Hot Water Heating",
    options=["No", "Yes"],
    default="No"
) == "Yes"

    airconditioning = st.segmented_control(
    "Air Conditioning",
    options=["No", "Yes"],
    default="No"
) == "Yes"

    prefarea = st.segmented_control(
    "Preferred Area",
    options=["No", "Yes"],
    default="No"
) == "Yes"




# -----------------------------
# One Hot Encoding
# -----------------------------
semi = 0
unfurnished = 0

if furnishing == "Semi-Furnished":
    semi = 1

elif furnishing == "Unfurnished":
    unfurnished = 1

# -----------------------------
# Prediction
# -----------------------------
if st.button(" Predict House Price", use_container_width=True):

    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        int(mainroad),
        int(guestroom),
        int(basement),
        int(hotwaterheating),
        int(airconditioning),
        parking,
        int(prefarea),
        semi,
        unfurnished
    ]])

    # Uncomment if scaler used
    # features = scaler.transform(features)

    prediction = model.predict(features)[0]

    st.markdown(
        f"""
        <div class="prediction">
        Estimated Price<br><br>
        ₹ {prediction:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.caption("Designed with ❤️ using Streamlit")