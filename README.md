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

stop_words.txt (default) взят с этого [репозитория](https://github.com/stopwords-iso/stopwords-ru) без слов: 
	даром
	дом
	деньги
	жизнь
	жить
	ребенок
	человек

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

**TextFilter.split_hash_tags(text)** - Парсинг хэш тегов

```
Parsing text with hash tags

Parameters:
	text: Text with illegible hash tags
	
Return:
	Text with parsing hash tags
```

**TextFilter.text_to_lower(text)** - Конвертирование всех символов в нижний регистр

```
Convert all symbols to lower case

Parameters:
	text: Source text
	
Return:
	Converted lowercase text
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
Remove all stop words (added earlier) from words

Stop words can be add using methods TextFilter.add_stop_words and TextFilter.add_stop_words_from_file

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

**TextFilter.parse_text(text)** - Парсинг текста в целом (применение функций, перечисленных ранее)

```
Parsing text using functions:
	TextFilter.split_hash_tags
	TextFilter.text_to_lower
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
	for word, count in sorted(dict_res.items(), key=lambda x: x[1], reverse=True):
		print(f"{count}: {word}", file=output_file)
```

### Ответ

```
1013: человек
844: благотворительный
721: ребёнок
682: помощь
657: жизнь
525: показать
511: полностью
487: деньга
438: добрый
399: фонд
385: дом
384: помочь
346: рубль
343: доброта
340: благотворительность
335: проект
333: организация
297: семья
261: праздник
255: участие
250: группа
239: февраль
236: помогать
233: сбор
217: средство
216: сумма
214: мероприятие
211: пара
206: карта
203: счёт
202: возможность
199: март
188: принять
187: поддержка
187: иоанн
180: история
179: жить
178: являться
173: центр
173: проявление
172: огромный
171: цель
171: право
170: необходимый
169: известный
168: область
168: проблема
166: любовь
165: добро
165: заниматься
163: пройти
162: александр
159: проходить
159: международный
157: родитель
156: мама
155: номер
152: отношение
151: волонтёр
151: образ
151: далее
150: любой
149: программа
148: вещий
148: новое
146: бог
145: месяц
144: просить
144: акция
143: провести
143: сердце
143: способ
142: спонтанный
142: находиться
140: число
139: святой
138: деятельность
135: поэтому
133: лечение
132: участник
132: рассказать
132: детский
131: смочь
131: здоровье
131: школа
130: разный
128: рф
128: результат
128: курс
127: общественный
127: принимать
127: состояние
126: неделя
125: перевод
125: компания
124: например
123: клуб
123: закон
123: ссылка
123: сша
...
```


## Библиотеки

* [re](https://docs.python.org/3/library/re.html) - Модуль для работы с регулярными выражениями
* [pymorhy2](https://pymorphy2.readthedocs.io/en/latest/) - Модуль для морфологического анализа слов


## Авторы

* **Герасимов Роман Михайлович**

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. В файле [LICENSE.md](LICENSE.md)