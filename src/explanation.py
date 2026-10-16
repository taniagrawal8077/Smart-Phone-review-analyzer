def explain_sentiment(text, aspects):
    import re
    text = text.lower()

    # split sentence
    parts = re.split(r"lekin|but|aur|and", text)

    positive_words = [
        "good", "great", "amazing", "achi", "badiya", "mast",
        "awesome", "love", "best", "fantastic",
        "acha", "accha", "fast"
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
        "build": ["build", "premium"],
        "storage": ["storage", "memory", "space"]
    }

    explanations = {}

    for aspect in aspects:
        explanations[aspect] = []
        keywords = aspect_keywords.get(aspect, [])

        for part in parts:
            words = part.split()

            # only relevant part
            if any(k in words for k in keywords):

                for i, word in enumerate(words):

                    # 🔴 NEGATIVE WORD
                    if word in negative_words:
                        if i > 0 and words[i - 1] in ["bahut", "very"]:
                            explanations[aspect].append(f"Strong Negative: {words[i-1]} {word}")
                        else:
                            explanations[aspect].append(f"Negative: {word}")

                    # 🟢 POSITIVE WORD WITH NEGATION FIX
                    elif word in positive_words:

                        # "nahi acha"
                        if i > 0 and words[i - 1] in negation_words:
                            explanations[aspect].append(f"Negative: {words[i-1]} {word}")

                        # "acha nahi"
                        elif i < len(words)-1 and words[i + 1] in negation_words:
                            explanations[aspect].append(f"Negative: {word} {words[i+1]}")

                        # strong positive
                        elif i > 0 and words[i - 1] in ["bahut", "very"]:
                            explanations[aspect].append(f"Strong Positive: {words[i-1]} {word}")

                        else:
                            explanations[aspect].append(f"Positive: {word}")

    return explanations