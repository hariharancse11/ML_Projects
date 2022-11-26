import string
from collections import Counter
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text_file = open('read.txt', encoding='utf-8').read()
lower_text = text_file.lower()
cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation))



#tokenizing text

tokenized_text = word_tokenize(cleaned_text,'english')

#To remove stopwords (It's nothing but non emotional word's like I,you..)
# print(stopwords.words('english'))

final_words = [word for word in tokenized_text if word not in stopwords.words('english')]

#Lemmatization - Convert words from plural to singular + Base form of a word (eg. Creating -> create)
Lemmatized_words = [WordNetLemmatizer().lemmatize(word) for word in final_words]
#print(Lemmatized_words)


emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in Lemmatized_words:
            emotion_list.append(emotion)

#print(emotion_list)
w = Counter(emotion_list)
#print(w)
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
#plt.show()
compound_score = 0.0
def sentimentAnalysis(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    compound_score = score['compound']
    print(score)
    res = ''
    if score['neg'] == score['pos']:
        res += 'Neutral'
    else:
        if score['neg'] < score['pos']:
            res += 'Positive'
        else:
            res += 'Negative'

    #print(compound_score)
    if compound_score < -0.5:
        print('1 Star')
    elif compound_score < 0.0:
        print('2 Star')
    elif compound_score < 0.25:
        print('3 Star')
    elif compound_score < 0.5:
        print('4 Star')
    else:
        print('5 Star')
    return ('The Text is in {}'.format(res))

print(sentimentAnalysis(cleaned_text))