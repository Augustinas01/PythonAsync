import random, hashlib

# start_time = time.time()
ltrs = "a06b17c28d39e4f5"


# csgoroll = "d72742438a6e6a294add67905c693e139f5cf9cf86ee5f45d5678ed4b09af547"
# csgoempire = "94c8ec9e17655f93f68f3fdc225ac278efc21406956b92ff8850830ddf029bc8"

def randomword(length):
    letters = ltrs
    return ''.join(random.choice(letters) for i in range(length))


def uzkoduoti(nekodas):
    return hashlib.sha256(nekodas.encode('utf-8')).hexdigest()


def patikra(manokodas, rollkodas):
    return manokodas == rollkodas


def fankcija(csgoroll, csgoempire):
    # wrd = "b17ba24cd22fda96c2847fbcf3d66dc0507a44e62ae2b2028e7b1be3d877a141"
    wrd = randomword(64)
    # f.write("{}\n".format(wrd))
    kwrd = uzkoduoti(wrd)
    # kwrd = "randomword(64)"
    # fa.write("{}\n".format(kwrd))
    # print(wrd)

    if kwrd == csgoroll:
        f = open("OpaPaejo.txt", "a")
        f.write("csgoroll: {} - {} \n".format(wrd, csgoroll))
        f.close()
        print("CSGOROLL: {}-{}".format(wrd, kwrd))
        setWrds(wrd, kwrd)
        return wrd, kwrd
    if kwrd == csgoempire:
        f = open("OpaPaejo.txt", "a")
        f.write("csgoempire: {} - {} \n".format(wrd, csgoempire))
        f.close()
        print("CSGOEMPIRE: {}-{}".format(wrd, kwrd))
        setWrds(wrd, kwrd)
        return wrd, kwrd

    return False, False


def start(csgoroll, csgoempire, y):
    # f = open("nekoduota4.txt", "a")
    # fa = open("koduota4.txt", "a")
    i = 0
    while True:
        # x.put(False)
        wrd, kwrd = fankcija(csgoroll, csgoempire)
        i += 1
        # print("Vaziuoja")
        if wrd != kwrd:
            return wrd, kwrd
        if i == 9999:
            y.put(i, False)
            i = 0

    # f.close()
    # fa.close()


def setWrds(x, y):
    global prizas, siurprizas
    prizas, siurprizas = x, y


def getWrds():
    return prizas, siurprizas

# start()
# print ("My program took", time.time() - start_time, "to run")
