from data import Data
from naive_bayes_classifier import tokenizer
from naive_bayes_classifier.classifier import Classifier
from naive_bayes_classifier.trainer import Trainer
from configs import config

newsTrainer = Trainer(tokenizer.Tokenizer(stop_words=[], signs_to_remove=["?!#%&"]))


reader = Data.get_csv_train_data()
for row in reader:
    newsTrainer.train(row[config.text_column_name], row[config.theme_column_name])

newsClassifier = Classifier(newsTrainer.data, tokenizer.Tokenizer(stop_words=[], signs_to_remove=["?!#%&"]))

unknownInstance = "деньги"
classification = newsClassifier.classify(unknownInstance)

predict_class, probability = classification[0]
print(predict_class, probability)
if probability == 0.00:
    predict_class = 'не определено'

print(predict_class)
