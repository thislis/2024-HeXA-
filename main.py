import PyPDF2
import os
import wikipediaapi
from keybert import KeyBERT
import pprint
import re

kw = KeyBERT()
wiki = wikipediaapi.Wikipedia("2024HeXA 최마진 (ckwone12@unist.ac.kr)", "en")

def pdf2txt(pdf_path, start_page=None, end_page=None):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []

        if not start_page:
            start_page = 0

        else:
            start_page -= 1

        if not end_page or end_page > len(reader.pages):
            end_page = len(reader.pages)

        for page_num in range(start_page, end_page):
            text.append(reader.pages[page_num].extract_text().split("."))

    return text

def ext_keyword(text_list, setting):
    keyword_list = []
    for text in text_list:
        for temp in kw.extract_keywords(text, keyphrase_ngram_range=(setting["minwordcnt"], setting["maxwordcnt"]), use_mmr=setting["mmr"], use_maxsum=setting["msd"]):
            keyword_list.append(temp)


    return keyword_list

def PlzNoMoreKeyTerm(pdf, bertseting):

    words = []

    for i in ext_keyword(pdf2txt(pdf["pdf_path"], pdf["start_page"], pdf["end_page"]), bertseting):
        for j in i:
            words.append(j[0])

    result = {}
    fail = []

    for word in words:
        word = re.sub("[0-9]", "", word)
        if bool(word):
            page = wiki.page(word)
            if page.exists():
                r = re.sub(" {3,}", "", re.sub("\n", "", page.summary))
                if "refer to" in r:
                    result[word] = r + f"({page.fullurl})"
                else:
                    result[word] = r
            else:
                fail.append(word)

    return {"result":result, "Not_founded":fail}

min, max = map(int, input("min/max word count(smaller integer, larger integer): ").split(", "))
if input("Maximal Marginal Relevance on/off: ") == "on":
    MMR = True
else: MMR = False
if input("Max Sum Distance on/off: ") == "on":
    MSD = True
else: MSD = False
BERTSETTING = {"minwordcnt":min, "maxwordcnt":max, "mmr":MMR, "msd":MSD}

pdf_path = input("Pdf path: ")
start, end = map(int, input("start page, end page(smaller integer, larger integer): ").split(", "))
PDF = {"pdf_path":pdf_path, "start_page":start, "end_page":end}



gg = PlzNoMoreKeyTerm(PDF, BERTSETTING)

pprint.pprint(gg["result"])
print("Not founded")
print(gg["Not_founded"])
