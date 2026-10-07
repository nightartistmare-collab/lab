''']
age=8
has_acess = True
if ((age>17) and has_acess)==1:
    print("Возраст:",age)
    print("Допуск имеется",has_acess)
    print("Доступ разрешён")
else:
    print("Возраст:",age)
    print("Допуск имеется",has_acess)
    print("Доступ запрещён")
    '''
print("введите количество изменений")
n=int(input())
j=0 #сумма чисел всех введённых значений
for i in range(1,n+1):
    print("Введите измерения")
    q=float(input())
    j+-q
print("Сумма всех измерений",j)
print("Среднее арифметическое всех измерений",j/n)