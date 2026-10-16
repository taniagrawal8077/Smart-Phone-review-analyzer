import streamlit as st
import matplotlib.pyplot as plt

from src.recommendation import recommend_based_on_preferences
from src.preprocessing import clean_text
from src.aspect_extraction import extract_aspects
from src.sentiment import get_sentiment
from src.explanation import explain_sentiment
from src.ml_aspect import predict_aspects

st.set_page_config(page_title="Aspect Sentiment Analyzer", layout="centered")

st.title("📊 Smart Phone Review Analyzer")
st.write("Get insights from reviews and find if the phone suits your needs.")

# 🔥 User 1 (review)
review = st.text_area("🗣️ Customer Review (User 1):")

# 🔥 User 2 (shopkeeper style 😎)
user_pref = st.text_input(
    "🛍️ What features are you focusing on? (e.g., camera, battery, performance)"
)

if st.button("Analyze"):

    if review.strip() == "":
        st.warning("Please enter a review!")
    else:
        cleaned = clean_text(review)

        # aspects
        rule_aspects = extract_aspects(cleaned)
        ml_aspects = predict_aspects(cleaned)
        final_aspects = list(set(rule_aspects + ml_aspects))

        # sentiment + explanation
        sentiments = get_sentiment(cleaned, final_aspects)
        explanations = explain_sentiment(cleaned, final_aspects)

        st.subheader("🔍 Results")

        st.write("**Cleaned Text:**", cleaned)
        st.write("**Detected Aspects:**", final_aspects)

        # ---------------------------
        # 📌 SENTIMENT
        # ---------------------------
        st.write("### 📌 Sentiment")
        for aspect, sentiment in sentiments.items():
            if sentiment == "Positive":
                st.success(f"{aspect} → {sentiment}")
            elif sentiment == "Negative":
                st.error(f"{aspect} → {sentiment}")
            else:
                st.warning(f"{aspect} → {sentiment}")

        # ---------------------------
        # 💡 EXPLANATION
        # ---------------------------
        st.write("### 💡 Explanation")
        for aspect, exp in explanations.items():
            st.write(f"**{aspect}:** {', '.join(exp) if exp else 'No strong keywords found'}")

        # ---------------------------
        # 📊 BAR CHART
        # ---------------------------
        st.write("### 📊 Aspect-wise Sentiment")

        aspect_names = list(sentiments.keys())
        scores = []

        for s in sentiments.values():
            if s == "Positive":
                scores.append(1)
            elif s == "Negative":
                scores.append(-1)
            else:
                scores.append(0)

        fig, ax = plt.subplots()
        ax.bar(aspect_names, scores)
        ax.set_title("Aspect Sentiment Score")
        ax.set_ylabel("1 = Positive, -1 = Negative, 0 = Neutral")

        st.pyplot(fig)

        # ---------------------------
        # 🤖 RECOMMENDATION (FIXED 🔥)
        # ---------------------------
        if user_pref.strip() != "":

            # 👉 STRING hi pass kar (IMPORTANT FIX)
            recommendation = recommend_based_on_preferences(user_pref, sentiments)

            st.write("### 🤖 Recommendation for User")
            st.success(recommendation)

        else:
            st.info("💬 Tell me what matters to you, and I'll suggest if this phone is right for you.")