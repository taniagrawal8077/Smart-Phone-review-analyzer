import random
import pandas as pd

# aspects and keywords
aspects = {
    "camera": ["camera"],
    "battery": ["battery"],
    "storage": ["storage", "memory"],
    "performance": ["performance", "slow"],
    "display": ["display", "screen"]
}

# sentiment variations
positive = [
    "acha hai", "bahut acha hai", "mast hai", "awesome hai",
    "very good hai", "great hai"
]

negative = [
    "bekar hai", "kharab hai", "acha nahi hai",
    "bahut bekar hai", "issue hai", "very bad hai"
]

neutral = [
    "theek hai", "average hai", "normal hai"
]

data = []

# 🔹 SINGLE ASPECT DATA (3000 rows)
for _ in range(3000):
    aspect = random.choice(list(aspects.keys()))
    keyword = random.choice(aspects[aspect])

    sentiment_type = random.choice(["pos", "neg", "neu"])

    if sentiment_type == "pos":
        phrase = random.choice(positive)
    elif sentiment_type == "neg":
        phrase = random.choice(negative)
    else:
        phrase = random.choice(neutral)

    sentence = f"{keyword} {phrase}"
    data.append([sentence, aspect])

# 🔹 MULTI-ASPECT DATA (1000 rows)
for _ in range(1000):
    a1, a2 = random.sample(list(aspects.keys()), 2)

    k1 = random.choice(aspects[a1])
    k2 = random.choice(aspects[a2])

    s1 = random.choice(positive + negative)
    s2 = random.choice(positive + negative)

    sentence = f"{k1} {s1} aur {k2} {s2}"

    data.append([sentence, f"{a1},{a2}"])

# create dataframe
df = pd.DataFrame(data, columns=["text", "aspect"])

# save CSV
df.to_csv("dataset.csv", index=False)

print("✅ dataset.csv generated with", len(df), "rows")