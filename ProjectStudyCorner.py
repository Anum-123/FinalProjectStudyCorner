import tkinter
import datetime
from tkinter import messagebox
global l_b
global my_entry
global lb
global entry_1
global entry_2
global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
global text
global m_w 
global root

#create registration form
def reg():
    global main_window
    global bookInfo1
    global bookInfo2
    global entry_4
    global bookInfo3
   
    #create tkinter window
    main_window =tkinter.Tk()
    main_window.title("STUDY CORNER REG FORM")
    main_window.geometry("1700x900")
    top_frame=tkinter.Frame(main_window)
   
    #create canvas
    Canvas1 =tkinter.Canvas(main_window)
   
    Canvas1.config(bg="dark olive green")
    Canvas1.pack(expand=True,fill=tkinter.BOTH)
    # library name
    headingFrame1 = tkinter.Frame(main_window,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.03,relwidth=0.5,relheight=0.16)
    headingLabel = tkinter.Label(headingFrame1, text="STUDY CORNER", bg='purple2', fg='black', font=('Times', 25, 'bold italic'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # form
    headingFrame2 = tkinter.Frame(main_window,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.25,rely=0.23,relwidth=0.5,relheight=0.13)
    headingLabel = tkinter.Label(headingFrame2, text="REGISTRATION\nFORM", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame= tkinter.Frame(main_window,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
       
    # full name
    lb1 = tkinter.Label(labelFrame,text="FULL NAME: ", bg='black', fg='white',font=("Courier", 13))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
       
    bookInfo1 = tkinter.Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.45, relheight=0.08)
       
    # gender
    lb2 = tkinter.Label(labelFrame,text="GENDER: ", bg='black', fg='white',font=("Courier", 13))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
   
    var = tkinter.IntVar(labelFrame)
    rb1=tkinter.Radiobutton(labelFrame, text="MALE",padx=15,pady =10, variable=var, value=1)
    rb1.place(relx=0.30,rely=0.35,relheight=0.08)
    rb2=tkinter.Radiobutton(labelFrame, text="FEMALE",padx =20,pady=10, variable=var, value=2)
    rb2.place(relx=0.5,rely=0.35,relheight=0.08)
   
    #age
    label_4 = tkinter.Label(labelFrame, text="AGE:",bg='black', fg='white',font=("Courier", 13))
    label_4.place(relx=0.05,rely=0.50, relheight=0.08)
    entry_4 = tkinter.Entry(labelFrame)
    spin = tkinter.Spinbox(labelFrame, textvariable=entry_4,from_=0, to=100)
    spin.place(relx=0.3,rely=0.50, relheight=0.08)
   
    #email
    lb2 = tkinter.Label(labelFrame,text="EMAIL: ", bg='black', fg='white',font=("Courier", 13))
    lb2.place(relx=0.05,rely=0.60, relheight=0.08)
    bookInfo2 = tkinter.Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.60, relwidth=0.45, relheight=0.08)
   
    #contact
    lb3 = tkinter.Label(labelFrame,text="CONTACT: ", bg='black', fg='white',font=("Courier", 13))
    lb3.place(relx=0.05,rely=0.7, relheight=0.08)
    bookInfo3 = tkinter.Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.7, relwidth=0.45, relheight=0.08)
   
    #create button
    SubmitBtn =tkinter. Button(main_window,text="SUBMIT",bg='grey', fg='black',font=("Courier", 13),command=log)
    SubmitBtn.place(relx=0.4,rely=0.83, relwidth=0.18,relheight=0.08)
    main_window.mainloop()

def log():
    #validation for registration form
    global main_window
    global bookInfo1
    global bookInfo2
    global entry_4
    global bookInfo3
    global var
    main_window.after(10000, lambda: main_window.destroy()) # Destroy the widget after 30 seconds
    if (bookInfo1.get().isalpha() and bookInfo3.get().isdigit()):
        option()
    else:
        messagebox.showinfo('Response',"invalid")
def option():
    #create options buttons
    main_window = tkinter.Tk()
    main_window.title("STUDY CORNER")
    main_window.minsize(width=400,height=400)
    main_window.geometry("1700x900")
    main_window.config(bg="dark olive green")

    headingFrame1 =tkinter. Frame(main_window,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = tkinter.Label(headingFrame1, text="WELCOME TO \nSTUDY CORNER", bg='black', fg='white', font=('Courier',20,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = tkinter.Button(main_window,text="VIEW BOOK",bg='black', fg='white',font=("Courier", 13),command=viewbook)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
   
    btn2 = tkinter.Button(main_window,text="LEND BOOK",bg='black', fg='white',font=("Courier", 13),command=lend_book)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
   
    btn3 = tkinter.Button(main_window,text="DONATE BOOK",bg='black', fg='white',font=("Courier", 13),command=donate_book)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
   
    btn4 = tkinter.Button(main_window,text="RETURN BOOK",bg='black', fg='white',font=("Courier", 13),command=return_book)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
   
    btn5 = tkinter.Button(main_window,text="FEED BACK",bg='black', fg='white',font=("Courier", 13),command=feed)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
   
    btn5 = tkinter.Button(main_window,text="EXIT",bg='black', fg='white',font=("Courier", 13),command=main_window.destroy)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    main_window.mainloop()

#create viewbookk
def viewbook():
    main_window = tkinter.Tk()
    main_window .title('STUDY CORNER')
    main_window.geometry("1700x900")
    top_frame = tkinter.Frame(main_window)
    bottom_frame = tkinter.Frame(main_window)
    main_window.config(bg="black")
    frame =tkinter.Frame(main_window )
    frame.pack(pady=10)
   
    #displaying list in listbox
    l_b=tkinter.Listbox(frame, width=110,height=20,font=('Times', 18),bd=0,bg="black",fg='yellow',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none")
    l_b.pack(side="left", fill=tkinter.BOTH)

    task_list=["        S.NO       BOOKS NAME                    AUTHOR                       EDITION",              
               
               '           1.                c++                                   Bjarne                             2017      ',
               '           2.               java                                   Brain                                2009',
               '           3.     Computer Programs                  Donald                              2000',
               '           4.     Computer Networks                  Behrouz                             2019',
               '           5.     Introduction to DBS                  Christopher                       2000',
               '           6.     Starting out with python           Tony                                  1999',
               '           7.     Close to the Machine                Ellen Ullman                       2015',
               '           8.     Computer Algorithms               Ellis Horowitz                       2008 ',
               '           9.     Unix Programming                     Ellis Horowitz                     1998',
               '          10.    Psychology Programming          Eric Raymond                      2011',
               '          11.    Software Writing I                     Joel Spolsky                          1990',
               '          12.    Software Wars                           Keith Curtis                          2011',
               '          13.    Free Software                            Richard                                 2007',
               '          15.    Free Society                              Richard                                  1989',
               '          16.    Patterns of Software                  Richard Gabriel                     1999',
               '          17.    Innovation Happens                   Richard P.G                          2002',                
               "          18.    The Happy Prince                      Oscar Wilde                          1888",
               "          19.    The Magic Shop                         H.G. Wells                            1903",
               "          20.    Rip Van Winkle                         Washington-I                        1819",
               "          21.    Moby-Dick                              Herman Melville                      2016",
               "          22.    Wuthering Heights                      Emily Brontë                        1999",
               "          23.    War and Peace                              Tolstoy                             2000",
               "          24.    The Odyssey                                 Homer                              2002",
               "          25.    Hamlet                                 William Shakespeare                  2007",
               "          26.    Crime and Punishment           Fyodor Dostoyevsky                1976",
               "          27.    Pride and Prejudice                    Jane Austen                          2000",
               "          28.    Jannat ke pattey                        Nimra ahmed                         1999",
               "          29.     Harry potter                           J. K. Rowling                         1965"]

    for item in task_list:
        l_b.insert("end", item)

    #create scrollbar
    sb =tkinter.Scrollbar(frame)
    sb.pack(side="right",fill=tkinter.BOTH)

    l_b.config(yscrollcommand=sb.set)
    sb.config(command=l_b.yview)
    quitBtn = tkinter.Button(main_window,text="QUIT",bg='grey', fg='white',font=("Courier", 15,"bold"), command=main_window.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    tkinter.mainloop()
   

#function of lendbook
def lend_book():    
    global bookInfo1
    global bookInfo2
    global m_w 
    m_w=tkinter.Tk()
    m_w.title('LEND BOOK')
    m_w.config(bg='#223441')
    m_w.geometry("1700x900")
    Canvas1 = tkinter.Canvas(m_w)
    Canvas1.config(bg="dark olive green")
    Canvas1.pack(expand=True,fill=tkinter.BOTH)
       
    headingFrame1 =tkinter. Frame(m_w,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
       
    headingLabel = tkinter.Label(headingFrame1, text="ISSUE BOOK", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
   
    labelFrame = tkinter.Frame(m_w ,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
       
    # Book name to Delete
    lb2 = tkinter.Label(labelFrame,text="BOOK NAME: ", bg='black', fg='white', font=('Courier',12))
    lb2.place(relx=0.05,rely=0.3)
       
    bookInfo1 = tkinter.Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.3, relwidth=0.62)
   
    # Book author to Delete
    lb3 = tkinter.Label(labelFrame,text="AUTHOR NAME: ", bg='black', fg='white', font=('Courier',12))
    lb3.place(relx=0.05,rely=0.5)
       
    bookInfo2 = tkinter.Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.5, relwidth=0.62)
   
   
    #Submit Button
    SubmitBtn =tkinter. Button(m_w ,text="SUBMIT",bg="chocolate1", fg='black',font=("Courier", 13),command=lendbook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
   
    quitBtn = tkinter.Button(m_w ,text="QUIT",bg='burlywood', fg='black',font=("Courier", 13),command=m_w.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
   
    m_w.mainloop()

#validation and operation for lend book
def lendbook():
    global bookInfo1
    global bookInfo2
    global m_w 
    x = datetime.datetime.now() #w3school
    b=str(x.strftime("%A"))
    today =str(datetime.date.today())
    task_list=['c++','java','The Art of Computer Programming','Computer Networks',
               'Introduction to Database System','Starting out with python','Close to the Machine',
               'Fundamentals of Computer Algorithms','The Art of Unix Programming',
               'The Psychology of Computer Programming','The Best Software Writing I',
               'After the Software Wars','Free Software','Free Society','Patterns of Software',
               'Innovation Happens Elsewhere',"The Happy Prince","The Magic Shop","Rip Van Winkle","Moby-Dick",
               "Wuthering Heights","War and Peace","The Odyssey","Hamlet","Crime and Punishment",
               "Pride and Prejudice","Jannat ke pattey","Harry potter"]
   
    authors=["Bjarne","Brain","Donald","Behrouz","Christopher","Tony","Ellen Ullman","Ellis Horowitz",
             "Ellis Horowitz","Eric Raymond","Joel Spolsky","Keith Curtis","Richard","Richard","Richard Gabriel",
             "Richard P.G,Oscar Wilde","H.G. Wells","Washington-I","Herman Melville","Emily Brontë",
             "Tolstoy","Homer","William Shakespeare","Fyodor Dostoyevsky","Jane Austen","Nimra ahmed","J. K. Rowling"]
   
    if (bookInfo1.get() != "" and bookInfo2.get()!= ""):
        if (bookInfo1.get() in task_list):
            if (bookInfo2.get() in authors):
                task_list.remove(bookInfo1.get())
                authors.remove(bookInfo2.get())
                messagebox.showinfo('Response',"you lend this book on " + today+"  "+b+ "\nHope.. it will beneficial for you...!!")
                print("Books")
                for i in task_list:
                    print(i,", ",end="")
                print("\n")
                print("Authors")
                for i in authors:
                    print(i,", ",end="")
                m_w.destroy()
            else:
                messagebox.showinfo('Response',"NOT AVAILABLE...!!")
        else:
            messagebox.showinfo('Response',"NOT AVAILABLE...!!")
    else:
        messagebox.showinfo('Response',"write anything...!!")

#function for return book
def return_book():
    global bookInfo2
    global bookInfo3
    global bookInfo4
    global root
    root = tkinter.Tk()
    root.title("Library")
    root.geometry("1700x900")
    Canvas1 =tkinter.Canvas(root)
   
    Canvas1.config(bg="dark olive green")
    Canvas1.pack(expand=True,fill=tkinter.BOTH)
       
    headingFrame1 = tkinter.Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = tkinter.Label(headingFrame1, text="Return Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = tkinter.Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
       
       
    # Title
    lb2 = tkinter.Label(labelFrame,text="BOOK NAME: ", bg='black', fg='white',font=("Courier", 13))
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
       
    bookInfo2 =tkinter.Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
       
    # Book Author
    lb3 = tkinter.Label(labelFrame,text="AUTHOR NAME: ", bg='black', fg='white',font=("Courier", 13))
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
       
    bookInfo3 =tkinter.Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
   
    lb4 = tkinter.Label(labelFrame,text="EDITION: ", bg='black', fg='white',font=("Courier", 13))
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
       
    bookInfo4 =tkinter.Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)
       
    #Submit Button
    SubmitBtn = tkinter.Button(root,text="SUBMIT",bg='chocolate1', fg='black',font=("Courier", 13),command=rb)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
   
    quitBtn = tkinter.Button(root,text="QUIT",bg='burlywood', fg='black',font=("Courier", 13),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
   
    root.mainloop()

#validation and operation for return book
def rb():
    global bookInfo2
    global bookInfo3
    task_list=['c++','java','The Art of Computer Programming','Computer Networks',
               'Introduction to Database System','Starting out with python','Close to the Machine',
               'Fundamentals of Computer Algorithms','The Art of Unix Programming',
               'The Psychology of Computer Programming','The Best Software Writing I',
               'After the Software Wars','Free Software','Free Society','Patterns of Software',
               'Innovation Happens Elsewhere',"The Happy Prince","The Magic Shop","Rip Van Winkle","Moby-Dick",
               "Wuthering Heights","War and Peace","The Odyssey","Hamlet","Crime and Punishment",
               "Pride and Prejudice","Jannat ke pattey","Harry potter"]
   
    authors=["Bjarne","Brain","Donald","Behrouz","Christopher","Tony","Ellen Ullman","Ellis Horowitz",
             "Ellis Horowitz","Eric Raymond","Joel Spolsky","Keith Curtis","Richard","Richard","Richard Gabriel",
             "Richard P.G,Oscar Wilde","H.G. Wells","Washington-I","Herman Melville","Emily Brontë",
             "Tolstoy","Homer","William Shakespeare","Fyodor Dostoyevsky","Jane Austen","Nimra ahmed","J. K. Rowling"]
    editions=['2010','2015','2017','2020','2005','2009','2004','2008','2010','2011','2009','2010','2006','2016','2004','2017']
    if (bookInfo2.get() != "" and bookInfo3.get()!= "" and bookInfo4.get()!=""):
        try:
            if(bookInfo2.get().isalpha() and bookInfo3.get().isalpha() and bookInfo4.get().isdigit()):
                task_list.append(bookInfo2.get())
                authors.append(bookInfo3.get())
                editions.append(bookInfo4.get())
                messagebox.showinfo('Response',"Thanks for returning...!!")
                print("Books")
                for i in task_list:
                    print(i,", ",end="")
                print("\n")
                print("Authors")
                for i in authors:
                    print(i,", ",end="")
                print("\n")
                print("Editions")
                for i in editions:
                    print(i,", ",end="")
                print("\n")
                root.destroy()
            else:
                messagebox.showinfo('Response',"plz give correct information...!!")
        except:
            messagebox.showinfo('Response',"plz give correct information...!!")
    else:
         messagebox.showinfo('Response',"write anything...!!")  

#function for donatebook
def donate_book():
    global bookInfo2
    global bookInfo3
    global bookInfo4
    global root
    root = tkinter.Tk()
    root.title("Library")
    root.geometry("1700x900")
    Canvas1 =tkinter.Canvas(root)
   
    Canvas1.config(bg="dark olive green")
    Canvas1.pack(expand=True,fill=tkinter.BOTH)
       
    headingFrame1 = tkinter.Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = tkinter.Label(headingFrame1, text="Donate Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = tkinter.Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
       
    # Title
    lb2 = tkinter.Label(labelFrame,text="BOOK NAME: ", bg='black', fg='white',font=('Courier',12))
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
       
    bookInfo2 =tkinter.Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
       
    # Book Author
    lb3 = tkinter.Label(labelFrame,text="AUTHOR NAME: ", bg='black', fg='white',font=('Courier',12))
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
       
    bookInfo3 =tkinter.Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
   
    lb4 = tkinter.Label(labelFrame,text="EDITION: ", bg='black', fg='white',font=('Courier',12))
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
       
    bookInfo4 =tkinter.Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)
       
    #Submit Button
    SubmitBtn = tkinter.Button(root,text="SUBMIT",bg='chocolate1', fg='black',font=("Courier", 13),command=db)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
   
    quitBtn = tkinter.Button(root,text="QUIT",bg='burlywood', fg='black',font=("Courier", 13),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
   
    root.mainloop()

#validation and operation for donate book
def db():
    global bookInfo2
    global bookInfo3
    global bookInfo4
    global root
    task_list=['c++','java','The Art of Computer Programming','Computer Networks',
               'Introduction to Database System','Starting out with python','Close to the Machine',
               'Fundamentals of Computer Algorithms','The Art of Unix Programming',
               'The Psychology of Computer Programming','The Best Software Writing I',
               'After the Software Wars','Free Software','Free Society','Patterns of Software',
               'Innovation Happens Elsewhere',"The Happy Prince","The Magic Shop","Rip Van Winkle","Moby-Dick",
               "Wuthering Heights","War and Peace","The Odyssey","Hamlet","Crime and Punishment",
               "Pride and Prejudice","Jannat ke pattey","Harry potter"]
   
    authors=["Bjarne","Brain","Donald","Behrouz","Christopher","Tony","Ellen Ullman","Ellis Horowitz",
             "Ellis Horowitz","Eric Raymond","Joel Spolsky","Keith Curtis","Richard","Richard","Richard Gabriel",
             "Richard P.G,Oscar Wilde","H.G. Wells","Washington-I","Herman Melville","Emily Brontë",
             "Tolstoy","Homer","William Shakespeare","Fyodor Dostoyevsky","Jane Austen","Nimra ahmed","J. K. Rowling"]
    editions=['2010','2015','2017','2020','2005','2009','2004','2008','2010','2011','2009','2010','2006','2016','2004','2017']
    if (bookInfo2.get() != "" and bookInfo3.get()!= "" and bookInfo4.get()!=""):
        try:
            if(bookInfo2.get().isalpha() and bookInfo3.get().isalpha() and bookInfo4.get().isdigit()):
                task_list.append(bookInfo2.get())
                authors.append(bookInfo3.get())
                editions.append(bookInfo4.get())
                messagebox.showinfo('Response',"Thanks for donation...!!")
                print("Books")
                for i in task_list:
                    print(i,", ",end="")
                print("\n")
                print("Authors")
                for i in authors:
                    print(i,", ",end="")
                print("\n")
                print("Editions")
                for i in editions:
                    print(i,", ",end="")
                print("\n")
                root.destroy()
            else:
                messagebox.showinfo('Response',"plz give correct information...!!")
        except:
            messagebox.showinfo('Response',"plz give correct information...!!")
    else:
         messagebox.showinfo('Response',"write anything...!!")  

#function of feedback
def feed():
    global text
    global ws
    ws =tkinter.Tk()
    ws.title('FeedBack')
    ws.geometry("1700x900")
    ws.config(bg='sea green')
    headingFrame1 =tkinter.Frame(ws,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.2)
    headingLabel =tkinter.Label(headingFrame1, text="ANY SUGGESTION/\nCOMMENTS", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    text = tkinter.Text(ws,height=15,width=60)
    text.place(x=430, y=250)
    SubmitBtn =tkinter. Button(ws,text="SUBMIT",bg='chocolate1', fg='black',command=send)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)
   
    quitBtn = tkinter.Button(ws,text="QUIT",bg='burlywood', fg='black', command=ws.destroy)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)
    ws.mainloop()

#validation and operation of feedback
def send():
    global text
    global ws
    try:
        if (text.get()==""):
            messagebox.showinfo('Response',"write anything...!!")
    except:
        messagebox.showinfo('Response',"Thanks for your feed back...")
        ws.destroy()
reg()