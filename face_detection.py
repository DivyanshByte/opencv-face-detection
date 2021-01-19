from tkinter import Tk
from tkinter.ttk import *
import webcam_face_detection
import image_face_detection
from tkinter import filedialog

window = Tk()

def start_cam():
    webcam_face_detection.start()

def start_file():
    filepath = filedialog.askopenfilename()
    image_face_detection.start(filepath)

btn = Button(window,text="Start WebCam",command=start_cam)
btn.pack()
btn2 = Button(window,text="Detect Face from Image",command=start_file)
btn2.pack()

window.title('Webcam Face detection')
window.geometry('300x300')
window.mainloop()
