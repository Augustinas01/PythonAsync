from tkinter import *
import webbrowser
import fankcija
import multiprocessing
import pools


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Csgoroll', cursor="hand2")
        self.lbl2=Label(win, text='Csgoempire', cursor="hand2")
        #self.lbl3=Label(win, text='Viena diena ;)')
        self.t1=Entry(width=65, bd=3)
        self.t2=Entry(width=65, bd=3)
        #self.t3=Entry(width=65, bd=5)
        #self.t4 = Entry(width=65, bd=5)
        #self.btn1 = Button(win, text='Add')
        #self.btn2 = Button(win, text='Subtract')
        self.lbl1.place(x=9, y=10)
        self.t1.place(x=10, y=35)
        self.lbl2.place(x=9, y=65)
        self.t2.place(x=10, y=90)
        self.b1=Button(win, text='Le go', command=self.add, width=8, height=4)
        #self.b2=Button(win, text='Subtract', command=self.stop)
        self.b1.place(x=420, y=39)
        #self.b2.place(x=200, y=150)
        #self.lbl3.place(x=9, y=120)
        #self.t3.place(x=10, y=145)
        #self.t4.place(x=10, y=175)
        #self.lbl1.pack()
        self.lbl1.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.csgoroll.com/en/roll/history"))
        self.lbl2.bind("<Button-1>", lambda e: webbrowser.open_new("https://csgoempire.com/fairness"))


    def add(self):
        #self.t3.delete(0, 'end')
        csgoroll=str(self.t1.get())
        csgoempire=str(self.t2.get())
        start(csgoroll,csgoempire)
    def sub(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
    def stop(self):
        fankcija.btn = 1




def start(csgoroll, csgoempire):

    queue = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    print(multiprocessing.cpu_count())
    x=0
    queue.put(False)
    queue2.put(0)
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=fankcija.start, args=(csgoroll,csgoempire,queue,queue2))
        #p.daemon = True
        p.start()
        #time.sleep(0.000000000000000001)
        #jobs.append(p)
        #print(queue2.get())
        queue.put(False)
        if queue.get():
            print("tlol")
            break
        queue.put(False)
        #p.start()
        #p.join()
        print(p)



if __name__ == '__main__':
    multiprocessing.freeze_support()
    #start("as","sad")
    #print("lol")
    window = Tk()
    mywin = MyWindow(window)
    window.title('Hello Wealth')
    window.geometry("500x120+10+10")
    window.mainloop()
