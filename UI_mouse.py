from tkinter import *
import videoCapture
import UIMouse


root = Tk()
root.geometry("1500x1000")

f1 = Frame(root)
f1.pack(side="top", fill="both", expand=True)
f1.place(x=0, y=0, relwidth=1, relheight=1)
f2 = Frame(root)
f2.pack(side="top", fill="both", expand=True)
f2.place(x=0, y=0, relwidth=1, relheight=1)
f3 = Frame(root)
f3.pack(side="top", fill="both", expand=True)
f3.place(x=0, y=0, relwidth=1, relheight=1)

def backgroundSetting():
    videoCapture.show()

def showMouse():
    UIMouse.simple()

def handgest():
   print("hello")



def raise_frame(frame):
    frame.lift()


def homepage(current):
    for widget in current.winfo_children():
        widget.destroy()
    raise_frame(f1)


def getpagetwo():
    f2.configure(background="#202d42")
    Label(f2, text="Instructions for Running", fg="white", bg="#202d42",
          font="Calibri 30 bold", pady=30).pack(fill="both")
    Label(f2, text="1. Use black screen as the background for better results.", fg="white", bg="#202d42",
          font="Calibri 25 bold", pady=30).pack(fill="both")
    Label(f2, text="2.Adjust the trackbars with little increments to form a contour around the hand.", fg="white",
          bg="#202d42",
          font="Calibri 25 bold", pady=30).pack(fill="both")
    Label(f2, text="3.Wait for Gesture to be recognised.", fg="white", bg="#202d42",
          font="Calibri 25 bold", pady=30).pack(fill="both")
    Button(f2, text="Start the system", font="Arial 20", width=30, bg="#2196f3", fg="white",
           pady=15, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white",command=lambda :handgest()).pack(fill="y")
    Button(f2, text="Back ->", font="Arial 20", width=30, bg="#2196f3", fg="white",
           pady=15, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white",
           command=lambda: homepage(f2)).pack(fill="y")
    raise_frame(f2)

def getpagethree():
    f3.configure(background="#202d42")
    Label(f3, text="Instructions for Running", fg="white", bg="#202d42",
          font="Calibri 30 bold", pady=30).pack(fill="both")
    Label(f3, text="1. This virtual mouse works with green coverings.", fg="white", bg="#202d42",
          font="Calibri 25 bold", pady=30).pack(fill="both")
    Label(f3, text="2.Put the green coverings on your thumb and index finger and keep them at a distance.", fg="white",
          bg="#202d42",
          font="Calibri 25 bold", pady=30).pack(fill="both")
    Label(f3, text="3.Bring them together up until a circle appears which simulates a click.", fg="white", bg="#202d42",
          font="Calibri 25 bold", pady=30).pack(fill="both")
    Button(f3, text="Start the system", font="Arial 20", width=30, bg="#2196f3", fg="white",
           pady=15, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white",command= lambda:showMouse()).pack(fill="y")
    Button(f3, text="Back ->", font="Arial 20", width=30, bg="#2196f3", fg="white",
           pady=15, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white",
           command=lambda: homepage(f3)).pack(fill="y")
    raise_frame(f3)


f1.configure(background="#202d42")
Label(f1, text="Hand Gesture Detection and Recognition", fg="white", bg="#202d42",
      font="Calibri 30 bold", pady=30).pack(fill="x")


btn_frame = Frame(f1, bg="#202d42", pady=30)
btn_frame.pack()

Button(btn_frame, text="Hand Gesture Recognition System", command=lambda: getpagetwo())
Button(btn_frame, text="Virtual Mouse",command=lambda: getpagethree())
Button(btn_frame,text = "Launch Camera for background setting",command = lambda: backgroundSetting())

for btn in btn_frame.winfo_children():
    btn.configure(font="Arial 20", width=30, bg="#2196f3", fg="white",
                  pady=7, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white")
    btn.pack(pady=30)

raise_frame(f1)
root.mainloop()