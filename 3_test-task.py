#В архиве (https://drive.google.com/file/d/0B9inz0bjkoAKUm5YclNYdWNzWUU) найдёте большой текстовый файл. (4GB)

#Задание: ответить на вопросы:

#Сколько строк в файле?
#Сколько раз встречается «a»?
#Какие инструменты использовали?
#Сколько времени ушло на выполнение задания?


import os
from datetime import datetime

startTime = datetime.now()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# file_for_analyze = os.path.join(os.path.dirname(__file__),"datasets","test_text.txt")
file_for_analyze = os.path.join('/home/julia/Documents/search_job/','QAtest.txt')
print(file_for_analyze)

strings = 0
symbols_a = 0
with open(file_for_analyze, 'r') as file:
    for line in file:
        if(strings<=5): print(line)
        strings += 1
        symbols_a += line.lower().count("а")

endTime = datetime.now()
print(f'Strings: {strings}\nSymbols a&A: {symbols_a}')
print(f'Time of doing: {endTime - startTime}')
