import speech_recognition as sr #install...

def hear():
    print("Đang nghe: ...")
    r = sr.Recognizer()       #lưu lại class recognizer dưới tên r
# source = sr.Microphone()
    with sr.Microphone() as source: #mở một microphone mới và lưu với tên source, sau khi thoát with as thì tắt microphone đi
        print("Tôi: ", end = '') 
        audio = r.listen(source, phrase_time_limit= 3) #lưu lại câu nói của mình dưới dạng âm thanh (.mp3)
        try:
            text = r.recognize_google(audio, language= "vi-VN")
            print(text)
            return str(text).lower()
        except:
            return None
        
print(hear())