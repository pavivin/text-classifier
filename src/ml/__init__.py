import pandas as pd
import typer
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

from case import ABCCase
from utils import print_classes, print_statitics
from configs import config
from data import Data


class MLCase(ABCCase):
    def classify_text(self, df: pd.DataFrame):
        train_doc = Data().get_train_data()
        test_doc = df

        x_train, y_train = train_doc[config.text_column_name], train_doc[config.theme_column_name]
        x_test, y_test = test_doc[config.text_column_name], test_doc[config.theme_column_name]

        sgd_ppl_clf = Pipeline([('tfidf', TfidfVectorizer()), ('sgd_clf', SGDClassifier(random_state=42))])
        knb_ppl_clf = Pipeline([('tfidf', TfidfVectorizer()), ('knb_clf', KNeighborsClassifier(n_neighbors=10))])

        sgd_ppl_clf.fit(x_train, y_train)
        knb_ppl_clf.fit(x_train, y_train)

        predicted_sgd = sgd_ppl_clf.predict(x_test)
        predicted_knb = knb_ppl_clf.predict(x_test)

        count = 0

        for predict_class, right_class in zip(predicted_sgd, train_doc[config.theme_column_name]):
            if predict_class == right_class:
                count += 1
            print_classes(predict_class=predict_class, right_class=right_class)

        print_statitics(data_len=len(df), count=count)
