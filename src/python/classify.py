import pickle
import sys, getopt

classes = ['Statement', 'Greet', 'ynQuestion', 'Emotion', 'Accept', 'Reject', 'whQuestion', 'Continuer', 'yAnswer', 'Bye', 'Clarify', 'Emphasis', 'nAnswer', 'Other']

count_vect = pickle.load( open( "/home/rdorado/project/dialogs/src/python/vectorizer.pkl", "rb" ) )
clf = pickle.load( open( "/home/rdorado/project/dialogs/src/python/clf.pkl", "rb" ) )

doc = [str(sys.argv[1])]
X_new = count_vect.transform(doc)
predicted = clf.predict(X_new)


print classes[predicted]
