## "Все совершенные число в диапазоне"

### Задание

Число совершенно, если оно равно сумме всех своих делителей, кроме самого себя. Пример: 6 = 1 + 2 + 3. \
Найдите все совершенные числа и их количество в заданном диапазоне [a, b].

### Формат входных данных

Даны два целых положительных числа, границы диапазона. Гарантируется, что a < b.

### Формат выходных данных

Вывести все совершенные числа, а затем их количество.

### Решение задачи

```python
# Shershakov Grigoriy
first_number, last_number = int(input("Введите первое число: ")), int(input("Введите последнее число: "))
input_number = first_number
line_perfect = ""
qty_divisors = 0
while input_number <= last_number:
    divisor = 0
    summ_divisors = 0
    while divisor < input_number:
        divisor += 1
        if input_number % divisor == 0 and divisor != input_number:
            summ_divisors += divisor
    if summ_divisors == input_number:
        qty_divisors += 1
        line_perfect += " " + str(input_number)
    input_number += 1
print("Количество чисел:", qty_divisors)
print("Числа:", line_perfect)
```

---

### Подсказки
<details>
<summary>Подсказка-1</summary>
Для решения задачи вам понадобятся вложенные циклы.

```python
while ...:  # внешний цикл
    while ...:  # внутренний цикл
        ...
```
Внешний цикл будет перебирать числа из диапазона, а внутренний проверять, является ли число совершенным.
</details>

<details>
<summary>Подсказка-2</summary>
Для проверки числа на совершенность, воспользуйтесь решение предыдущей задачи "Совершенное число".
</details>
