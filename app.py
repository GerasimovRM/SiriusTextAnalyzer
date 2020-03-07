# -*- coding: utf-8 -*-
from text_analyzer.text_reader import TextReader
from text_analyzer.text_filter import TextFilter
from text_analyzer.common import status_time


@status_time
def main():
    text_reader = TextReader('Данные для задания.csv', 'csv')
    text_filter = TextFilter()

    text = ' '.join(map(lambda x: x['body'], text_reader.read()))
    iter_obj = text_filter.parse_text(text)
    dict_res = {}
    for elem in iter_obj:
        if elem not in dict_res:
            dict_res[elem] = 0
        dict_res[elem] += 1

    with open("answer.txt", 'w') as output_file:
        for key, value in sorted(dict_res.items(), reverse=True, key=lambda x: x[1]):
            print(f"{key}: {value}", file=output_file)


if __name__ == '__main__':
    main()
