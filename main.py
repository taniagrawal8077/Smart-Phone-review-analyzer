from src.preprocessing import clean_text
from src.aspect_extraction import extract_aspects
from src.sentiment import get_sentiment
from src.explanation import explain_sentiment
from src.ml_aspect import predict_aspects

print("===== USER INPUT TEST =====")
review = input("Enter your review: ")

cleaned = clean_text(review)

# 🔥 RULE-BASED
rule_aspects = extract_aspects(cleaned)

# 🔥 ML-BASED
ml_aspects = predict_aspects(cleaned)

# 🔥 FINAL COMBINED (MOST IMPORTANT)
# 🔥 keep only meaningful ML aspects
final_aspects = list(set(rule_aspects + ml_aspects))

# remove false ones (important)
valid_aspects = []
for asp in final_aspects:
    if asp in cleaned:   # only if word actually present
        valid_aspects.append(asp)

final_aspects = valid_aspects

# 🔥 SENTIMENT
sentiments = get_sentiment(cleaned, final_aspects)

# 🔥 EXPLANATION
explanations = explain_sentiment(cleaned, final_aspects)

print("\nResults:")
print("Cleaned:", cleaned)
print("Rule-based Aspects:", rule_aspects)
print("ML Predicted Aspects:", ml_aspects)
print("Final Aspects:", final_aspects)
print("Sentiment:", sentiments)
print("Aspect-wise Explanation:", explanations)
from src.accuracy import calculate_accuracy

# run accuracy
calculate_accuracy()