import re
import nltk
import numpy as np
import wikipedia
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

nltk.download('punkt')

def qwiki_search(query, n):
  titles = wikipedia.search(query, results=5)
  if not titles:
    print ('The given query does not match any wikipedia page.')
    exit()
  data = []
  for title in titles:
      try:
          raw_data = wikipedia.page(title).content.replace('\n', ' ')
          processed_data = re.sub('== References ==.+|== See Also ==.+', '', raw_data)#removing irrelevant data from content
          data.append(processed_data)
      except Exception:
          pass

  articles = [nltk.sent_tokenize(text) for text in data]
  temporal_sentences = []
  for article in articles:
      for sentence in article:
          if re.search(r'\d{4}', sentence) is not None:               
              temporal_sentences.append(re.sub('=+.+?=+', '', sentence))
  tfidf_vectorizer = TfidfVectorizer(stop_words='english')
  tfidf = tfidf_vectorizer.fit_transform(temporal_sentences)

 
  nmf_model = NMF(n_components=1, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

  W = nmf_model.transform(tfidf)

 
  top_sent_indices = np.argsort( W[:,0] )[::-1][0:n]
  best_sentences = [temporal_sentences[sent_index] for sent_index in top_sent_indices]

 
  output = []
  for line in best_sentences:
      year = re.search(r'\d{4}', line).group()
      output.append((year, line))
  sorted_output = sorted(output, key=lambda tup: tup[0], reverse = True)
  return sorted_output

if __name__ == "__main__":
  query = input('Enter query: ')
  n = int(input('Enter number of sentences to be returned: '))
  sentences = qwiki_search(query, n)
  for item in sentences:
    print(item)