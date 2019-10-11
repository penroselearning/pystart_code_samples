from tkinter import *
from tkinter.ttk import *
#import xlsxwriter
from datetime import datetime
screen=Tk()
screen.title("Student Registration Form")

s=Style()
s.configure('.', font=('verdana', 12),background='spring green')

def formdata():

    fields=['Name','Age','Gender','Mode of Transportation','Date']

    today = datetime.now()

    #workbook = xlsxwriter.Workbook('Students Form.xlsx')

    #worksheet = workbook.add_worksheet()

    # row=0
    # col=0
    # for f in fields:
    #     worksheet.write(row, col, f)
    #     col += 1
    #
    entries=[name.get(),gender.get(),agevar.get(),transportvar.get(),datetime.now()]
    #
    # col=0
    # row += 1
    # for x in range(len(entries)):
    #     worksheet.write(row,col,entries[x])
    #     col+=1
    #
    # workbook.close()

    print("The below Student has been successfully registered")
    print('-'*50)
    print(f'''Name:{name.get()}
Gender:{gender.get()}
Age:{agevar.get()}
Mode of Transportation:{transportvar.get()}
Regisration Date: {entries[4]}''')

options=['Car','Bus','Walking/Cycling']
form_questions=['Enter Name','Choose Gender', 'Enter Age', 'Mode of Transportation']

r=0
for form_question in form_questions:
    Label1 = Label(screen, text=form_question, style='TLabel')
    Label1.grid(row=r, column=0, sticky=NSEW)
    r+=1

name = Entry(screen, style='TEntry')
name.grid(row=0, column=1, columnspan=2, sticky=NSEW)

gender=StringVar()
Radio1=Radiobutton(screen,text="Male",value="Male",variable=gender)
Radio1.grid(row=1,column=1,sticky=NSEW)
Radio2=Radiobutton(screen,text="Female",value="Female",variable=gender)
Radio2.grid(row=1,column=2,sticky=NSEW)

agevar=IntVar(screen)
age=Spinbox(screen,width=25,from_=1,to=20,increment=1,textvariable=agevar)
age.grid(row=2,column=1,columnspan=2,sticky=NSEW)

transportvar=StringVar(screen)
transportvar.set(options[0])
transport=Combobox(screen,height=10,width=25,values=options,textvariable=transportvar)
transport.grid(row=3,column=1,columnspan=2,sticky=NSEW)

Button1=Button(screen,text="Submit",style='TButton',state=ACTIVE,command=formdata)
Button1.grid(row=4,column=0,columnspan=3,sticky=NSEW)

screen.mainloop()