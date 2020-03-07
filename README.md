# SiriusTextAnalyzer

Программа предобработки текстовых данных для участия в проекте образовательного центра «Сириус»: «Большие данные и машинное обучение в когнитивных и социальных науках»

## Начало

Следующие инструкции предоставят вам информации о возможностях проекта


### Установка

Склонируйте проект с репозитория для дальнейшего использования или скачайте его .zip файлом

```
git clone https://github.com/GerasimovRM/SiriusTextAnalyzer.git
```


## Описание классов

Проект содержит два основных класса:

* **TextReader** - класс для считывания данных в форматах txt, json, csv
* **TextFilter** - класс для фильтрации данных по критериям из задания


### TextReader и его методы

Класс находится в *text_analyzer/text_reader.py*

**TextReader.init(file_name[, file_type='txt'])**

```
Class for reading text

Available file formats: txt (default), json, csv

Parameters:
	file_name: File with text data
	file_type: One of the available file formats
```

**TextReader.read()

```
Return text data from source
	'txt' -> str
	'json' -> Dict
	'csv' -> List[Dict]

Return:
	File context
```

### TextFilter и его методы

Класс находится в *text_analyzer/text_filter.py*

**TextFilter.init([source_stop_words='stop_words.txt'])**

```
Class for filtering text

Parameters:
	source_stop_words: File with stop words ('stop_words.txt' (default) taken from https://github.com/stopwords-iso/stopwords-ru)
```

**TextFilter.add_stop_words(added_stop_words)**

```
Adds stop words in TextFilter from collection

Parameters:
	added_stop_words: Collection with stop words
```

**TextFilter.add_stop_words_from_file(file_name)**

```
Adds stop words from file

Parameters:
	file_name: File with stop words
```

**TextFilter.add_stop_words_from_file(file_name)**

```
Parsing text using functions:
	str.lower
	TextFilter.split_hash_tags
	TextFilter.remove_punctuation
	TextFilter.delete_irrelevant
	TextFilter.remove_stop_words
	TextFilter.transform_words_to_normal_form	

Parameters:
	text: Text to parse
Return:
	Iterator with parsed words
```




## Библиотеки

* [re](https://docs.python.org/3/library/re.html) - Модуль для работы с регулярными выражениями
* [pymorhy2](https://pymorphy2.readthedocs.io/en/latest/) - Модуль для морфологического анализа слов


## Авторы

* **Герасимов Роман Михайлович**

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. В файле [LICENSE.md](LICENSE.md)