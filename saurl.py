import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')
url = 'https://en.wikipedia.org/wiki/Ice_cream'
article = Article(url)
article.download()
article.parse()
article.nlp()
text= article. summary
print (text)
blob= TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print (sentiment)

"""
see whether the content in the website is positive or negative
"""