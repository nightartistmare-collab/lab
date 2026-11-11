# def greet(name):
#     print("Привет,", name)
# greet("Иван")
# def square(numb):
#     print(numb*numb)
# square(9)
# def max_of_two(a,b):
#     if a>b: print(a)
#     else: print(b)
# max_of_two(19,5)


# def calculate_rectangle(width,height):
#     print(width*height)
# calculate_rectangle(12,10)
# def calculate_perimeter(width,heignt):
#     print(width*2+heignt*2)
# calculate_perimeter(12,10)
# def describe_rectangle(width,heignt,unit="см"):
#     print("ширина -",width,"высота -",heignt)
# describe_rectangle(12,10)


# value=10
# def example():
#     value=20
#     print(value)
# example() # выводится значение из условия функции
# print(value) # выводится значение вне функции


# num =[10,11,12,13,14,15,16,17,18,19]
# print(num[0:3])
# num[2]=20
# print(num[2])
# num.append(30)
# num.remove(16)
# print("Список",num,"Длина",len(num))


# num=[1,2,3,4,5,6,7,8,9,10]
# print(num[0:2])
# print(num[-3::])
# print(num[2:7])
# print(num[::2])
# print(num[::-1])



# measurements =(1,2,3,4,5,6,7,8)
# print(measurements[0],measurements[2:5],measurements[-1])
# #measurements[2]=1 изменение невозможно тк кортеж это неизменяемый тип данных
# one = measurements[0]
# two = measurements[1]
# print(one, two)
# measure=list(measurements)
# measure[4]=12
# measurements=tuple(measure)
# print(measurements)


# num=[1,2,3,4,5,6,7,8,9,10]
# print(len(num))
# print(min(num))
# print(max(num))
# print(sum(num)/len(num))
# print(sorted(num))
# num.sort()
# print(num)


# def calculate_sum(num):
#     summ=0
#     for i in num:
#         summ+=i
#     print(summ)
# k=[1,2,3,4,5]
# calculate_sum(k)
# def calculate_min(num):
#     m=num[0]
#     for i in num:
#         if i<m:
#             m=i
#     print(m)
# k=[1,2,3,4,5]
# calculate_min(k)
# def calculate_max(num):
#     m=num[0]
#     for i in num:
#         if i>m:
#             m=i
#     print(m)
# k=[1,2,3,4,5]
# calculate_max(k)


# def find_element(num,tg):
#     for i in range(len(num)):
#         if num[i] == tg:
#             return i
#     return -1
# k=[1,2,4,5,8,-9]
# print(find_element(k,4))



# def analyze(num):
#     mn=(min(num))
#     mx=(max(num))
#     sr=(sum(num)/len(num))
#     return mn, mx, sr
# k=[1,2,3,4,5]
# a,b,c=analyze(k)
# print(a)
# print(b)
# print(c)


num=[-10,3,-2,8,-5]
print(sorted(num))
rs=sorted(num,key=lambda x: abs(x))
print(rs)


