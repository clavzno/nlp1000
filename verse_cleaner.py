import os
import re

os.chdir(r"C:\Users\Van Asher Alcantara\Documents\DLSU\AY 2025-2026\Term 1\NLP1000\nlp1000-mco1")

def verse_regex(text):
    text = re.sub(r'^\d+\s*', r'', text, flags=re.MULTILINE)
    text = re.sub(r'^\w+\s+\d+\s*\n?', r'', text, flags=re.MULTILINE)
    text = re.sub(r'\n+', r'\n', text)
    text = re.sub(r'(?m)(\d+)([A-Za-z“"‘\'])', r'\n\1\2', text)
    text = re.sub(r'\n+', r'\n', text)
    text = text.lstrip('\n')
    text = re.sub(r'^\d+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r"[“”]", '"', text)
    text = re.sub(r"[‘’]", "'", text)

    # this regex keeps letters (including accented), numbers, and common punctuation marks 
    # while removing inconsistent special characters
    text = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ\u00C0-\u024F\u1E00-\u1EFF0-9\s\.\,\!\?\:\;\'"\-]', "", text)
    
    return text

text = ""

script_dir = os.path.dirname(__file__)
# change to proper file path
file_path = os.path.join(script_dir, r"data(no notes and headings)\ivatan.txt")
with open(file_path, "r", errors="ignore", encoding="utf-8") as f:
    text = f.read()

text = verse_regex(text)

# change to proper file path
output_path = os.path.join(script_dir, "ivatan-cleaned-verses.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)