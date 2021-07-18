from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

folder_Name = ""

#location

def openLocation():
    global folder_Name
    folder_Name = filedialog.askdirectory()
    if(len(folder_Name) > 1):
        pathError.config(text=folder_Name,fg="green")
    else:
        pathError.config(text="Please choose a folder !!",fg="red")

#download video

def DownloadVideo():
    choice = drop_down.get()
    url = urlEntry.get()

    if(len(url) > 1):
        urlError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            urlError.config(text="Invalid link !!! please try again",fg="red")

#download button function
    select.download(folder_Name)
    urlError.config(text="Download Completed !!", fg="green")

root = Tk()
root.title("YouTube Downloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)

#link label

ytdLabel = Label(root,text="Enter the URL of the Video", font=("lorem ipsum",15))
ytdLabel.grid()

#entry_box

urlEntryVar = StringVar()
urlEntry = Entry(root,width=50,textvariable=urlEntryVar)
urlEntry.grid()

#error_msg for invalid url

urlError = Label(root,text=" ", fg="red",font=("jost",10))
urlError.grid()

#save file

saveLabel = Label(root,text="Save the File",font=("jost",15,"bold"))
saveLabel.grid()

#button for choosing location

savePath = Button(root,width=10,bg="red", fg="white",text="Choose Path",command = openLocation)
savePath.grid()

#error_msg for if no path input

pathError = Label(root,text="",fg="red",font=("jost",10))
pathError.grid()

#download quality

dQuality = Label(root,text="Select Quality", font=("jost",15))
dQuality.grid()

#drop_down

choices = ["720p","144p","only Audio"]
drop_down = ttk.Combobox(root,values=choices)
drop_down.grid()

#download button

down_button = Button(root,width=10,bg="green",fg="white",text="Download", command = DownloadVideo)
down_button.grid()

blankSpace1 = Label(root,text="                   ")
blankSpace1.grid()
blankSpace2 = Label(root,text="                   ")
blankSpace2.grid()
blankSpace3 = Label(root,text="                   ")
blankSpace3.grid()
blankSpace4 = Label(root,text="                   ")
blankSpace4.grid()

#developer_label

devLabel = Label(root,text="Magnum opUs  ~~shibz~~",font=("lorem ipsum",11))
devLabel.grid()


root.mainloop()