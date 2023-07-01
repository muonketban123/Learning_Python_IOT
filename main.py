from mypackage.library import*
from mypackage.myfunction import*
from mypackage.speak_hear import*
from threading import Thread
import requests as re

url  = "https://myproject-8695e-default-rtdb.asia-southeast1.firebasedatabase.app/test.json"

json = {"int" : 2}

def wiki_search(text):
    try:
        #Do chuỗi thông tin gửi về khá dài nên chúng ta chia thành các đoạn và lưu ở dạng list
        infor = wikipedia.summary(text).split('\n')
        speak(infor[0].split(".")[0])
        for a in infor[1:]: #chạy từ 1 cho đến hết
            speak("Bạn muốn nghe thêm không")
            ans = hear()
            if "có" not in ans:
                break
            speak(a)
        
        speak("Cảm ơn bạn đã lắng nghe, Bạn muốn giúp gì nữa không")
    except:
        speak("Mình không tìm được tài liệu bạn muốn tìm kiếm, Bạn muốn giúp gì khác không ?")

def Tro_Ly_Ao():
    f = open("database\\answer.txt", mode = "r", encoding= "utf8")
    answer = f.read().split("\n")
    speak("Xin chào mọi người, mình là trợ lý ảo BKFast")
    i = 1
    while True:
        you = hear()
        if you == None:
            i += 1
            #speak("Mình chưa nghe bạn nói gì cả.")
        elif "đói" in you or "hỗ trợ" in you or "cần giúp" in you:
            json["int"] = 2
            s = re.put(url = url, json = json)
            speak("Tôi đã gửi yêu cầu hỗ trợ cho bạn rồi")
        elif "tìm kiếm" in you and "thông tin" in you:
            wiki_search(you)
        else:
            index = handle_data(you)
            speak(answer[index])

thread1 = Thread(target= Tro_Ly_Ao)
thread1.start()

root.mainloop()
