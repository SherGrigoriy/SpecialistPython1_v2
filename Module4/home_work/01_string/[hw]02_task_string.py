# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
some_string = "тана строка состоящая из слов все слова разделены бовно одним пробелом"
low_some_string = some_string.lower()
if low_some_string[0] == "б":
    new_string = low_some_string.find(" ")
    print(some_string[:new_string])
else:
    find_space = low_some_string.find(" б")
    new_string = low_some_string[find_space+1:]
    word = new_string.find(" ")
    print(new_string[:word])
