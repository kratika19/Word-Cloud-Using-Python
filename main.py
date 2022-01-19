import sys
import numpy as np
from PIL import Image
import random
import wikipedia
from wordcloud import WordCloud, STOPWORDS

a = str(input("Enter the name of which you want to make word cloud : "))
title = wikipedia.search(a)[0]
try:
    page = wikipedia.page(title, auto_suggest=False, redirect=True, preload=False)
except wikipedia.DisambiguationError as e:
    title = random.choice(e.options)
    page = wikipedia.page(title, auto_suggest=False, redirect=True, preload=False)

text = page.content
print(text)

bg = np.array(Image.open("abcd.jpg"))
unwanted_words = set(STOPWORDS)
wordclo = WordCloud(background_color="black",max_words=400, mask=bg, stopwords=unwanted_words)
wordclo.generate(text)
wordclo.to_file("sample.png")
