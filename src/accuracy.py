from src.preprocessing import clean_text
from src.aspect_extraction import extract_aspects
from src.sentiment import get_sentiment
from src.ml_aspect import predict_aspects

def calculate_accuracy():
    test_data = [
        ("camera acha hai", {"camera": "Positive"}),
        ("battery kharab hai", {"battery": "Negative"}),
        ("memory kam hai", {"storage": "Negative"}),
        ("camera acha hai lekin battery bekar hai", {"camera": "Positive", "battery": "Negative"}),
        ("phone slow hai", {"performance": "Negative"}),
        ("camera mast hai", {"camera": "Positive"}),
        ("battery drains fast", {"battery": "Negative"}),
        ("storage acha hai", {"storage": "Positive"}),
        ("camera acha hai aur storage bhi acha hai", {"camera": "Positive", "storage": "Positive"}),
        ("camera bekar hai lekin battery good hai", {"camera": "Negative", "battery": "Positive"})
    ]

    correct = 0
    total = 0

    for text, expected in test_data:
        cleaned = clean_text(text)

        rule_aspects = extract_aspects(cleaned)
        ml_aspects = predict_aspects(cleaned)

        final_aspects = list(set(rule_aspects + ml_aspects))

        pred_sentiment = get_sentiment(cleaned, final_aspects)

        for aspect in expected:
            total += 1
            if aspect in pred_sentiment and pred_sentiment[aspect] == expected[aspect]:
                correct += 1

    accuracy = correct / total * 100
    print(f"\n🔥 Accuracy: {accuracy:.2f}%")

# 🔥 IMPORTANT — function ke bahar hona chahiye
if __name__ == "__main__":
    calculate_accuracy()