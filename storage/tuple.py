tup = ("một", "hai", 12.3)

print(tup)

tup1 = tuple("abcd")

print(tup1)

tup2 = (("1", 2, 3), (), ('a', 'b', 'c'))

a = 'một' in tup
b = 'hai' in tup

s = "abcdef"
print(s[1:4])

tup3 = tuple("abcdabcd")
print(tup.count("a")) #count sẽ đếm số lần xuất hiện value trong tuple

value = 'a'
print(tup.index(value))