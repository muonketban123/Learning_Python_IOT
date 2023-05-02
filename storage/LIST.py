lst = ["một" , "hai", "ba", 1, 3, 3.4, 4.2]
lst1 = [1, 2, 3]
lst2 = ["một", "hai", "ba"]

print(lst[2])

print(lst2*3)

lst3 = list("1234")
print(lst3)

lst4 = [['a', 'b', 'c'], [1,2,3], [12.3, 14.5], []]
print(lst4[0][0])

lst5 = "một hai ba".split(" ")
print(lst5)

a = "một" in lst2
print(a) #true

b = "một" in lst1
print(b) #false


lst6 = ["môt", "hai", "ba"]
c = lst6.index("hai") #chỉ số
lst6.append("ba") #thêm "ba" vàl lst6
lst6.clear() #xoá sạch các phần tử trong list






