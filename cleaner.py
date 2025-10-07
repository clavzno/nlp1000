import os
import re

#CHANGE TO THE DIRECTORY WHERE THIS PROGRAM IS
# os.chdir(r"C:\Users\Coco\Downloads\nlp\nlp1000-main")

def sentence_regex(text):
    # replace weird ‘ with ' accounts for letters before and after
    text = re.sub(r"(\w)‘(\w)", r"\1'\2", text, flags=re.MULTILINE)
    text = re.sub(r"‘", r"'", text, flags=re.MULTILINE)  # for standalone
    # replace ’ with '
    text = re.sub(r"(\w)’(\w)", r"\1'\2", text, flags=re.MULTILINE)
    text = re.sub(r"’", r"'", text, flags=re.MULTILINE)  # for standalone

    # replace weird ” and “ with " and accounts for letters before and after
    text = re.sub(r"(\w)”", r'\1"', text, flags=re.MULTILINE)
    text = re.sub(r"“(\w)", r'"\1', text, flags=re.MULTILINE)
    text = re.sub(r"”", r'"', text, flags=re.MULTILINE)  # for standalone
    text = re.sub(r"“", r'"', text, flags=re.MULTILINE)  # for standalone

    # remove space for , " --> DOESNT WORK
    text = re.sub(r'\s+,', ',', text, flags=re.MULTILINE) # remove space before comma
    text = re.sub(r',\s+', ',', text, flags=re.MULTILINE) # remove space after comma
    text = re.sub(r'\s+"', '"', text, flags=re.MULTILINE) # remove spaces before quotation marks
    text = re.sub(r'"\s+', '"', text, flags=re.MULTILINE) # remove spaces after quotation marks
    
    # remove lines that only contain a quotation mark --> DOESNT WORK
    text = re.sub(r'^\s*"\s*$', '', text, flags=re.MULTILINE)

    # remove numbers followed by uppercase letters
    text = re.sub(r'[0-9][0-9]([A-Z])', r'\1', text, flags = re.MULTILINE)
    text = re.sub(r'[0-9]([A-Z])', r'\1', text, flags = re.MULTILINE)

    # ensure sentences within quotes are not split by a period until the closing quote (masbateno-specific)
    text = re.sub(r'"([^"]*\.[^"]*)"', r'"\1"', text, flags=re.MULTILINE)

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

    # remove lines starting with numbers again (NOTE: redundant pattern)
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
    text = re.sub(r'(")([A-Z])', r'\1\n\2', text, flags = re.MULTILINE) # for ", handled by first few lines

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
    text = re.sub(r'(\.\'") ', r'', text, flags=re.MULTILINE) # for "" and '', handled by first few lines

    # add a newline after ? followed by uppercase letters
    text = re.sub(r'(\?)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    # add a newline after ! followed by uppercase letters (redundant, see below)
    text = re.sub(r'(!”)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(!")\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE) # for ", handled by first few lines

    # add a newline after ? followed by uppercase letters
    text = re.sub(r'(\?”) ([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    # Add a newline after digits followed by "‘"
    text = re.sub(r'\d+(‘)', r'\n\1', text, flags = re.MULTILINE)
    text = re.sub(r"\d+(')", r'\n\1', text, flags=re.MULTILINE) # for ', handled by first few lines

    # Remove ) followed by digits
    text = re.sub(r'\)\d+', r'', text, flags = re.MULTILINE)

    # remove lines starting with : followed by digits and ending with ;
    text = re.sub(r'^:\d+.*[0-9];\s', r'', text, flags = re.MULTILINE)

    # remove all number digits
    text = re.sub(r'[0-9]', r'', text, flags = re.MULTILINE)

    # remove leading whitespace (e.g., " Text" -> "Text")
    text = re.sub(r'^\s', r'', text, flags=re.MULTILINE)

    # add a newline after ? followed by uppercase letters
    text = re.sub(r'(\?)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    # add a newline after ! followed by uppercase letters
    text = re.sub(r'(!)\s([A-Z])', r'\1\n\2', text, flags = re.MULTILINE)

    # add a newline after "!”" followed by "“"
    text = re.sub(r'(!)\s(“)', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(!)\s(")', r'\1\n\2', text, flags = re.MULTILINE) # for ", handled by first few lines

    # add a newline after "?" followed by "“"
    text = re.sub(r'(\?)\s(“)', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(\?)\s(")', r'\1\n\2', text, flags = re.MULTILINE) # for ", handled by first few lines

    # add a newline after .” followed by “
    text = re.sub(r'(\.”)\s(“)', r'\1\n\2', text, flags = re.MULTILINE)
    text = re.sub(r'(\.")\s(")', r'\1\n\2', text, flags = re.MULTILINE) # for "", handled by first few lines

    # remove "¶ " and "¶" (e.g., "¶ Text" -> "Text")
    text = re.sub(r'¶ ', r'', text, flags = re.MULTILINE)
    text = re.sub(r'¶', r'', text, flags = re.MULTILINE)

    # remove Lc :. or Lc: (kapampangan-specific)
    text = re.sub(r"Lc\s*:", "", text) 

    # add a space like Makatua(Marcos to Makatua (Marcos (kapampangan-specific)
    text = re.sub(r"(\w+)\((\w+)", r"\1 (\2", text)

    # remove :-; (kapampangan-specific)
    re.sub(r":-;", "", text, flags=re.MULTILINE)  

    # remove :. (kapampangan-specific)
    text = re.sub(r":\.", "", text, flags=re.MULTILINE)  

    # Add a space after a comma if there's none (ex. niya,asin to niya, asin)
    text = re.sub(r',(\S)', r', \1', text, flags=re.MULTILINE)

    #text = re.sub(r'', r'', text)

    return text 

'''
text = ""

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data", "tausug.txt")
with open(file_path, "r", errors = "ignore", encoding = "utf-8" ) as f:
    text = f.read()

text = sentence_regex(text)

output_path = os.path.join(script_dir, "tausug-cleaned.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)
'''