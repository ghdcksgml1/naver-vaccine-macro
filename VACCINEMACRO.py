from tkinter import *
from tkinter import filedialog as fd
import backend
Chr_Folder=""

def btn_ready():
    backend.ready(entry0,entry1,entry2,Chr_Folder)

def btn_start():
    backend.start()

def btn_reset():
    backend.reset()


window = Tk()
window.title("VACCINE MACRO")
window.geometry("988x648")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 648,
    width = 988,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./images/background.png")
background = canvas.create_image(
    190.5, 324.0,
    image=background_img)

canvas.create_text(
    681.5, 86.5,
    text = "VACCINE MACRO",
    fill = "#000000",
    font = ("Roboto-Black", int(50.0)))

canvas.create_text(
    481.5, 223.5,
    text = "Link 1 : ",
    fill = "#000000",
    font = ("Roboto-Black", int(25.0)))

canvas.create_text(
    481.5, 290.5,
    text = "Link 2 : ",
    fill = "#000000",
    font = ("Roboto-Black", int(25.0)))

canvas.create_text(
    481.5, 357.5,
    text = "Link 3 : ",
    fill = "#000000",
    font = ("Roboto-Black", int(25.0)))

canvas.create_text(
    679.0, 583.0,
    text = "소프트웨어를 개발한 프로그래머나 저작권자는 어떠한 경우에도 소프트웨어나\n소프트웨어의 사용 등의 행위와 관련하여 일어나는 어떤 요구사항이나 손해 및\n기타 책임에 대해 계약상, 불법행위 또는 기타 이유로 인한 책임을 지지 않는다.",
    fill = "#cccccc",
    font = ("Roboto-Black", int(15.0)))

entry0_img = PhotoImage(file = f"./images/img_textBox0.png")
entry0_bg = canvas.create_image(
    732.0, 223.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 552, y = 209,
    width = 360,
    height = 27)

entry1_img = PhotoImage(file = f"./images/img_textBox1.png")
entry1_bg = canvas.create_image(
    732.0, 290.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 552, y = 276,
    width = 360,
    height = 27)

entry2_img = PhotoImage(file = f"./images/img_textBox2.png")
entry2_bg = canvas.create_image(
    732.0, 357.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 552, y = 343,
    width = 360,
    height = 27)

img0 = PhotoImage(file = f"./images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_ready,
    relief = "flat")

b0.place(
    x = 499, y = 424,
    width = 91,
    height = 39)

img1 = PhotoImage(file = f"./images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_start,
    relief = "flat")

b1.place(
    x = 636, y = 424,
    width = 91,
    height = 39)

img2 = PhotoImage(file = f"./images/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_reset,
    relief = "flat")

b2.place(
    x = 773, y = 424,
    width = 91,
    height = 39)
Chr_Folder = fd.askopenfilename()

window.resizable(False, False)
window.mainloop()
