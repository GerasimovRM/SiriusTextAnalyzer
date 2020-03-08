# -*- coding: utf-8 -*-
from text_analyzer.text_reader import TextReader
from text_analyzer.text_filter import TextFilter
from text_analyzer.common import status_time


@status_time
def main():
    text_reader = TextReader('Данные для задания.csv', 'csv')
    text_filter = TextFilter()

    # считывание данных из 'Данные для задания.csv'
    text = ' '.join(map(lambda x: x['body'], text_reader.read()))

    # результат работы парсинга
    iter_obj = text_filter.parse_text(text)

    # построение алфавитно-частнтного словаря
    dict_res = {}
    for elem in iter_obj:
        if elem not in dict_res:
            dict_res[elem] = 0
        dict_res[elem] += 1

    # вывод алфавитно-частотного словаря, отсортированного по количеству употребления слов, в 'answer.txt'
    with open("answer.txt", 'w') as output_file:
        for word, count in sorted(dict_res.items(), key=lambda x: x[1], reverse=True):
            print(f"{count}: {word}", file=output_file)


if __name__ == '__main__':
    main()
