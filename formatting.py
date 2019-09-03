class FormattedText():
    """Форматирование текстого файла по ширине и """


    def read_file(self, filename):
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
                    if self.len_w_s(formatted_line) + len(word) < 81:
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


            result.append('\t')
            return result
