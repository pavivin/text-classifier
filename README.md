# Описание
Классификатор текстовых сообщений. 


На ввод любого текстового сообщения 
отвечает наименованием класса, к которому оно относится. 

Необходимо присвоить один из четырех классов: 

- кредит, 

- кредитная карта, 

- дебетовая карта, 

- не определено.


# Запуск
## Linux
```bash
python3 -m virtualenv env
source env/bin/activate
pip install -r all-requirements.txt
```

## Windows
```shell
python -m virtualenv env
env/bin/activate.ps1
pip install -r all-requirements.txt
```

```bash
python src/cli.py
# --method (nlp | ml | regex)
# --filename (data.xlsx)
# --input (predict text)
# --theme (predict class)
# --build (bool, rebuild default xlsx to csv)
# data/input_data.xlsx = default xlsx file

python src/cli.py --method nlp --input кредитка --theme кредитная карта
```

# Требования


#####

regexp/ -> заданные правила для поиска класса

nlp/ -> очистка текста, наивный алгоритм Байеса train_data с тестовыми

ml/ -> tf-df, метод ближайших соседей
