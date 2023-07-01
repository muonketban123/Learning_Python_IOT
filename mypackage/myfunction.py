
from mypackage.library import*
#mở file question.txt và đọc file lưu các câu hỏi ở dạng list
f = open("database\\question.txt", mode= "r", encoding= "utf8")
ques = f.read().split("\n")
#tạo hàm xử lý dữ liệu
def handle_data(text):
    #chia câu hỏi người dùng thành các từ riêng biệt
    text = text.split(" ")
    #khởi tạo lst rỗng để lưu tỉ lệ % giống nhau giữa câu hỏi người dùng và data question mình đã tạo
    ans = []

    #tính toán tỉ lệ % từng câu hỏi trong database bằng for
    for s in ques:
        #khởi tạo biến đếm số từ trùng lặp trong câu hỏi người dùng và câu hỏi trong database
        count = 0
        #tính toán số từ trùng lặp
        for i in text:
            if i in s:
                #cứ mỗi lần có từ trùng lặp thì count + 1
                count += 1
        #sau khi tính được số từ trùng lặp thì sẽ chia cho độ dài của câu hỏi trong database để lấy tỉ lệ % trùng lặp
        ratio = count * 100 / len(s)
        #append() tỉ lệ % đó vào lst
        ans.append(ratio)

    #trả về câu hỏi có tỷ lệ % tương ứng cao nhất
    print(ans)
    return numpy.argmax(ans) #thư viện ngoài numpy pip install numpy 





'''#đọc file answer.txt và lưu các câu hỏi ở dạng lst
f = open("database\\answer.txt", mode = "r", encoding= "utf8")
answer = f.read().split("\n")'''

'''index = handle_data("bạn tên là cái đéo gì vậy")
print(answer[index])'''


