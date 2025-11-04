### 1.1 Remaining Data Cleaning
In the first project, we may have left out certain quirks that were present in some languages. Furthermore, after every sentence, there must be a space. The following code will delete and rewrite the cleaned files.

```python
'''
# base code for accessing all files per language
# we're not using the old data folder we have a copy of it here in project2/
data_folder = Path("p2data")

# output file paths here
# raw_data_filepath = data_folder / f"{lang}.txt"
# all_verses_filepath = data_folder / f"{lang}-cleaned.txt"
# all_sentences_filepath = data_folder / f"(sentences)-{lang}-cleaned.txt"

for lang in languages: 
    output_file_path = # check above

    if if cleaned_file_path.exists() and cleaned_file_path.stat().st_size > 0:
        with cleaned_file_path.open("r", encoding="utf-8") as f:
        # do whatever you want here
            text = f.read()
            word_count = len(text.split())
            total_word_count += word_count
            print(f"Word count for {lang}.txt: {word_count}")

    else:
        print(f"Skipped: {cleaned_file_path} (file does not exist or is empty)")


for lang in languages:
    output_file_path = # check above

    if not source_file_path.exists() or source_file_path.stat().st_size == 0:
        print(f"Skipped: {source_file_path} (file does not exist or is empty)")
        continue
        
    # rewrite all the txts if it exists
    if output_file_path.exists():
        print(f"unlinking/deleting old files")
        output_path.unlink()

    # read input
    with source_file_path.open("r", errors="ignore", encoding="utf-8") as f:
        text = f.read()
    
    # do whatever you want here
    cleaned_text = something(text)

    # save it
    with output_path.open("w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"Cleaned and saved: {output_path}")'''
```