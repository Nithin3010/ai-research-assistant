import re


def clean_text(text):
    # Join words broken by a line break.
    text = re.sub(r"-\s*\n\s*", "", text)

    # Replace line breaks with spaces.
    text = text.replace("\n", " ")

    # Replace multiple spaces with a single space.
    text = re.sub(r"\s+", " ", text)

    return text.strip()