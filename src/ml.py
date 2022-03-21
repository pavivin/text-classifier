from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

from configs import config
from data import Data

from case import ABCCase


class MLCase(ABCCase):
    def __call__(self):
        train_doc = Data.get_train_data()
        test_doc = Data.get_test_data()

        x_train, y_train = train_doc[config.text_column_name], train_doc[config.theme_column_name]
        x_test, y_test = test_doc[config.text_column_name], test_doc[config.theme_column_name]

        sgd_ppl_clf = Pipeline([('tfidf', TfidfVectorizer()), ('sgd_clf', SGDClassifier(random_state=42))])
        knb_ppl_clf = Pipeline([('tfidf', TfidfVectorizer()), ('knb_clf', KNeighborsClassifier(n_neighbors=10))])

        sgd_ppl_clf.fit(x_train, y_train)
        knb_ppl_clf.fit(x_train, y_train)

        predicted_sgd = sgd_ppl_clf.predict(x_test)
        predicted_knb = knb_ppl_clf.predict(x_test)

        print('', metrics.classification_report(predicted_sgd, y_test))
        print('', metrics.classification_report(predicted_knb, y_test))
