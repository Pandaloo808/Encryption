from tkinter import *

root=Tk()
root.title("Encryption with ASCII Code")
root.geometry("400x300")
root.configure(bg="light blue")

ibox=Entry(root)
ibox.place(relx=0.5, rely=0.4,anchor=CENTER)
output=Label(root,bg="light blue", fg="red")

output2=Label(root,bg="light blue", fg="blue")

def ascii():
    name=ibox.get()
    asciicode=""
    encryption=""
    for letter in name:
        num=ord(letter)
        asciicode=asciicode +"  "+ str(num)
        k=num-1
        kValue=chr(k)
        encryption=encryption+str(kValue)
    output["text"]=asciicode
    output2["text"]=encryption
    
btn=Button(root,text="Display the ASCII Code and Encrypted Value", command=ascii, bg="purple", fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
output.place(relx=0.5,rely=0.6,anchor=CENTER)
output2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()

