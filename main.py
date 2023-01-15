import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox

try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')

try:
    import PyPDF2
except:
    os.system('pip install PyPDF2')


#----------------------------------------- Eng to Mp3 --------------------------------------------

def engToMp3Gui(*args):
    global selectfile, pathLabel, startFrom, startFromPage, startOperation, back
    backFromMainMenu()
    selectfile = Button(top, text='Select File', bg='red', fg='white', width=20, font='arial 12 bold', command=selectFile)
    selectfile.pack(pady=20)

    pathLabel = Label(top, text='File path: ', fg='white', bg='black', font='arial 10')
    pathLabel.pack()

    startFrom = Label(top, text='Start From Page Number', bg='black', fg='white', width=20, font='arial 12 bold')
    startFrom.pack(pady=10)

    startFromPage = Entry(top, width=22, font='arial 12 bold')
    startFromPage.pack()

    startOperation = Button(top, text='Convert', bg='red', fg='white', width=20, font='arial 12 bold', command=start)
    startOperation.pack(pady=10)

    back = Button(top, text='Back', bg='black', fg='white', width=20, font='arial 12 bold', command=backFromEngToMp3Gui)
    back.pack()

def start(*args):
    start = threading.Thread(target=start_running)
    try:
        start.start()
    except:
        pass

askFilePath = ""
def start_running(*args):
    if askFilePath == '':
        messagebox.showwarning("Notify!", "You Must Select a Pdf File")
    elif startFromPage.get() == "":
        messagebox.showwarning("Notify!", "Start Page Can't Empty\nType The Number of Page Start From or Type '0'")
    else:
        try:
            start = int(startFromPage.get())
            full_book = ""
            engine = pyttsx3.init()
            engine.setProperty('rate', 130)
            book = open(f"{askFilePath}", "rb")
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            for num in range(start, pages):
                page = pdfReader.getPage(num)
                text = page.extractText()
                full_book += text
            askSavePath = filedialog.askdirectory(title="Save in..")
            if askSavePath == '':
                messagebox.showerror("Error", "You Must Select Path to Save a New File")
            else:
                engine.save_to_file(full_book, f"{askSavePath}\\New-AudioBook.mp3")
                engine.runAndWait()
                messagebox.showinfo("Complete", "Mp3 File Now is ready to Listen")
        except:
            messagebox.showerror("Error", "Some values was incorrect!")

def selectFile(*args):
    global askFilePath
    askFilePath = filedialog.askopenfilename(title="Open Pdf File")
    pathLabel['text'] = "File Path: "+str(askFilePath)

def backFromEngToMp3Gui(*args):
    selectfile.destroy()
    pathLabel.destroy()
    startFrom.destroy()
    startFromPage.destroy()
    startOperation.destroy()
    back.destroy()
    MainMenu()


#------------------------------------------ Menu -------------------------------------------------
def MainMenu(*args):
    global mainLabel, convertEngPdf, convertArPdf
    mainLabel = Label(top, text="Pdf to AudioBook", fg='white', bg='red', width=300, font='arial 16 bold', height=2)
    mainLabel.pack()

    convertEngPdf = Button(top, text='English Pdf To Mp3', bg='red', fg='white', width=20, font='arial 12 bold', height=2, command=engToMp3Gui)
    convertEngPdf.pack(pady=100)

    convertArPdf = Button(top, text='Arabic Pdf To Mp3\n(Coming soon...)', bg='red', fg='white', width=20, font='arial 12 bold')
    convertArPdf.place(x=45, y=250)

def backFromMainMenu(*args):
    mainLabel.destroy()
    convertEngPdf.destroy()
    convertArPdf.destroy()
#------------------------------------- _home_ ------------------------------------------------
top = Tk()
top.title("Pdf to AudioBook")
top.geometry("300x450+400+10")
top.configure(background='black')
top.iconbitmap("")

MainMenu()

top.mainloop()