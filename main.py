# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# # Самостоятельно создайте DataFrame с данными
# # Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# # Вычислите среднюю оценку по каждому предмету
# # Вычислите медианную оценку по каждому предмету
# # Вычислите Q1 и Q3 для оценок по математике:
# # Q1_math = df['Математика'].quantile(0.25)
# # Q3_math = df['Математика'].quantile(0.75)
# # можно также попробовать рассчитать IQR
# Вычислите стандартное отклонение

import pandas as pd
import numpy as np
import random

pupils_list = {
    "ученики" : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Antonina', 'Serafin', 'Aleksandra', 'Robert', 'Paula'],
    "математика" : [],
    "физкультура" : [],
    "литература": [],
    "музыка": [],
    "технология": [],

}

for i in range(10):
    mark = random.randint(1, 5)
    pupils_list["математика"].append(mark)

for i in range(10):
    mark = random.randint(1, 5)
    pupils_list["физкультура"].append(mark)

for i in range(10):
    mark = random.randint(1, 5)
    pupils_list["литература"].append(mark)

for i in range(10):
    mark = random.randint(1, 5)
    pupils_list["музыка"].append(mark)

for i in range(10):
    mark = random.randint(1, 5)
    pupils_list["технология"].append(mark)

df = pd.DataFrame(pupils_list)

print(df, "\n")
print('\tсредние оценки:')
print('математика', df['математика'].mean())
print('физкультура', df['физкультура'].mean())
print('литература', df['литература'].mean())
print('музыка', df['музыка'].mean())
print('технология', df['технология'].mean())

print('\n\tмедианные оценки:')
print('математика', df['математика'].median())
print('физкультура', df['физкультура'].median())
print('литература', df['литература'].median())
print('музыка', df['музыка'].median())
print('технология', df['технология'].median())

Q1_math = df['математика'].quantile(0.25)
Q3_math = df['математика'].quantile(0.75)
print('\nQ1 по математике:', Q1_math)
print('Q3 по математике:', Q3_math)

#Межквартальный размах (IQR) вычисляется как разница между третьим и первым квартилями.
# Межквартальный размах показывает, как широко разбросаны средних 50 процентов значений, которые здесь есть
print('IQR по математике:', Q3_math - Q1_math)

print('\n\tстандартные отклонения:')
print('математика', round(df['математика'].std(), 4))
print('физкультура', round(df['физкультура'].std(), 4))
print('литература', round(df['литература'].std(), 4))
print('музыка', round(df['музыка'].std(), 4))
print('технология', round(df['технология'].std(), 4))

