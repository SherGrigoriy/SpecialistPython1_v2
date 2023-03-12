# Посчитайте количество согласных букв в данной строке.

# Shershakov Grigoriy
text = "Посчитайте количество согласных букв в данной строке."
consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
low_text = text.lower()
counter = 0
for letter in low_text:
    for find_consonants in consonants:
        if find_consonants == letter:
            counter += 1
print(counter)
