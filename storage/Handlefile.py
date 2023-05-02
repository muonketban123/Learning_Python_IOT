


'''file = open("text.txt", encoding= 'utf8', mode = "a")
file.write("\ntoàn đẹp trai x2")

file.close()'''


'''file = open("text.txt", encoding='utf8', mode="r")
s = file.read()
print(s)

s = s.split("\n")
print(s)

file.close()'''

#nhược điểm vẫn để ký tự \n nên dùng cách trên ok hơn
file = open("text.txt", encoding='utf8', mode="r")
s = file.readlines()
print(s)
file.close()


#file.seak(6) đọc từ ký tự thứ 6