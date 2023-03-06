# create a function that does sentiment analysis on the days transcripts

def sentiment_analysis(transcript_text):
    analyzer = vader.SentimentIntensityAnalyzer()
    sentences = nltk.sent_tokenize(transcript_text)
    scores = [(sentence, analyzer.polarity_scores(sentence)['compound']) for sentence in sentences]
    pos = [s for s in scores if s[1] > 0.5]
    neg = [s for s in scores if s[1] < -0.5]
    neu = [s for s in scores if abs(s[1]) < 0.5]
    return pos, neg, neu
