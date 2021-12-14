import TextBlob as TextBlob
from youtube_comment_scraper_python import *

link = input()
youtube.open(link)
all_data = []
for i in range(0, 10):
    response = youtube.video_comments()
    data = response['body']
    all_data.extend(data)

import pandas as pd

df = pd.DataFrame(data)
df = df[['Comment', 'Likes', 'Time']]
df.to_csv('data.csv', index=False)


def find_subjectivity_on_single_comment(text):
    return TextBlob(text).sentiment.subjectivity


def apply_subjectivity_on_all_comments(df):
    df['Subjectivity'] = df['Comment'].apply(find_subjectivity_on_single_comment)
    return df


df = apply_subjectivity_on_all_comments(df)

df.drop('Polarity', axis=1, inplace=True)
df.drop('pol_cat', axis=1, inplace=True)
df.drop('stop_comments', axis=1, inplace=True)


def find_polarity_of_single_comment(text):
    return TextBlob(text).sentiment.polarity


def find_polarity_of_every_comment(df):
    df['Polarity'] = df['Comment'].apply(find_polarity_of_single_comment)
    return df


analysis = lambda polarity: 'Positive' if polarity > 0 else 'Neutral' if polarity == 0 else 'Negative'


def analysis_based_on_polarity(df):
    df['Analysis'] = df['Polarity'].apply(analysis)
    return df


df = analysis_based_on_polarity(df)
df = find_polarity_of_every_comment(df)


def print_positive_comments():
    print('Printing positive comments:\n')
    sortedDF = df.sort_values(by=['Polarity'])
    for i in range(0, sortedDF.shape[0]):
        if 'Positive' == sortedDF['Analysis'][i]:
            print(str(i + 1) + '> ' + sortedDF['Comment'][i])
            print()


def print_negative_comments():
    print('Printing negative comments:\n')
    sortedDF = df.sort_values(by=['Polarity'])
    for j in range(0, sortedDF.shape[0]):
        if sortedDF['Analysis'][j] == 'Negative':
            print(str(j + 1) + '> ' + sortedDF['Comment'][j])
            print()


print_negative_comments()

print_positive_comments()


def print_neutral_comments():
    print('Printing neutral comments:\n')
    sortedDF = df.sort_values(by=['Polarity'])
    for k in range(0, sortedDF.shape[0]):
        if sortedDF['Analysis'][k] == 'Neutral':
            print(str(k + 1) + '> ' + sortedDF['Comment'][k])
            print()


print_neutral_comments()

import matplotlib.pyplot as plt
from sklearn.feature_extraction import text
from wordcloud import WordCloud


def generate_word_clouds(df):
    allWords = ' '.join([twts for twts in df['Comment']])
    wordCloud = WordCloud(stopwords=text.ENGLISH_STOP_WORDS, width=1000, height=600, random_state=21,
                          max_font_size=110).generate(allWords)
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


generate_word_clouds(df)
