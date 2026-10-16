import re

def get_sentiment(text, aspects):
    text = text.lower()

    parts = re.split(r"lekin|but|aur|and", text)

    positive_words = [
        "good", "great", "amazing", "achi", "badiya", "mast",
        "awesome", "love", "best", "fantastic",
        "acha", "accha"
    ]

    negative_words = [
        "bad", "kharab", "bekar", "bekaar",
        "drains", "issue", "slow", "lag", "laggy", "kam"
    ]

    negation_words = ["not", "nahi", "na"]

    aspect_keywords = {
        "camera": ["camera"],
        "battery": ["battery"],
        "display": ["display", "screen"],
        "performance": ["performance", "slow", "lag", "laggy"],
        "sound": ["sound", "audio"],
        "build": ["build"],
        "storage": ["storage", "memory", "space"]
    }

    sentiments = {}

    def calculate_score(words):
        score = 0
        for i, word in enumerate(words):

            if word in negative_words:
                score -= 1

            elif word in positive_words:

                # negation
                if i > 0 and words[i - 1] in negation_words:
                    score -= 1
                elif i < len(words)-1 and words[i + 1] in negation_words:
                    score -= 1
                else:
                    score += 1

        return score

    # 🔥 MAIN LOGIC
    for aspect in aspects:
        keywords = aspect_keywords.get(aspect, [])
        total_score = 0

        for part in parts:
            words = part.split()

            # ✅ agar is part me koi bhi aspect hai
            if any(k in words for k in keywords):

                # 🔥 IMPORTANT: score of entire part
                part_score = calculate_score(words)

                # 🔥 assign to ALL aspects present in this part
                total_score += part_score

        # fallback (rare case)
        if total_score == 0:
            words = text.split()
            if any(k in words for k in keywords):
                total_score = calculate_score(words)

        # label
        if total_score > 0:
            sentiments[aspect] = "Positive"
        elif total_score < 0:
            sentiments[aspect] = "Negative"
        else:
            sentiments[aspect] = "Neutral"

    return sentiments