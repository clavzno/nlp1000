import sys
import re
import pandas as pd
from pathlib import Path

#Usage: python csv_converter.py nlp1000/SOMETHING-cleaned.txt

def parse_translation_file(filepath):
    """Parse a cleaned translation text into a structured DataFrame."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read().strip()

    # Split chapters where verse numbering resets to 1
    chapters = re.split(r'\n(?=1,)', text)

    data = []
    for chapter_idx, chapter_text in enumerate(chapters, start=1):
        # Match verse lines
        verses = re.findall(r'(\d+),(.*?)(?=\n\d+,|\Z)', chapter_text, flags=re.S)
        for verse_num, verse_text in verses:
            verse_text = verse_text.strip()
            data.append(["", chapter_idx, int(verse_num), verse_text])  # Empty Book column

    #make the data frame
    df = pd.DataFrame(data, columns=["Book", "Chapter", "Verse", "Text"])
    return df

def main():
    if len(sys.argv) < 2:
        print("Wrong arguments passed. Usage: python make_csv.py <input_file>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"File not found: {input_file}")
        sys.exit(1)

    print(f"Processing {input_file.name}...")
    df = parse_translation_file(input_file)

    # Output file name (e.g., english-cleaned.txt → english.csv)
    output_name = input_file.stem.replace("-cleaned", "") + ".csv"
    df.to_csv(output_name, index=False, encoding="utf-8-sig")
    print(f"Saved {output_name} with {len(df)} verses across {df['Chapter'].nunique()} chapters.")

if __name__ == "__main__":
    main()
