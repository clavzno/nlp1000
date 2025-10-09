import re

# works with uncleaned data
def divide_into_verses(text):
    # WEIRD ENCODING: replace weird ‘ with ' accounts for letters before and after
    text = re.sub(r"(\w)‘(\w)", r"\1'\2", text, flags=re.MULTILINE)
    text = re.sub(r"‘", r"'", text, flags=re.MULTILINE)  # for standalone
    # WEIRD ENCODING: replace ’ with '
    text = re.sub(r"(\w)’(\w)", r"\1'\2", text, flags=re.MULTILINE)
    text = re.sub(r"’", r"'", text, flags=re.MULTILINE)  # for standalone
    # WEIRD ENCODING: replace weird ” and “ with " and accounts for letters before and after
    text = re.sub(r"(\w)”", r'\1"', text, flags=re.MULTILINE)
    text = re.sub(r"“(\w)", r'"\1', text, flags=re.MULTILINE)
    text = re.sub(r"”", r'"', text, flags=re.MULTILINE)  # for standalone
    text = re.sub(r"“", r'"', text, flags=re.MULTILINE)  # for standalone

    # see test.ipynb

    # SPACING: remove double spaces
    text = re.sub(r' {2,}', ' ', text, flags=re.MULTILINE)

    # SPACING: remove double new lines
    text = re.sub(r'\n\n', r'', text, flags = re.MULTILINE)

    # SPACING: remove leading newlines
    text = re.sub(r'^\n', r'', text, flags = re.MULTILINE)

    # SPACING: remove leading whitespace (e.g., " Text" -> "Text")
    text = re.sub(r'^\s+', r'', text, flags=re.MULTILINE)

    # ----- SPECIFIC QUIRKS BELOW -----

    return text

# works with uncleaned data
# the vision is to clean it into verses, then remove the numbers nalang 
def divide_into_sentences(text):
    return text