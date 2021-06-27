import multiprocessing, random, string
import fankcija, time


def main(csgoroll, csgoempire):
    queue = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    print(multiprocessing.cpu_count())
    x = 0
    queue.put(False)
    queue2.put(0)
    for i in range((multiprocessing.cpu_count())):
        p = multiprocessing.Process(target=fankcija.start, args=(csgoroll, csgoempire, queue, queue2))
        # p.daemon = True
        p.start()
        # time.sleep(0.000000000000000001)
        # jobs.append(p)
        # print(queue2.get())
        queue.put(False)
        if queue.get():
            print("tlol")
            break
        queue.put(False)
        # p.start()
        # p.join()
        print(p)


if __name__ == '__main__':
    main()
