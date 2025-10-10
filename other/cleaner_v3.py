# old cleaner.py that was in main.ipynb; this is the latest ver of it
from cleaner import sentence_regex # cleaner.py

languages = ["spanish", "tagalog", "english", "hiligaynon", "bikol", "waray", "ilocano", "cebuano", "kapampangan", "pangasinense", "yakan", "ivatan", "tausug", "yami", "tuwali_ifugao", "masbateno"]
data_folder = Path("data")
cleaned_folder = Path("data/cleaned")
cleaned_folder.mkdir(parents=True, exist_ok=True) 

for lang in languages:
    file_path = data_folder / f"{lang}.txt"
    output_path = cleaned_folder / f"{lang}-cleaned.txt"

    # SKIP if the input file does not exist or is empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        print(f"Skipped: {file_path} (file does not exist or is empty)")
        continue

    # read input
    with file_path.open("r", errors="ignore", encoding="utf-8") as f:
        text = f.read()

    # clean the text
    cleaned_text = sentence_regex(text)

    # save
    with output_path.open("w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"Cleaned and saved: {output_path}")