import os
import re

#CHANGE TO THE DIRECTORY WHERE THIS PROGRAM IS
os.chdir(r"C:\Users\Coco\Downloads\nlp\nlp1000-main")

def sentence_regex(text):
    text = re.sub(r'[0-9][0-9]([A-Z])', r'\1', text, flags = re.MULTILINE)
    text = re.sub(r'[0-9]([A-Z])', r'\1', text, flags = re.MULTILINE)
    
    text = re.sub(r'\.\s([A-Z])',r'.\n\1', text, flags = re.MULTILINE)
    text = re.sub(r'(\.\s)[0-9]', r'\1\n', text, flags = re.MULTILINE)
    text = re.sub(r'\(...\s$', r'', text, flags = re.MULTILINE)
    text = re.sub(r':\d+-\d\d\) ', r'', text, flags = re.MULTILINE)
    text = re.sub(r':\d-\d\) ', r'', text, flags = re.MULTILINE)
    text = re.sub(r'(\..).([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    text = re.sub(r'^[0-9][0-9][0-9]|^[0-9][0-9]|^[0-9]', r'', text, flags = re.MULTILINE)
    text = re.sub(r'^:.*\)\s|^:.*\)', r'', text, flags=re.MULTILINE)
    
    text = re.sub(r'^[0-9][0-9][0-9]|^[0-9][0-9]|^[0-9]', r'', text, flags = re.MULTILINE)
    text = re.sub(r'^:.* $\n', r'', text, flags = re.MULTILINE)
    
    text = re.sub(r'.*[0-9]$', r'', text, flags = re.MULTILINE)
    text = re.sub(r'\n\n', r'', text, flags = re.MULTILINE)
    
    text = re.sub(r'^\n', r'', text, flags = re.MULTILINE)
    text = re.sub(r'(\.)([A-Z])', r'', text, flags = re.MULTILINE)
    text = re.sub(r'(!)([A-Z])', r'', text, flags = re.MULTILINE)
    text = re.sub(r'(”)([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    text = re.sub(r'#.*;|#.*:', r'', text, flags = re.MULTILINE)
    text = re.sub(r'\d+([A-z])', r'\1', text, flags = re.MULTILINE)
    text = re.sub(r'([a-z])([A-Z])', r'', text, flags = re.MULTILINE)
    text = re.sub(r'.*[a-z]$\n', r'', text, flags = re.MULTILINE)
    text = re.sub(r'(\.’”) ', r'', text, flags = re.MULTILINE)
    text = re.sub(r'(\?)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(!”)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    text = re.sub(r'(\?”) ([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'\d+(‘)', r'\n\1', text, flags = re.MULTILINE)
    text = re.sub(r'\)\d+', r'', text, flags = re.MULTILINE)
    text = re.sub(r'^:\d+.*[0-9];\s', r'', text, flags = re.MULTILINE)
    text = re.sub(r'[0-9]', r'', text, flags = re.MULTILINE)
    text = re.sub(r'^\s', r'', text, flags=re.MULTILINE)

    
    text = re.sub(r'(\?)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(!)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(!)\s(“)', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(\?)\s(“)', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(\.”)\s(“)', r'\1\n\2', text, flags = re.MULTILINE)
    
    text = re.sub(r'¶ ', r'', text, flags = re.MULTILINE)
    text = re.sub(r'¶', r'', text, flags = re.MULTILINE)


    #text = re.sub(r'', r'', text)

    return text 

text = ""

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data", "tausug.txt")
with open(file_path, "r", errors = "ignore", encoding = "utf-8" ) as f:
    text = f.read()

text = sentence_regex(text)

output_path = os.path.join(script_dir, "tausug-cleaned.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)
