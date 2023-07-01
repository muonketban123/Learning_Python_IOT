import speech_recognition as sr #install...
from gtts import gTTS #pip install gtts
import playsound #pip install playsound==1.2.2
import os
from tkinter import * 
from PIL import Image, ImageTk

#đồ hoạ
root = Tk() 
root.title("BKFast Assistant") # Đặt tên tiêu đề
root.geometry("900x830") # Cài độ rộng cho background
root.iconbitmap("data_dohoa\\icon.ico") #chèn logo vào giao diện
load = Image.open("data_dohoa\\Background-la-gi.jpg") # Chèn background vào giao diện
render = ImageTk.PhotoImage(load) # Biến render giúp xuất background ra ngoài
img = Label(root, image = render) #label giúp hiển thị hình ảnh và văn bản
img.place(x=0, y= 0) #đặt background lên màn hình

#tạo biến label để giúp hiển thị chữ ra màn hình
name = Label(root, text = "BKFast ASSISTANT", fg = '#45F848', bg = '#03152D')
name.config(font = ("Transformers Movie", 35)) #cấu hình dùng font transformers Movie với cỡ chữ 35
name.pack(pady = 10) #pady = 10 để cách viền trục y 10 đơn vị


#box 1
#Tương tự tạo label name1 hiển thị chữ "BKFast HEAR" lên background
name1 = Label(root, text = "BKFast HEAR", fg = '#F8E245', bd = 0, bg = "#03152D")
name1.config(font = ("Transformers Movie", 20))
name1.pack(pady = 30)

#tạo một ô để hiển thị nội dung trợ lý ảo nghe được giao diện
box1 = Text(root, width = 48, height = 8, font = ("ROBOTO", 16))
box1.pack(pady = 0)

#box2
#Tạo label hiện thị text "BKFast Speak" lên background
name2 = Label(root, text = "BKFast SPEAK", fg = '#F8E245', bd = 0, bg = '#03153D')
name2.config(font = ("Transformers Movie", 20))
name2.pack(pady = 30)

#tạo ô để hiển thị nội dung trọ lý ảo speak ra giao diện
box2 = Text(root, width = 48, height = 9, font = ("ROBOTO", 16))
box2.pack(pady = 0)

#tạo hàm để xuất text ra box tương ứng đã tạo ở trên
def box1_(text):
    box1.delete(1.0, END) #xoá nội dung cũ trong box1
    box1.insert(END, text) # viết nội dung mới vào box1
def box2_(text):
    box2.delete(1.0, END) #xoá nội dung cũ trong box2
    box2.insert(END, text) # viết nội dung mới vào box2



#module hear



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
            box1_(text)
            return str(text).lower()
        except:
            return None
        
print(hear())

#module speak




def speak(text):
    box2_(text)
    print("BKfast: " + text)
    tts = gTTS(text = text, lang= "vi", slow= False ) #chuyển text thành âm thanh qua api google
    tts.save("sound.mp3") #sau khi gửi âm thanh về thì lưu lại tên sound.mp3
    playsound.playsound("sound.mp3", True) #phát file sound.mp3, true là khi bật âm thanh thì không chạy chương trình
    os.remove("sound.mp3") #xoá file sound.mp3
