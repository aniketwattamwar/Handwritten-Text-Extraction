# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:02:20 2020

@author: hp
"""

from PIL import Image 
import pytesseract 

filename = "Crossed-Cheque.png"

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
text = str(((pytesseract.image_to_string(Image.open(filename)))))


splitted_text = list(text.split(" "))
data_items =[]
cols = 3


data_items = [splitted_text[i:i + cols] for i in range(0, len(splitted_text), cols)] 
import csv
with open("output2.csv", "a", newline='') as fp:
    wr = csv.writer(fp, dialect='excel')
    for i in range(len(data_items)):
        wr.writerow(data_items[i])









