# Project 1: Data Cleaning
Submitted on October 12, 2025

NLP1000 S17
Group 12: 
| Member Name      | ID Number      |
| ------------- | ------------- |
| Alcantara, Van Asher | 12340898 |
| Aragon, Enrique | 12227811 |
| Clavano, Angelica (Jack) | 12206245 |
| Lozada, Job | 12307246 |

## Table of Contents
1. Data Selection & Web Scraping
2. Data Cleaning and Segmentation
3. Parallel Corpus

---

## Running this Notebook:
- Make sure you have at least Python 3.12.0 or 3.14.0 installed.
- See first code block under 1.1 for `pip requirements`.

---

## Folder Structure:
```
/nlp1000 --> root
└── /data
    └── lang.txt files --> raw webscraped data
    └── /cleaned
        └── (sentences)-lang-cleaned.txt --> cleaned sentence files in txt format
        └── lang-cleaned.txt --> cleaned verse files in txt format
└── /parallel-corpora --> parallel corpora (aligned) but in separate xlsx files
└── .gitignore
└── main.ipynb --> MAIN SUBMISSION contains source information, source code, documentation
└── cleaned_sentences.ipynb --> cleaned sentence files in xlsx format - from data/cleaned/(sentences)-(lang)-cleaned.txt files
└── README.md --> contains the same information as this markdown block.
└── cleaned_verses.xlsx --> cleaned verse files in xlsx format - created when running the notebook from data/cleaned/(lang)-cleaned.txt
└── parallel_corpora.xlsx --> parallel corpora base file (unaligned) - created when running the notebook 
└── parallel_corpora_all.xlsx --> parallel corpora (aligned)
└── ai_declaration.pdf --> AI declaration
└── steps.xlsx --> steps for regex present in divide_into_verses() and divide_into_sentences()
```