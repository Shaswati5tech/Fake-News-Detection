
import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📌 About")
    st.write("""
    This application uses:

    - TF-IDF Vectorization
    - Logistic Regression
    - Natural Language Processing

    to classify news articles as Fake or Real.
    """)

    st.info("Model Accuracy: 98.4%")
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Dataset")

st.sidebar.write("Articles: 44,898")
st.sidebar.write("Fake: 23,481")
st.sidebar.write("Real: 21,417")

# Main Header
st.markdown(
    """
    <h1 style='text-align:center;'>
    📰 Fake News Detection System
    </h1>
    <h4 style='text-align:center;color:gray;'>
    AI-powered News Verification
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()
st.info(
    "🔍 Paste any news article and the AI model will determine whether it is Fake or Real."
)

# Input Area
news = st.text_area(
    "Paste a News Article",
    height=250,
    placeholder="Paste the complete news article here..."
)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    analyze = st.button("🔍 Analyze News", use_container_width=True)

if analyze:

    if news.strip() == "":
        st.warning("Please enter a news article.")
    else:

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)
        probability = model.predict_proba(news_vector)

        confidence = max(probability[0]) * 100

        st.divider()

        if prediction[0] == 0:
            st.error("🚨 FAKE NEWS DETECTED")
        else:
            st.success("✅ REAL NEWS DETECTED")

        st.metric(
            label="Confidence Score",
            value=f"{confidence:.2f}%"
        )

        st.progress(int(confidence))

st.divider()

st.caption(
    "Built using Python, Scikit-Learn, NLP and Streamlit"
)
