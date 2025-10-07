# modified version so that we can just run one thing 
import os
#note: python -m pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

output_folder = "data"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

languages = ["spanish", "tagalog", "english", "hiligaynon", "bikol", "waray", "ilocano", "cebuano", "kapampangan", "pangasinense", "yakan", "ivatan", "tausug", "yami", "tuwali_ifugao", "masbateno"]
# if SKIP, skip entirely and move to the next 
bibleNumbers = ["1076", "177", "3523", "2190", "890", "2198", "782", "562", "1141", "2194", "1388", "1315", "1319", "2364", "2123", "1222"]
bibleAbbreviation = ["JBS", "TLAB", "NRSVUE", "MBBHIL12", "MBBBIK92", "MBBSAM", "RIPV", "RCPV", "PMPV", "MBBPAN83", "YAKV", "VTSP", "TSG", "SNT", "IFKWB", "MSB"]

bookCodes = ["mat", "mrk", "luk", "jhn"]
chapterRanges = {
    "mat": [1, 28],
    "mrk": [1, 16],
    "luk": [1, 24],
    "jhn": [1, 21]
}

# clear content of the file if it exists
for lang in languages:
    file_name = os.path.join(output_folder, f"{lang}.txt")
    with open(file_name, "w", encoding="utf-8") as f:
        pass 


for lang, bibleNumber, abbreviation in zip(languages, bibleNumbers, bibleAbbreviation):
  if bibleNumber == "SKIP" or abbreviation == "SKIP":
        continue
  
  for bookCode, (start, end) in chapterRanges.items():
     for chapter in range(start, end + 1):
      urlPartOne = "https://www.bible.com/bible/"
      chapterNumber = str(chapter)
      bibleName = f".{abbreviation}"

      url = f"{urlPartOne}{bibleNumber}/{bookCode.upper()}.{chapterNumber}{bibleName}"
      print(f"Scraping URL: {url}")

      try: 
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        
        #IMPORTANT: THIS ONLY WORKS ON BIBLE.COM, for other sites just use inspect element then select the div/class containing the text so that it extracts just that
        text = soup.find('div', {'class': 'ChapterContent_reader__Dt27r'})

        if text:
          
          # excludes the pop-up notes
          for note in text.select('span.ChapterContent_note__YlDW0'):
            note.decompose()
          
          # excludes chapter headings
          for heading in text.select('span.ChapterContent_heading__xBDcs'):
            heading.decompose()
        
          # write to lang-specific file
          file_name = os.path.join(output_folder, f"{lang}.txt")
          # file_name = f"{lang}.txt"
          with open(file_name, "a", encoding="utf-8") as f:
              f.write(text.get_text() + "\n")
        else:
            print(f"No content found for {lang}, {bookCode}, chapter {chapter}")
      except Exception as e:
                  print(f"Error scraping {url}: {e}")