## "Клетки шахматной доски"

### Задание

Имеем стандартное поле шахматной доски размеров 8x8

![board.png](img/board.png)

Даны координаты двух клеток на шахматной доске.

Определить, одинакового ли цвета клетки?

### Формат входных данных

Даны четыре целые числа в диапазоне [1, 8]

### Формат выходных данных

Вывести "Да", если клетки с заданными координатам одинакового цвета, и "Нет", если разного.

### Решение задачи

```python
# Shershakov Grigoriy
# До того как открыл вторую подсказку))
a, b, x, y = int(input()), int(input()), int(input()), int(input())
if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):       # 1 number white
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):   # 2 number white
        print("Да")
    elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1): # 2 number black
        print("Нет")
elif (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0):     # 1 number black
    if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):   # 2 number black
        print("Да")
    elif (x % 2 == 0 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 0): # 2 number white
        print("Нет")
######################################################################################
# После того как открыл вторую подсказку))
a, b, x, y = int(input()), int(input()), int(input()), int(input())
if (a + b) % 2 == 0:        # 1 number white
    if (x + y) % 2 == 0:    # 2 number white
        print("Да")
    elif (x + y) % 2 == 1:  # 2 number black
        print("Нет")
elif (a + b) % 2 == 1:      # 1 number black
    if (x + y) % 2 == 1:    # 2 number black
        print("Да")
    elif (x + y) % 2 == 0:  # 2 number whte
        print("Нет")
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Условие для проверки четности числа:

```python
n % 2 == 0
```

</details>

<details>
<summary>Подсказка-2</summary>
Сумма двух нечетных чисел, всегда четная.
</details>
