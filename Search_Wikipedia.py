import wikipedia
wikipedia.set_lang("vi")

def wiki_search(text):
    try:
        #Do chuỗi thông tin gửi về khá dài nên chúng ta chia thành các đoạn và lưu ở dạng list
        infor = wikipedia.summary(text).split('\n')
        print(infor[0].split(".")[0])
        for a in infor[1:]: #chạy từ 1 cho đến hết
            print("Bạn muốn nghe thêm không")
            ans = input()
            if "có" not in ans:
                break
            print(a)
        
        print("Cảm ơn bạn đã lắng nghe, Bạn muốn giúp gì nữa không")
    except:
        print("Mình không tìm được tài liệu bạn muốn tìm kiếm, Bạn muốn giúp gì khác không ?")

wiki_search("Hồ Chí Minh")       
        
