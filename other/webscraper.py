import os
os.chdir(r"C:\Users\Coco\Documents\DLSU\AY 2025-2026\Term 1\NLP1000")
#this is technically optional, i just changed the directory to the folder this code is in so that the text file is made there

#note: install BeautifulSoup by entering this in the command line: python -m pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

#goes through chapters of the book
for i in range(1,51):
  urlPartOne = "https://www.bible.com/bible/"
  #bibles on bible.com have their own number, just replace bibleNumber
  bibleNumber = str(1319)

  #the code of the bible book youre extracting from
  bookCode = "/EXO."

  #chapter number auto updated
  chapterNumber = str(i)

  #this is just the bible's abbreviation. make sure you keep the . at the start
  bibleName = ".PMPV"
  
  url = urlPartOne + bibleNumber + bookCode + chapterNumber + bibleName
  print(url)
  page = urlopen(url)
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  
  #isolates the actual bible text
  #IMPORTANT: THIS ONLY WORKS ON BIBLE.COM, for other sites just use inspect element then select the div/class containing the text so that it extracts just that
  test = soup.find('div', {'class': 'ChapterContent_reader__Dt27r'})
  
  #make sure to change file name
  with open("kapampangan.txt", "a") as f:
    f.write(test.get_text())
