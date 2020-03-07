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

**TextReader.__init__** - инициализатор TextReader
"""
	Class for reading text\n

	Available file formats: txt (default), json', csv\n

	:param file_name: File with text data
	:param file_type: One of the available file formats
"""

### And coding style tests

Explain what these tests test and why

```
Give an example
```


## Библиотеки

* [re](https://docs.python.org/3/library/re.html) - Модуль для работы с регулярными выражениями
* [pymorhy2](https://pymorphy2.readthedocs.io/en/latest/) - Модуль для морфологического анализа слов


## Авторы

* **Герасимов Роман Михайлович**

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. В файле [LICENSE.md](LICENSE.md)