def summary_analysis(transcript_text):
    sentences = nltk.sent_tokenize(transcript_text)
    words = nltk.word_tokenize(transcript_text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words if not w in stop_words]
    fdist = nltk.FreqDist(filtered_words)
    summary = fdist.most_common(10)
    return summary
