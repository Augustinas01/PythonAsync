from tkinter import *
import webbrowser
import fankcija,threading, time
import multiprocessing

queue2 = multiprocessing.Queue()
csgoroll, csgoempire = "",""
bilietas2 = 0
bilietai3 = 0
pracesai = []

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Csgoroll', cursor="hand2", bg="#a6aea9")
        self.lbl2=Label(win, text='Csgoempire', cursor="hand2", bg="#a6aea9")
        self.sv = StringVar()
        self.sv.set("0 Bilieteliu")
        self.lbl3=Label(win, textvariable=self.sv, bg="#a6aea9")
        self.lbl3.place(x=10, y=95)
        self.sv2 = StringVar()
        self.sv2.set("0 /s")
        self.lbl4 = Label(win, textvariable=self.sv2, bg="#a6aea9")
        self.lbl4.place(x=10, y=115)
        self.t1=Entry(width=65, bg="#636865")
        self.t2=Entry(width=65, bg="#636865")
        #self.t3=Entry(width=65, bd=5)
        #self.t4 = Entry(width=65, bd=5)
        #self.btn1 = Button(win, text='Add')
        #self.btn2 = Button(win, text='Subtract')
        self.lbl1.place(x=195, y=10)
        self.t1.place(x=13, y=30)
        self.lbl2.place(x=185, y=50)
        self.t2.place(x=13, y=70)
        self.b1=Button(win, text='Le go', command=self.add, width=6, height=2, bg="#77dd88")
        self.b2=Button(win, text='La stop', command=self.stop, width=6, height=2, bg="#ff4566")
        self.b1.place(x=294, y=95)
        self.b2.place(x=354, y=95)
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
        self.change_value_callback()
    def sub(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
    def stop(self):
        #print("Stoperinio")
        stop()

    def change_value_callback(self):
        th = threading.Thread(target=self.change_value, args=())
        th.start()

    def change_value(self):
        global bilietas2, bilietai3
        time.sleep(0.5)
        while True:
            time.sleep(1)
            while queue2.qsize()>0:
                try:
                    bilietas = int(queue2.get(False))
                except:
                    continue
                bilietai3 += bilietas
            bilietas2 += bilietai3
            self.sv.set("{:,} Bilieteliu".format(bilietas2))
            self.sv2.set("{:,}/s ".format( bilietai3))
            bilietai3 = 0













def start(csgoroll, csgoempire):
    #global queue, queue2

    #queue = multiprocessing.Queue()
    #queue2 = multiprocessing.Queue()
    trol = 3
    #labelis.configure(text="%.2f" % trol)
    #labelis.after(5000, labelis.configure(text="%.2f" % trol))
    #print(multiprocessing.cpu_count())
    x=0

    queue2.put(0)
    for i in range(int(multiprocessing.cpu_count()*0.75)):
        p = multiprocessing.Process(target=fankcija.start, args=(csgoroll,csgoempire,queue2))
        #p.daemon = True
        p.start()
        pracesai.append(p)
        #time.sleep(0.000000000000000001)
        #jobs.append(p)
        #print(queue2.get())
        #p.start()
        #p.join()
        #print(p)


def stop():
    print("Stoperinio pradeda veikt ({})".format(len(pracesai)))
    for i in range(len(pracesai)):
        print("Stabdom {} procesa".format(i))
        pracesai.pop(0).terminate()




if __name__ == '__main__':
    multiprocessing.freeze_support()
    #start("as","sad")
    #print("lol")
    window = Tk()
    #window.overrideredirect(True)
    mywin = MyWindow(window)
    window.resizable(0,0)
    window.title('Hello Wealth')
    #window.iconbitmap("icon.ico")
    window.geometry("420x140+10+10")
    window.configure(bg="#a6aea9")
    window.mainloop()
