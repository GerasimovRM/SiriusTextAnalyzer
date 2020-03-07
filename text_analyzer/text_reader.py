import json
from typing import Union, List, Dict


class TextReader:
    __TYPES = ("txt", "json", "csv")

    def __init__(self, file_name: str, file_type: str = 'txt'):
        """
        Class for reading text\n

        Available file formats: txt (default), json', csv\n

        :param file_name: File with text data
        :param file_type: One of the available file formats
        """
        if not file_name:
            raise TypeError("File source is bad name")

        self.file_name = file_name
        self.type = file_type
        if self.type not in self.__TYPES:
            raise TypeError("Type of source file is bad\n"
                            f"Available formats: {self.__TYPES}")

    def read(self) -> Union[str, Dict, List[Dict]]:
        """
        Return text data from source

        'txt' -> str

        'json' -> Dict

        'csv' -> List[Dict]

        :return: File context
        """
        if self.type == 'txt':
            return self.__read_txt()
        elif self.type == 'json':
            return self.__read_json()
        elif self.type == 'csv':
            return self.__read_csv()

    def __read_txt(self) -> str:
        with open(self.file_name, encoding='utf-8') as input_file:
            return input_file.read()

    def __read_json(self) -> Dict:
        with open(self.file_name, encoding='utf-8') as input_file:
            return json.loads(input_file.read())

    def __read_csv(self) -> List[Dict]:
        """
        !!! Using for task 2 !!!
        """
        with open(self.file_name, encoding='utf-8') as input_file:
            data = input_file.readlines()
        headers = data[0].replace(";", "").rstrip().split(",")
        results = []
        for line in data[1:]:
            if len(line) > 0:
                if line[0] == "\"":
                    line = line[1:]
                results.append(dict(list(zip(headers, line.split(",", 5)))))
        return results
