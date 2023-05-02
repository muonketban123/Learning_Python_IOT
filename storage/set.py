t = {'a', 'b', 23, 4} #set không chưa phần tử trùng lặp
print(t)
b = set("abcdgf")
a = {1, 1, 2, 4, 4, 5, 6, 3, 9}

print(a.remove(1)) #báo lỗi nếu không có phần tử 1
print(a.discard(1)) #không báo lỗi giả sử nếu không có phần tử 1
print(a.add(3))

print(b)
print(a)

set1 = {1, 2, 3, 4}
set2 = {2, 4, 5}

set3 = set1 - set2
set3 = set1 & set2
print(set3)

t.clear() #xoá sạch các phần tử của t

try: 
    k1 = t.pop()
    k2 = t.pop()
except: 
    print(" không POP được đâu bé ơi")

print(b)