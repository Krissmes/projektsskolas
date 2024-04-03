def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # r - read; w - write (izdzēš iepriekšēju, pārraksta pāri); a - append (pievieno klāt)
    fails.write(teksts+"\n")
    fails.close()
    return

ierakstit("hello")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close
    return
pierakstit_klat("sveiki")

def nolaist_visu():
    fails = open("teksts.txt","r", encoding="utf-8")
    teksts = fails.read()
    return teksts

print (nolaist_visu())

def dabut_rindinas():
    fails = open("teksts.txt","r", encoding="utf-8")
    rindas = fails.readlines()
    for i in range(len(rindas)):
        rindas[i] = rindas[1].strip()

    return rindas




saraksts = dabut_rindinas()
print(saraksts)