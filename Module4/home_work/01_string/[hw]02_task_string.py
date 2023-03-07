# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = "Дана строка состоящая из слов все слова разделены Ровно одним пробелом"
low_text = text.lower()

if low_text.find(" б") != -1:
    find_space = low_text.find(" б")
    new_string = low_text[find_space+1:]
    if new_string.find(" ") == -1:
        print(new_string)
    else:
        word = new_string.find(" ")
        print(new_string[:word])
elif low_text[0] == "б":
    new_string = low_text.find(" ")
    print(text[:new_string])
else:
    print("слов на б нет")
print(low_text.find(" б"))
