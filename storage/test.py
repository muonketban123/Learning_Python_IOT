
import fractions
d = fractions.Fraction(12, 5)

a, b, c = 11, 12, 13
e = complex(3,4) # 3 + 4i

z = '123\
    hello'
g = '''123 hello
hello world'''
t = "I'm Toan"
print(len(t)) #in ra do dai chuoi t
print(t.upper()) #viết hoa các ký tự
print(t.lower()) #viết thường các ký tự
print(t.split(" ")) #"I'm" "Toan"


h = "1 2 3 4 5"
n = h.split(" ")
print(n)
v = ".".join(n)
print(v)

print(type(a))
print(type(b))
print(c)
print(d)
