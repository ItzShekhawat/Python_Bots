from pytube import YouTube
from tkinter import *
import os



def download():
    link = ""
    path = r"C:\Users\Karni\Desktop\Coding\Python\Bots\YouTube\Tube_Videos"
    video = YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
    #video.download("C:\Users\Karni\Desktop\Coding\Python\Bots\YouTube\Tube_Videos")
   # print(str(link.get()))

download()


#Imprementing a GUI

"""

canvasCreation = Tk()
canvasCreation.geometry("300x500")
canvasCreation.title("YouTube Video Downloader")
Label_Title = Label(canvasCreation, text = "PASTE THE LINK HERE", font=("bold", 10))
Label_Title.place(x = 75 , y = 150)

link = StringVar()
path = StringVar()

link_Holder = Entry(canvasCreation, width = 45, textvariable = link)
link_Holder.place(x = 12, y = 200)

#-------------------------------------------------------------------------------------


Label_Title = Label(canvasCreation, text = "WHERE DO YOU WANT TO DOWNLOAD IT ?", font=("bold", 9))
Label_Title.place(x = 20 , y = 250)

path_Holder = Entry(canvasCreation, width = 45, textvariable = path)
path_Holder.place(x = 12, y = 300)


enter_Btn = Button(canvasCreation, text = "Download" , width = 25, bg = "green", fg = "white", command=download)
enter_Btn.place(x = 60 , y = 350)

canvasCreation.mainloop()

"""





