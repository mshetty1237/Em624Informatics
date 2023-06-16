#Code run by Mohit Shetty
import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def clean_text(text, stopwords, min_len):
    clean_words = []


    for word in nltk.word_tokenize(text):
        word = word.lower()
        if word.isalpha() and word not in stopwords and len(word) > min_len:
            clean_words.append(word)
    return clean_words

import string
from nltk.tokenize import word_tokenize


def read_text_file(filename):
    with open(filename, 'r', encoding='utf8') as file:
        return file.read()

def remove_punctuation(text):
    clean_word = []
    return text.translate(str.maketrans('', '', string.punctuation))

    text_without_punct = remove_punctuation(clean_words)
    words = word_tokenize(text_without_punct)
    words = [word for word in words if word.strip()]
    clean_words.append(word)

pro_txt = read_text_file('pro_space.txt')
con_txt = read_text_file('cons_space.txt')
stopwords_txt = read_text_file('stopwords_en.txt').split('\n')
stopwords = set(stopwords_txt)  # convert to set for faster lookup

min_len = 3

pro_clean_words = clean_text(pro_txt, stopwords, min_len)
con_clean_words = clean_text(con_txt, stopwords, min_len)

analyzer = SentimentIntensityAnalyzer()

pro_clean_text_str = ' '.join(pro_clean_words)
pro_vad_sentiment = analyzer.polarity_scores(pro_clean_text_str)

pro_pos, pro_neg, pro_neu = [pro_vad_sentiment[key] for key in ['pos', 'neg', 'neu']]

print('\nThe following is the distribution of the sentiment for pro Privatisation of Prison')
print('\nIt is positive for', '{:.1%}'.format(pro_pos))
print('\nIt is negative for', '{:.1%}'.format(pro_neg))
print('\nIt is neutral for', '{:.1%}'.format(pro_neu))

con_clean_text_str = ' '.join(con_clean_words)
con_vad_sentiment = analyzer.polarity_scores(con_clean_text_str)

con_pos, con_neg, con_neu = [con_vad_sentiment[key] for key in ['pos', 'neg', 'neu']]

print('\nThe following is the distribution of the sentiment for con Privatisation of Prison')
print('\nIt is positive for', '{:.1%}'.format(con_pos))
print('\nIt is negative for', '{:.1%}'.format(con_neg))
print('\nIt is neutral for', '{:.1%}'.format(con_neu))

# calculate pro and con bigrams
pro_bigrammed = list(nltk.bigrams(pro_clean_words))
print('\nThe following are the bigrams extracted from the pro text')
print(pro_bigrammed)
con_bigrammed = list(nltk.bigrams(con_clean_words))
print('\nThe following are the bigrams extracted from the con text')
print(con_bigrammed)

# print 5 most common bigrams and their frequencies for pros and cons
freqdist_pro = nltk.FreqDist(pro_bigrammed).most_common(10)
freqdist_con = nltk.FreqDist(con_bigrammed).most_common(10)
print('\nThe most frequent bigrams and their frequencies from the pro file are as follows: \n', freqdist_pro)
print('\nThe most frequent bigrams and their frequencies from the con file are as follows: \n', freqdist_con)

# defining the wordcloud parameters
wc_pro = WordCloud(background_color='white', max_words=3000)
wc_con = WordCloud(background_color='white', max_words=3000)

# generating word cloud
wc_pro.generate(pro_clean_text_str)
wc_con.generate(con_clean_text_str)

# show the clouds
plt.figure(figsize=(100, 50))
plt.subplot(211)
plt.imshow(wc_pro)
plt.axis('off')
plt.title('Pro word Cloud')
plt.subplot(212)
plt.imshow(wc_con)
plt.axis('off')
plt.title('Con word Cloud')
plt.show()

