def recommend_based_on_preferences(user_input, sentiments):
    user_input = user_input.lower()

    # 🔥 extract user preferred aspects
    preferences = []
    all_aspects = ["camera", "battery", "performance", "storage", "display"]

    for a in all_aspects:
        if a in user_input:
            preferences.append(a)

    if not preferences:
        return "🤔 I couldn’t understand your preferences clearly."

    pos, neg, neu = 0, 0, 0

    for p in preferences:
        if p in sentiments:
            if sentiments[p] == "Positive":
                pos += 1
            elif sentiments[p] == "Negative":
                neg += 1
            else:
                neu += 1

    # 🔥 DECISION LOGIC
    if pos == len(preferences):
        return f"🔥 Great choice! Since you're focusing on {', '.join(preferences)}, and this phone performs well in all of them — I’d totally recommend it!"

    elif neg == len(preferences):
        return f"🚫 Not a good pick! You're focusing on {', '.join(preferences)}, but this phone performs poorly in those areas."

    elif pos > neg:
        return f"⚖️ Mixed vibes! You care about {', '.join(preferences)} — some are good, some not so great. I’d say it depends on your priority."

    elif neg > pos:
        return f"⚠️ Risky choice! Since {', '.join(preferences)} matter to you and performance is weak there, I wouldn’t strongly recommend it."

    else:
        return f"🤷 For {', '.join(preferences)}, the phone is average — you can consider it, but it's not the best choice."
      