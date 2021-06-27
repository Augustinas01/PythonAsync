
import threading
import time
import fankcija

global csgoroll, csgoempire, fankcija, labelis, selfis

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        labelis = getwrds()
        #fankcija.start(csgoroll, csgoempire, self.counter)
        labelis.after(5000, update(selfis,labelis))


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print
        "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

def setup(y, x):
    global labelis, selfis
    labelis = x
    selfis = y
    #csgoempire = y
    #fankcija = f
def getwrds():
    return labelis

def update(selfis, labelis):
        """ update the label every 1 second """

        labelis.configure(text="5")

        # schedule another timer
        labelis.after(1000, update(selfis, labelis))

# Create new threads
thread1 = myThread(2, "Thread-2", 2)


# Start new Threads
#thread1.start()
#thread2.start()

