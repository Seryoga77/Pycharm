import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл '{file_name}' не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла '{file_name}': {e}")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word.lower())
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('teXT'))
