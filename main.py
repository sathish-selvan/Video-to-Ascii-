
import cv2
from PIL import Image
import sys
import os
from tkinter import filedialog
import tkinter

global UNIT
UNIT = 75

root = tkinter.Tk()
root.geometry("300x150")
root.title("Ascii stimulator")
root.iconbitmap("reso\hehe.ico")


bg = tkinter.PhotoImage(file="reso/download.png")

def ascii_convertion(img,UNIT):
    
    width, height = img.size
    ratio = height/width

    new_width = 50
    new_height = ratio*new_width

    img = img.resize((new_width,int(new_height)))

    img = img.convert("L")
    pixel = img.getdata()

    characters = ["@",'#',"S","%","?","*","+",";",":",",","."]

    new_pixel = [characters[pixels//25] for pixels in pixel]
    new_height = "".join(new_pixel)

    count = len(new_pixel)

    final_image = [new_pixel[index:index+new_width] for index in range(0,count,new_width)]
    txt_file = ""
    for i in final_image:

        txt_file += "".join(i)
        txt_file += "\n"

    # print(txt_file)
    with open("2.txt","w+") as f:
        
        f.write(txt_file)

    sys.stdout.write(txt_file)
    os.system("cls")
    

def live_cam():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)
    while True:
        success, imag = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow("Vedio",imag)
        cv2.waitKey(1)
        img = Image.fromarray(imag)
        # img = Image.open(frame)
        ascii_convertion(img,UNIT)
    cap.release()
    cv2.destroyAllWindows()



def find_path():
    global vedio_path

    vedio_path = filedialog.askopenfilename(initialdir ="reso/", title ="Choose a vedio file", filetypes=(("mp4 Files", "*.mp4"),("avi Files", "*.avi"), ))
    cap = cv2.VideoCapture(vedio_path)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)
    while True:
        success, imag = cap.read()
        cv2.imshow("Vedio",imag)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #convertion of cv2 image to PIl image object
        img = Image.fromarray(imag)
        # img = Image.open(frame)
        ascii_convertion(img,UNIT)

bg_lable = tkinter.Label(root,image=bg)
bg_lable.place(x=0,y=0,relwidth=1, relheight=1)

my_lable = tkinter.Label(root,text="Choose your options")
my_lable.pack(pady = 10,padx=10)



my_button = tkinter.Button(root, text="Select an vedio", command= find_path)
my_button.pack(pady = 10,padx=10)

my_button1 = tkinter.Button(root, text="Go live cam", command= live_cam)
my_button1.pack(pady = 10,padx=10)

root.mainloop()





