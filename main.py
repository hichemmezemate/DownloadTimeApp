from tkinter import * 
from tkinter import messagebox

down_app = Tk()

down_app.title("Calculate the time to download your file ")

down_app.geometry("400x300")

text0 = Label(down_app, text="", font=("Arial", 15))
text0.pack()

text1 = Label(down_app, text="Insert the size of your file in Gb", font=("Arial", 15))
text1.pack()

size = IntVar()
size.set('0')


file_size = Entry(down_app, width=4, font=("Arial", 20), textvariable=size, borderwidth=0)
file_size.pack()

text2 = Label(down_app, text="Insert your download speed in Mb/s", font=("Arial", 15), )
text2.pack()

speed = IntVar()
speed.set("0")

speed_input = Entry(down_app, width=4, font=("Arial", 20), textvariable=speed, borderwidth=0)
speed_input.pack()

def download():
    x = size.get()
    y = speed.get()
    if type(x) == str:
        messagebox.showinfo("ERROR", "please insert a valid number")
    else:
        u = float(x) * 1000 #size in mb
        t = u / float(y) #time in second
        l = t // 60 #time in minutes 
        k = t - (l*60)
        f = k * 60 #seconds
        h = l // 60 #hours
        j = l - (h*60) #what left in minutes
    #h = t / 60
    """ print("Your download will be ready in :")
    print("{} hours".format(int(h)))
    print("{} minutes".format(int(j)))
    print("{} second".format(int(k)) """

    messagebox.showinfo("Finished", "Your file will be downloaded in " + str(h) + " hours"
    "\n" "and " + str(j) + " minutes"
    "\n" "and " + str(k) + " second")

cliki = Button(down_app, text="Calculate", font=("Arial", 20), command=download)
cliki.pack()

down_app.mainloop()
