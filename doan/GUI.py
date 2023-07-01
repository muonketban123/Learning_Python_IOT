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

box1_("Chào trợ lý ảo !!!")
box2_("Xin chào, Mình là trợ lý ảo BKFast")

#root.loop() có tác dụng tạo vòng lặp chạy chương trình để hiển thị giao diện
root.mainloop()
