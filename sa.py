from textblob import TextBlob
with open('myText.txt', 'r') as f:
    text = f.read()
blob = TextBlob(text)
sentiment = blob.setiment.polarity # -1
print(sentiment)