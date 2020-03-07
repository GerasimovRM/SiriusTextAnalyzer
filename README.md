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

**TextReader.init(file_name[, file_type='txt'])** - Инициализатор TextReader

```
Class for reading text

Available file formats: txt (default), json, csv

Parameters:
	file_name: File with text data
	file_type: One of the available file formats
```

**TextReader.read()** - Считывание данных из источника

```
Read text data from source

	'txt' -> str
	'json' -> Dict
	'csv' -> List[Dict]

Return:
	File context
```

### TextFilter и его методы

Класс находится в *text_analyzer/text_filter.py*

**TextFilter.init([source_stop_words='stop_words.txt'])** - Инициализатор TextFilter

```
Class for filtering text

Parameters:
	source_stop_words: File with stop words
```

stop_words.txt (default) взят с этого [репозитория](https://github.com/stopwords-iso/stopwords-ru)

**TextFilter.add_stop_words(added_stop_words)** - Добавление стоп слов из коллекции

```
Adds stop words in TextFilter from collection

Parameters:
	added_stop_words: Collection with stop words
```

**TextFilter.add_stop_words_from_file(file_name)** - Добавление стоп слов из файла

```
Adds stop words from file

Parameters:
	file_name: File with stop words
```

**TextFilter.split_hash_tags(text)** - Парсинг html тегов

```
Parsing text with hash tags

Parameters:
	text: Text with illegible hash tags
	
Return:
	Text with parsing hash tags
```

**TextFilter.remove_punctuation(text)** - Удаление пункутуации

```
Replace all punctuation symbols to white space

Parameters:
	text: Text with punctuation
Return:
	Filtered text without punctuation
```

**TextFilter.delete_irrelevant(text)** - Удаление нерелевантных слов

```
Remove links, HTML-tags, etc.

Parameters:
	text: Text to filter

Return:
	Filtered list of words
```

**TextFilter.remove_stop_words(words, stop_words)** - Удаление стоп слов

```
Remove all stop words from words

Parameters:
	words: Source list of words
	stop_words: Unnecessary words
	
Return:
	Filtered list of words
```

**TextFilter.transform_words_to_normal_form(words)** - Конвертирование слов в нормальную форму

```
Convert words to normal form
        
Parameters:
	Source list of words

Return:
	List of normal form words
```

**TextFilter.parse_text(text)** - Парсинг текста в целом (применение str.lower и пяти функций, перечисленных ранее)

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


## Пример работы
Выполнение тестового задания реализовано в файле app.py:

```python
# -*- coding: utf-8 -*-
from text_analyzer.text_reader import TextReader
from text_analyzer.text_filter import TextFilter


text_reader = TextReader('Данные для задания.csv', 'csv')
text_filter = TextFilter()

# считывание данных из 'Данные для задания.csv'
text = ' '.join(map(lambda x: x['body'], text_reader.read()))

# результат работы парсинга
iter_obj = text_filter.parse_text(text)

# построение алфавитно-частотного словаря
dict_res = {}
for elem in iter_obj:
		if elem not in dict_res:
				dict_res[elem] = 0
		dict_res[elem] += 1

# вывод алфавитно-частотного словаря, отсортированного по количеству употребления слов, в 'answer.txt'
with open("answer.txt", 'w') as output_file:
		for key, value in sorted(dict_res.items(), reverse=True, key=lambda x: x[1]):
				print(f"{key}: {value}", file=output_file)
```



## Библиотеки

* [re](https://docs.python.org/3/library/re.html) - Модуль для работы с регулярными выражениями
* [pymorhy2](https://pymorphy2.readthedocs.io/en/latest/) - Модуль для морфологического анализа слов


## Авторы

* **Герасимов Роман Михайлович**

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. В файле [LICENSE.md](LICENSE.md)