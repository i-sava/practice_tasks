"""
Задається послідовність чисел з клавіатури.
Знайти всі числа більші за 5 та збільшити їх вдвічі, вивести їх та обчислити їхню суму
"""

lst = list(map(int,input('введіть числа через пробіл у список   ').split()))
print(lst)

lst2 = [x for x in lst if x > 5]
print(lst2)

s = 0
for i in range(len(lst)):
  if lst[i] > 5:
    lst[i] = lst[i] * 2
  s = s + lst[i]
print(lst)
print(s)
print(sum(lst))

lst2 = [x for x in lst if x > 5]
print(lst2)