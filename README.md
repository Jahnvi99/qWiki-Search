# qWiki-Search

qWiki search helps user to gain knowledge about a topic in a jiffy. User enters topic and number of sentences he wants, as a result the user receives the relevant and latest sentences about the topic.

## Method used:

We find relevant wikipedia pages about the topic entered by the user. Next, sentences containing dates are extracted from the pages. tf-idf vectorization is computed for these sentences. This is then given as input for non-negative matrix factorization. 

Non - Negative Matrix Factorization (NMF) splits the document-word matrix (tfidf) into document-topic matrix (W) and topic-word matrix(H). Sentences giving highest score are then extracted from W and latest sentences are shown in chronological order.
