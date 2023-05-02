# ==, >, <, <=, >=, in

a = 12
if a == 12:
    print("a = 12")
elif a == 11:
    print("a = 11")
else: 
    print("a không bằng 12")


for i in range(0,12): #in đến 12
    print(i)

lst = ['một', 'hai', 3, 4]
for s in lst:
    print(s)

while(a > 0):
    print(a) 
    a -= 1

while True:
    print("vong lap vo han")
    a -= 1
    if(a == 0): 
        break


for i in range(0,12):
    if(i % 2 == 0):
        continue #tiếp tục vòng lặp bỏ qua các lệnh dưới nó
    print(i)