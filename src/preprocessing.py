import re

def clean_text(text):
    text = text.lower()

    # remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # remove mentions
    text = re.sub(r'@\w+', '', text)

    # remove hashtags (#good → good)
    text = re.sub(r'#', '', text)

    # remove emojis (basic)
    text = re.sub(r'[^\w\s]', '', text)

    return text