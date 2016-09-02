import nltk
from nltk.classify import NaiveBayesClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

posts = nltk.corpus.nps_chat.xml_posts()


train_data = []
train_targets = []
classes = ['Statement', 'Greet', 'ynQuestion', 'Emotion', 'Accept', 'Reject', 'whQuestion', 'Continuer', 'yAnswer', 'Bye', 'Clarify', 'Emphasis', 'nAnswer', 'Other']
for post in posts:
  if post.get('class') == "System" : continue

  train_data.append(post.text)
  train_targets.append( classes.index(post.get('class')) )

count_vect = CountVectorizer()
X_train = count_vect.fit_transform(train_data)
#clf = MultinomialNB().fit(X_train, train_targets)
clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42).fit(X_train, train_targets)


pickle.dump( count_vect , open( 'vectorizer.pkl' , "wb" ) )
pickle.dump( clf , open( 'clf.pkl' , "wb" ) )

#X_new = count_vect.transform(test_data)
#predicted = clf.predict(X_new)
#print 'Raw counts accuracy: ',np.mean(predicted == test_targets) 

