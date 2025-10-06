import os
import re

#CHANGE TO THE DIRECTORY WHERE THIS PROGRAM IS
# os.chdir(r"C:\Users\Coco\Downloads\nlp\nlp1000-main")

def sentence_regex(text):
    # remove numbers followed by uppercase letters
    text = re.sub(r'[0-9][0-9]([A-Z])', r'\1', text, flags = re.MULTILINE)
    text = re.sub(r'[0-9]([A-Z])', r'\1', text, flags = re.MULTILINE)
    # add a newline after a period followed by an uppercase letter
    text = re.sub(r'\.\s([A-Z])',r'.\n\1', text, flags = re.MULTILINE)
    # add a newline after a period is followed by a number
    text = re.sub(r'(\.\s)[0-9]', r'\1\n', text, flags = re.MULTILINE)
    # remove lines ending with (...
    text = re.sub(r'\(...\s$', r'', text, flags = re.MULTILINE)
    # remove patterns like ":12-34)" or ":1-2)"
    text = re.sub(r':\d+-\d\d\) ', r'', text, flags = re.MULTILINE)
    text = re.sub(r':\d-\d\) ', r'', text, flags = re.MULTILINE)
    # add a newline after a period followed by a lowercase letter and uppercase letter
    text = re.sub(r'(\..).([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    # remove lines start w numbers
    text = re.sub(r'^[0-9][0-9][0-9]|^[0-9][0-9]|^[0-9]', r'', text, flags = re.MULTILINE)
    # remove lines starting with : followed by any text ending with )
    text = re.sub(r'^:.*\)\s|^:.*\)', r'', text, flags=re.MULTILINE)
    # remove lines starting with numbers again (redundant pattern)
    text = re.sub(r'^[0-9][0-9][0-9]|^[0-9][0-9]|^[0-9]', r'', text, flags = re.MULTILINE)
    # remove lines starting with ":" followed by a space
    text = re.sub(r'^:.* $\n', r'', text, flags = re.MULTILINE)
    # remove lines ending with a number
    text = re.sub(r'.*[0-9]$', r'', text, flags = re.MULTILINE)
    # remove double new lines
    text = re.sub(r'\n\n', r'', text, flags = re.MULTILINE)
    # remove leading newlines
    text = re.sub(r'^\n', r'', text, flags = re.MULTILINE)
    # remove . followed by uppercase letters
    text = re.sub(r'(\.)([A-Z])', r'', text, flags = re.MULTILINE)
    # remove exclamation marks followed by uppercase letters
    text = re.sub(r'(!)([A-Z])', r'', text, flags = re.MULTILINE)
    # add a newline after quotation marks followed by uppercase letters
    text = re.sub(r'(”)([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    # Remove patterns starting with # followed by any text ending with ; or :
    text = re.sub(r'#.*;|#.*:', r'', text, flags = re.MULTILINE)
    # remove numbers followed by letters
    text = re.sub(r'\d+([A-z])', r'\1', text, flags = re.MULTILINE)
    # remove lowercase-uppercase transitions
    text = re.sub(r'([a-z])([A-Z])', r'', text, flags = re.MULTILINE)
    # remove lines ending with lowercase letters
    text = re.sub(r'.*[a-z]$\n', r'', text, flags = re.MULTILINE)
    # remove pattern that looks like .’”) 
    text = re.sub(r'(\.’”) ', r'', text, flags = re.MULTILINE)
    # add a newline after ? followed by uppercase letters
    text = re.sub(r'(\?)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    # add a newline after ! followed by uppercase letters
    text = re.sub(r'(!”)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    # add a newline after question marks followed by uppercase letters
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


    # remove Lc :. or Lc: (kapampangan)
    text = re.sub(r"Lc\s*:", "", text) 
    # add a space like Makatua(Marcos to Makatua (Marcos (kapampangan)
    text = re.sub(r"(\w+)\((\w+)", r"\1 (\2", text)
    # remove :-; (kapampangan)
    re.sub(r":-;", "", text, flags=re.MULTILINE)  
    # remove :. (kapampangan)
    text = re.sub(r":\.", "", text, flags=re.MULTILINE)  

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
