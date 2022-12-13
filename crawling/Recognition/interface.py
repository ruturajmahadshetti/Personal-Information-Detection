from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import glob
import pandas as pd
import os
from retinaface import RetinaFace
import cv2
from deepface import DeepFace
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkinter import filedialog
import sqlite3
image=[]
def show():
    window = Tk()
    window.geometry("1900x1200")
    con = sqlite3.connect(database="img.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT, photo BLOB )")

    # ==========Variblels================
    var_name = StringVar()
    var_photo = StringVar()

    window.title("SMART IMAGE RECOGNIZER")
    tkinter.Label(window, text = "SMART IMAGE RECOGNIZER SYSTEM", font ="ar 35 bold", fg = "black", bg = "#FBC399").pack(fill = "x")
    tkinter.Label(window,text='Search where is image available...!',font ="Helvetica 20 bold", fg = "black",).pack()
    label1=tkinter.Label(window,text='Select image:',font ="Helvetica 15 bold", fg = "black",)
    label1.place(x=650,y=155)
    label2=tkinter.Label(window,text='Note: Image should consists face image',font ="Helvetica 10", fg = "black",)
    label2.place(x=650,y=195)
    # btn1 = tkinter.Button(window, text="CONTINUE", fg="black", bg='#F2D388', command=cont_inue)
    # btn1.place(x=360, y=450, width=80)

    btn1=tkinter.Button(window, text='Upload File',
                   width=30, command=lambda: upload_file())
    btn1.place(x=800, y=150)

    btn2 = tkinter.Button(window, text="Submit", font ="Helvetica 15 bold",fg="black", bg='#F2D388',
                          command=lambda: show_submit())#, command=cont_inue)
    btn2.place(x=750, y=220, width=200)

    def recognition(img):
        con = sqlite3.connect(database="std.db")
        cur = con.cursor()
        path = '/study/Ruturaj/Research work/AI_face_recognition/crawling/detection/'
        img =var_photo.get()
        try:
            if var_photo.get() == "":
                messagebox.showerror("Error")
            else:
                cur.execute("select * from std where name =? ", (var_photo.get(),))
                row = cur.fetchone()
                # if row != None:
                #     messagebox.showerror("Error", "Student name is already exists")
                # else:
                #     cur.execute("insert into std (name,photo) values (?,?)", (
                #         var_name.get(),
                #         var_photo.get()
                #     ))
                pf = pd.read_csv(path + 'filtered_data.csv')

                img_list = pf['image_path']
                web_page = pf['web_page']
                urls = pf['url']

                for i in range(10):

                    images = img_list[i]
                    # print(images)

                    obj = DeepFace.verify(img, images
                                          , model_name='SFace', detector_backend='retinaface')
                    if obj["verified"] == True:
                        return images, web_page[i], urls[i]
                con.commit()
                messagebox.showinfo({images}, web_page[i], urls[i])
        except Exception as ex:
            messagebox.showerror("Error", f"Error duo to {str(ex)}")
        # img='/study/Ruturaj/Research work/AI_face_recognition/crawling/images/img_13.jpg'
        import cv2



    def upload_file():
        def function(event):
            if (b2.cget('image') == img):
                b2.config(image=img)
        # Select the Imagename from a folder
        filename = filedialog.askopenfilename(initialdir="/",
                                              filetypes=(('JPG Files', '*.jpg'), ('PNG Files', '*.png')))
        image = Image.open(filename)
        image = image.resize((256, 256))
        img = ImageTk.PhotoImage(image)
        # var_photo = Label(img_LabelFrame, image=img)

        var_photo.image = image
        var_photo.pack()

        b2 = tkinter.Button(window, image=img)
        b2.config(image=img)
        b2.bind('<ButtonRelease>',function )
        b2.place(x=1150, y=200)
        label3=tkinter.Label(window,text='Uploaded Successfully...!',font ="Helvetica 15", fg = "black",)
        label3.place(x=1150, y=155)

    def show_submit():
        label4=tkinter.Label(window,text="Information about image ",font="ar 15", fg="black")
        label4.place(x=650, y=470)
        img=upload_file()
        print(img)
        btn2.cget()

        # img,webpage,link=recognition(img)
        # label4=Text(window, height = 5, width = 25,bg = "light cyan")
        # label4.insert(link)





    # def show_submit():
    #     window1 = Tk()
    #     window1.geometry("1900x1200")
    #   # window.configure(background='')
    #
    #     window1.title("SMART IMAGE RECOGNIZER")
    #     tkinter.Label(window1, text="SMART IMAGE RECOGNIZER SYSTEM", font="ar 35 bold", fg="black", bg="#FBC399").pack(fill="x")
    #     tkinter.Label(window1, text='Search where is image available...!', font="Helvetica 20 bold", fg="black", ).pack()
    #     tkinter.Label(window1, text='Search where is image available...!', font="Helvetica 20 bold",
    #                   fg="black", ).pack()
    #
    #     window1.mainloop()
    window.mainloop()

if __name__ == '__main__':
    show()
    # root = Tk()
    # root.geometry("600x400")
    #
    # # ==========Database================
    #
    #
    #
    # # ==========Method to Upload Image ================
    # def uploadImg():
    #     filename = filedialog.askopenfilename(initialdir="/",
    #                                           filetypes=(('JPG Files', '*.jpg'), ('PNG Files', '*.png')))
    #     image = Image.open(filename)  # Read the Image
    #
    #     resize_image = image.resize((200, 150))  # Reszie the image using resize() method
    #
    #     show_img = ImageTk.PhotoImage(resize_image)  # create label and to add the resize image
    #
    #     var_photo = Label(img_LabelFrame, image=show_img)
    #
    #     var_photo.image = show_img
    #     var_photo.pack()
    #
    #
    # # ==========Method to add The Name and  Image  to Database ================
    #
    #
    #
    #
    # # ==========Entry Fileds ================
    # bl_Name = Label(root, text="Student Name:", font=("Arial", 15,)).place(x=10, y=40)
    # En_Name = Entry(textvariable=var_name, font=("Arial", 15,), bg="lightyellow").place(x=150, y=40, width=250)
    #
    # lbl_Std_photo = Label(root, text="Student Photo: ", font=("Arial", 15,)).place(x=10, y=90)
    # img_LabelFrame = ttk.LabelFrame(root, text="")
    # img_LabelFrame.place(x=150, y=90, width=200, height=150)
    #
    # btn_upload_img = Button(text="Upload Image", bg="green", command=uploadImg).place(x=200, y=280, width=150,
    #                                                                                   height=40)
    # btn_save = Button(text="Save", bg="green", command=add).place(x=200, y=330, width=150, height=40)
    #
    # mainloop()
    #
    # # from tkinter import *
    # #
    # root = Tk()
    # root.geometry("300x300")
    # root.title(" Q&A ")
    #
    #
    # def Take_input():
    #     INPUT = inputtxt.get("1.0", "end-1c")
    #     print(INPUT)
    #     if (INPUT == "120"):
    #         Output.insert(END, 'Correct')
    #     else:
    #         Output.insert(END, "Wrong answe
    #
    #
    # l = Label(text="What is 24 * 5 ? ")
    # inputtxt = Text(root, height=10,
    #                 width=25,
    #                 bg="light yellow")
    #
    # Output = Text(root, height=5,
    #               width=25,
    #               bg="light cyan")
    #
    # Display = Button(root, height=2,
    #                  width=20,
    #                  text="Show",
    #                  command=lambda: Take_input())
    #
    # l.pack()
    # inputtxt.pack()
    # Display.pack()
    # Output.pack()
    #
    # mainloop()
    #
    #
    #
