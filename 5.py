import csv
import os
import re
a = os.listdir("news")
comp = re.compile(r"https://\S*")
SUH = re.compile(r"([^\.]\s[А-Я]{1}[а-я]*|[^\.]\s[A-Z]{1}[a-z]*|\"[А-Я]{1}[а-я]*\"|\"[A-Z]{1}[a-z]*\")")
BAZA = [["index", "Title", "Lid", "Text", "Ner", "Language", "URL", "Date"]]
i=0
Language=0
for sda in a:
    STROKA= []
    NEWS = "news\{ner}"
    NEWS1 = NEWS.format(ner=a[i])
    with open(NEWS1, 'r', encoding='utf-8') as f:
        Text = f.read()
        # Нахождение сылки на статью
        res = re.search(comp, Text)
        result=res.group()
        STROKA.append(i) #Присвоение индекса
        #разделение текст на строки и оброботка его
        TEXT_SP = Text.split("\n")
        try:
            while True:
                TEXT_SP.remove("")
        except ValueError:
            pass
        Title = TEXT_SP[0].replace("\ufeff","")
        ZIK = len(TEXT_SP)
        ZOK= []
        STROKA.append(Title) #Заголовки статей
        STROKA.append(TEXT_SP[1]) # Краткое содержание новости
        TEXT=" ".join(TEXT_SP)
        TEXTR = TEXT.replace(result, "")
        for dos in range(1,ZIK):
            ZOK.append(TEXT_SP[dos])
        TEXTR1=" ".join(ZOK)
        STROKA.append(TEXT) # Текст статьй
        if re.search(SUH, TEXTR1): # Имена собственные
            Ner = 1
        else:
            Ner = 0
        STROKA.append(Ner)
        # Языка статьй
        if re.search(r"[a-z]", TEXTR, re.I):
            Language=Language+1
        if re.search(r"[а-я]", TEXTR, re.I):
            Language=Language+2
        if Language == 3:
            Language1="ru-en"
        if Language == 2:
            Language1="ru"
        if Language == 1:
            Language1="en"
        STROKA.append(Language1)
        # Сылка на статью
        STROKA.append(result)
        # Дата стати
        if re.search(r"(19\d\d\D|20\d\d\D)", result):
            DATA = re.search(r"(19\d\d\D|20\d\d\D)", result).group()
            DATA1= re.search(r"(19\d\d|20\d\d)", DATA).group()
        else:
            DATA1 = ""
        STROKA.append(DATA1)
        BAZA.append(STROKA)
    i=i+1
with open("BAZA.csv","w",encoding="utf-8", newline="") as File:
    wr = csv.writer(File)
    wr.writerows(BAZA)
