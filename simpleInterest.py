from tkinter import *
window = Tk()

window.title('Simple Interest Calculator')
window.geometry("525x410")
window.configure(bg='pink')

def calculate_interest() :
    p=float(principal_entry.get())
    r=float(rate_entry.get())
    t=float(time_entry.get())
    i=(p*r*t)/100
    interest=round(i,2)
    result_label.destroy()
    message=Label(result_frame,text="Interest on ₹ "+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is ₹"+str(interest),bg="pink",font=("Calibri",12),width=55,height=3)
    message.place(x=20,y=40)
    message.pack()

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "brown", bg = "pink", font=("Calibri", 20),bd=5)
app_label.place(x=15, y=20)

principal_label=Label(window, text="Principal", fg = "brown", bg = "pink", font=("Calibri", 15),bd=1)
principal_label.place(x=40, y=90)

principal_entry=Entry(window, text="", width=22,bd=2)
principal_entry.place(x=190, y=92)

rate_label = Label(window, text="Rate of Interest", fg = "brown", bg = "pink", font=("Calibri",15),bd=1)
rate_label.place(x=40,y=140)

rate_entry = Entry(window,text="",width=22,bd=2)
rate_entry.place(x=190, y=140)

time_label = Label(window, text="Time (in years)", fg = "brown", bg = "pink", font=("Calibri",15),bd=1)
time_label.place(x=40,y=185)

time_entry = Entry(window,text="",width=22,bd=2)
time_entry.place(x=190, y=185)

calculator_button=Button(window,text="Calculate",fg="pink",bg="brown",command=calculate_interest,width=40)
calculator_button.place(x=40,y=250)

result_frame = LabelFrame(window,text="Result", bg = "pink", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=40,y=300)

result_label=Label(result_frame,text="Your result will be displayed here", bg = "pink", font=("Calibri", 12), width=55,height=3)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()