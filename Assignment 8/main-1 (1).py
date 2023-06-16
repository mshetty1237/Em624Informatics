import bs4 as bs
import nltk
#nltk.download()
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# URL of the website
url = "https://www.nbcnews.com/"

# Get the webpage content and create a BeautifulSoup object
response = requests.get(url)
sp = bs.BeautifulSoup(response.content, "html.parser")

# Extract the article headings
headings = [h.get_text() for h in sp.find_all('h3')]

# Stopwords to be excluded from the text
stopwords = nltk.corpus.stopwords.words('english') + ['world', 'cup', 'trump', 'thanksgiving', 'russia', 'war', 'advertisement', 'covid']

# Clean the text by removing stopwords, punctuation, and converting to lowercase
clean_headings = []
for heading in headings:
    words = nltk.word_tokenize(heading.lower())
    clean_words = [word for word in words if word.isalpha() and word not in stopwords]
    clean_headings.append(' '.join(clean_words))

# Calculate sentiment scores using VADER
analyzer = SentimentIntensityAnalyzer()
sentiment_scores = [analyzer.polarity_scores(heading) for heading in clean_headings]
pos = sum(score['pos'] for score in sentiment_scores)
neg = sum(score['neg'] for score in sentiment_scores)
neu = sum(score['neu'] for score in sentiment_scores)

# Print sentiment distribution
total = pos + neg + neu
print(f"\nThe following is the distribution of the sentiment :\n"
      f"\nIt is positive for {pos/total:.1%}\n"
      f"It is negative for {neg/total:.1%}\n"
      f"It is neutral for {neu/total:.1%}")

# Extract bigrams from the text
bigrams = nltk.bigrams([word for heading in clean_headings for word in heading.split()])
freq = nltk.FreqDist(bigrams).most_common(5)

# Print most common bigrams and their frequencies
print(f"\nThe most frequent bigrams and their frequencies from The nbc are as follows:\n{freq}")

# Generate a word cloud from the text
text = ' '.join(clean_headings)
wc = WordCloud(background_color ='white',max_words = 1000)
wc.generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()

