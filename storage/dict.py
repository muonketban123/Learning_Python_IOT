a = {"a" : "1", "b" : 2}
print(a["a"])
print(type(a["b"]))

b = dict(name = "toan", age = 20, locate = "Hanoi")
print(b)
print(b['name']) #hiện ra toan

b["name"] = "kaka" #thay đổi toàn thành kaka
print(b['name'])

b["nyc"] = "rong"
print("Người yêu cũ của " + b['name'] + " là " + b["nyc"])

d = b #thay đổi trong d thì đồng nghĩa thay đổi trong b
c = b.copy()
c["name"] = "An" #KHÔNG ẢNH HƯỞNG TỚI b
print(c)

d = b.get("name") #trả về kaka

e = b.pop("name") #đẩy thằng name đi
print(e)
z = [(1,2), (3,4)]
b.update(z) #thêm 1:2, 3:4 vào b










