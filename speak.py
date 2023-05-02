
from gtts import gTTS #pip install gtts
import playsound #pip install playsound==1.2.2
import os



def speak(text):
    print("BKfast: " + text)
    tts = gTTS(text = text, lang= "vi", slow= False ) #chuyển text thành âm thanh qua api google
    tts.save("sound.mp3") #sau khi gửi âm thanh về thì lưu lại tên sound.mp3
    playsound.playsound("sound.mp3", True) #phát file sound.mp3, true là khi bật âm thanh thì không chạy chương trình
    os.remove("sound.mp3") #xoá file sound.mp3
