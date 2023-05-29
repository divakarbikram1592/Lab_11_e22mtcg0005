import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest


def summarize(text, n):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words and remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word_tokenize(sentence.lower()) for sentence in sentences]
    words = [[word for word in sentence if word not in stop_words] for sentence in words]

    # Calculate the importance of each sentence based on word frequency
    freq = {}
    for sentence in words:
        for word in sentence:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1

    max_freq = max(freq.values())
    for word in freq:
        freq[word] = freq[word] / max_freq

    # Calculate the score of each sentence based on importance of words
    scores = {}
    for i in range(len(sentences)):
        scores[i] = 0
        for word in words[i]:
            if word in freq:
                scores[i] += freq[word]

    # Select the top n sentences with highest scores
    top_n = nlargest(n, scores, key=scores.get)
    summary = [sentences[i] for i in sorted(top_n)]
    return ' '.join(summary)

text = """Java is a programming language and a platform. Java is a high level, robust, object-oriented and secure programming language.
Java was developed by Sun Microsystems (which is now the subsidiary of Oracle) in the year 1995. James Gosling is known as the father of Java. 
Before Java, its name was Oak. Since Oak was already a registered company, so James Gosling and his team changed the name from Oak to Java."""

summary = summarize(text, 2)
print(summary)
