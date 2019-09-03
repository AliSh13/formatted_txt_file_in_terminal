#!/usr/bin/python3
import sys

class FormattedText():
    """Форматирование текстого файла по ширине и """

    def len_w_s(self, array):
        """Возвращает количиство символов вместе с предпологаемыми пробелами
         из списка слов."""
        len_words = sum(list(map(len,array)))
        if len(array) > 1:
            len_space = len(array) - 1
        else:
            len_space = 0
        return len_words + len_space

    def formatted_list(self, list, width=80):
        """ Возвращает отформатированную строку из списка слов по заданной
        ширине (по умолчанию  - 80 символов )"""
        extra_spasec = width - self.len_w_s(list) # на сколько список меньше заданной ширины
        """ Добавляет пробелы в текст в зависимости от количества слов"""
        if extra_spasec > 0 and extra_spasec < self.len_w_s(list):
            if extra_spasec >= len(list):
                difference = extra_spasec - len(list) + 1
                for i in range(0, difference):
                    list[i] += ' '
                for i in range(0, extra_spasec - difference):
                    list[i] += ' '
            else:
                for i in range(0,extra_spasec):
                    list[i] += ' '

        formatted_text = ' '.join(list)
        return formatted_text

    def read_file(self, filename):
        """Открывает файл и разбивает текст на слова.
        После чего записывате отформатированный текст в результирующий списко """
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
            result = []
            for line in lines:
                words = line.split()
                if line.isspace():
                    continue
                words[0] = '  ' + words[0]
                formatted_line = []
                for word in words:
                    if self.len_w_s(formatted_line) + len(word) < 80:
                        formatted_line.append(word)
                        if word == words[-1]:
                            formatted_text = ' '.join(formatted_line) + '\n'
                            result.append(formatted_text)

                    else:
                        formatted_text = self.formatted_list(formatted_line)
                        result.append(formatted_text)
                        formatted_line.clear()
                        formatted_line.append(word)
                        if word == words[-1]:
                            formatted_text = ' '.join(formatted_line) + '\n'
                            result.append(formatted_text)

                        formatted_text = ''

            result.append('\t') # добавляет пусту строку после каждого абзаца
            return result

    def send_message(self, array=[], message=''):
        """Выводит сообщение в терминал"""
        if len(array) > 0:
            for string in array:
                print(string)
        elif message:
            print(type(message))

    def run(self):
        """ Запускает скрипт, предварительно проверив наличие аргументов
        и их допустимость"""
        try:
            args = sys.argv
            arg2 = sys.argv[1].split('.')[1]
            if len(args) == 2 and arg2 == 'txt':
                self.send_message(array = self.read_file(filename=sys.argv[1]))
            else:
                raise AttributeError

        except AttributeError:
            #перехватывает исключение не корректного атрибута.
            messge = ('Не допустимый формат файла или пути.')
            self.send_message(message=messge)


if __name__ == '__main__':
    main = FormattedText()
    main.run()
