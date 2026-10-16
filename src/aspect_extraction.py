def extract_aspects(text):
    aspects = []

    aspect_keywords = {
        "camera": ["camera"],
        "battery": ["battery"],
        "display": ["display", "screen"],
        "performance": ["performance", "slow", "lag", "laggy", "fast"],
        "sound": ["sound", "audio"],
        "build": ["build", "premium"],
        "storage": ["storage", "memory", "space"]
    }

    words = text.lower().split()

    for aspect, keywords in aspect_keywords.items():
        for word in keywords:
            if word in words:
                aspects.append(aspect)
                break

    return list(set(aspects))