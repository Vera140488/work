# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром - слово или текст, который читается одинаково слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба. 

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Приводим строку к нижнему регистру и убираем пробелы
    return s == s[::-1]  # Сравниваем строку с ее перевернутой версией

user_input = input("Введите строку: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")

# Пользователь вводит с клавиатуры некоторый текст,
# после чегопользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст. 

def change_reserved_words(text, reserved_words):
    words = text.split()
    for i in range(len(words)):
        if words[i] in reserved_words:
            words[i] = words[i].upper()
    return ' '.join(words)

user_text = input("Введите текст: ")
reserved_words = input("Введите список зарезервированных слов через пробел: ").split()

new_text = change_reserved_words(user_text, reserved_words)
print("Измененный текст:")
print(new_text)

# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
# результат.

import re

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    # Удаляем пустые строки, которые могут возникнуть после разделения текста
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)

user_text = input("Введите текст: ")

num_sentences = count_sentences(user_text)
print("Количество предложений в тексте:", num_sentences)
