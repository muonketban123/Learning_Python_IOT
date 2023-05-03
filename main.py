from hear import*
from speak import*
from datetime import date, datetime, time
import webbrowser
import time
import wikipedia
wikipedia.set_lang("vi")

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

     
        


speak("Xin chào mọi người, mình là trợ lý ảo Bkfast")

while True:
    you = hear() 

    if you == None:
        speak("Mình chưa nghe bạn nói, bạn nói lại được không?")
   
    elif "tìm kiếm" in you and "thông tin" in you:
        wiki_search(you)
    elif "hôm nay" in you or "bây giờ" in you:
        now = datetime.now()
        if "giờ" in you:
            t = now.strftime("%H h, %M phút, %S giây")
            speak(t)
        if "ngày" in you:
            t = now.strftime("Hôm nay là ngày %d, tháng %m, năm %Y")
            speak(t)
    
    elif "mở" in you:
        if "facebook" in you:
            webbrowser.open("https://www.facebook.com/")
            time.sleep(1)
            speak("Facebook đã được mở")

        if "youtube" in you:
            webbrowser.open("https://www.youtube.com/")
            time.sleep(1)
            speak("Youtube đã được mở")
    #elif "mở" in you and "word" in you:
        #os.startfile("C:\Program Files\Microsoft Office\root\Office16")

    elif "con người" in you:
        speak("Mình chỉ là trợ lý ảo thôi")
    elif "hôm nay là ngày bao nhiêu" in you:
        speak("Hôm nay là 29/4")
    elif "chủ tịch" in you and "đầu tiên" in you:
        speak("là chủ tịch HỒ CHÍ MINH")
    elif "tạm biệt" in you:
        speak("Tạm biệt, hẹn gặp lại")
        break
