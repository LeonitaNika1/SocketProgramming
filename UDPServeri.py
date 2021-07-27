import socket
from datetime import datetime
import random
from collections import Counter
host = 'localhost'
serverPort = 13000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    serverSocket.bind((host, serverPort))
except socket.error as e:
    print("Nuk mund te lidheni")
print('Serveri eshte i gatshem te pranoj kerkesa')
try:

    def konvertimi(s, num):
        if s == "CMTOFEET":
            return num / 30.48
        elif s == "FEETTOCM":
            return num * 30.48
        elif s == "KMTOMILES":
            return num / 1.609344
        elif s == "MILESTOKM":
            return num * 1.609344

    def gcf(x, y):
        while y:
            x, y = y, x % y
        return x


    def rev(x):
        teksti = str.join(" ", x)
        reverse = teksti[::-1]
        return reverse


    def palindrom(x):
        teksti = str.join(" ", x)
        return teksti

    def kerkesaa(klienti, adresa):
        global reverse, teksti, pergjigjja
        klienti=klienti.decode('utf-8')
        klienti=klienti.split()
        if klienti[0] == 'IPADDRESS':
            pergjigjja = " IP Adresa e klientit është :" + adresa[0]
            if klienti[1:]:
                pergjigjja = "Shkruani kerkesen ne rregull ! "

        elif klienti[0] == 'PORT':
            pergjigjja = "Klienti është duke përdorur portin " + str(adresa[1])
            if klienti[1:]:
                pergjigjja = "Shkruani kerkesen ne rregull !"

        elif klienti[0] == 'COUNT':
            a = ""
            a = a.join(klienti[1:])
            zanore = 0
            bashketingellore = 0
            if len(a) != 0:
               for i in range(0, len(a)):
                  if a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"  or a[i] == "Y":
                        zanore = zanore + 1
                  else:
                        if a[i]>= 'A' and a[i]<= 'Z':
                             bashketingellore = bashketingellore + 1
               pergjigjja = "Teksti i pranuar përmban " + str(zanore) + " zanore  dhe "\
                             + str(bashketingellore) + " bashkëtingëllore "
            else:
                    pergjigjja = "JU lutem shenoni nje fjali pas kërkesës !"

        elif klienti[0] == "REVERSE":
            try:
                if klienti[1]:
                    pergjigjja = "Teksti i kthyer ne formen reverse është : " + str(rev(klienti[1:]))
            except Exception:
                pergjigjja = "Ju lutem shenoni nje fjali pas fjalës  " + str(klienti[0])

        elif klienti[0] == "PALINDROME":
            try:
                if klienti[1]:
                    teksti = palindrom(klienti[1:])
                    reverse = rev(klienti[1:])
                if teksti == reverse:
                    pergjigjja = "Teksti i dhënë eshte palindrome"
                else:
                    pergjigjja = "Teksti i dhënë nuk eshte palindrome"
            except Exception:
                pergjigjja = "Ju lutem shenoni nje tekst pas kërkesës " + klienti[0]

        elif klienti[0] == "LETTERS":
            try:
                if klienti[3:]:
                    pergjigjja = "Ju lutem shkruani kërkesën ne rregull duhet dhënë vetem dy fjale pas kërkesës."
                else:
                    teksti1 = klienti[1].lower()
                    teksti2 = klienti[2].lower()
                    shkronjatenjejta = Counter(teksti1) & Counter(teksti2)
                    shkronjatendryshme = Counter(teksti1) - Counter(teksti2)
                    a = sum(shkronjatenjejta.values())
                    b = sum(shkronjatendryshme.values())
                    pergjigjja = "Numri i shkronjave te njejta eshte [" + str(a) + "] dhe caktimi i tyre me " + \
                                 str(shkronjatenjejta) + "\nNumri i shkronjave te ndryshme eshte [" + str(
                        b) + "] dhe caktimi i tyre me " + str(shkronjatendryshme)
            except:
                pergjigjja = "Ju lutem shkruani kërkesën ne rregull duhet dhënë dy fjale pas kërkesës"

        elif klienti[0] == 'TIME':
            if klienti[1:]:
                pergjigjja = "Nuk keni nevoj te shkruani asgje pas kërkesës TIME! "
            else:
                koha = datetime.now().strftime('%d.%m.%Y %I:%M:%S:%p')
                pergjigjja = koha

        elif klienti[0] == 'GAME':
            if klienti[1:]:
                pergjigjja = "Game i merr rastesisht numrat nuk keni nevoj te shkruani asgje! "
            else:
                game = [random.randint(1, 35) for i in range(5)]
                game.sort()
                pergjigjja = "5 numra te rastesishem nga rangu 1-35: " + str(game)

        elif klienti[0] == 'GCF':
            try:
                num1 = int(klienti[1])
                num2 = int(klienti[2])
                ops = klienti[3:]
                if ops:
                    pergjigjja = "Nuk mund të shkruani me shumë se dy numra pas kërkesës"
                else:
                    num = gcf(num1, num2)
                    pergjigjja = "GCF : " + num
            except:
                pergjigjja = "Ju lutem shënoni dy numra të plote pas kërkesës GCF"

        elif klienti[0] == 'PERQINDJA':
            try:
                num1 = float(klienti[1])
                num2 = float(klienti[2])
                if klienti[3:]:
                    pergjigjja = "Nuk mund të shkruani me shumë se dy numra pas kërkesës"
                else:
                    num = num1 * num2
                    num3 = num / 100
                    num4 = "%.2f" % (num1 - num3)
                    pergjigjja = "Qmimi  ka qene " + str(num1) + " pas zbritjes  " + str(
                        num2) + "%" + " qmimi eshte bere " + str(num4)
            except:
                pergjigjja = "Ju lutem shënoni dy numra pas kërkesës "

        elif klienti[0] == 'CONVERT':
            try:
                opsioni = klienti[1]
                num1 = float(klienti[2].upper())
                if klienti[3:]:
                    pergjigjja = "Duhet ta shenoni vetem qka deshironi te konvertoni dhe numrin pas kerkeses! \n " 
                else:
                    num = "%.2f" % (konvertimi(opsioni, num1))
                    pergjigjja = num
            except:
                pergjigjja = "Ju lutem shenoni kerkesen ne rregull ,duhet shkuar njeren nga mundesite per konvertim dhe numrin pas kerkeses ! \n"
        else:
            pergjigjja = "Ju lutem shenoni njeren nga kërkesat!"
        return pergjigjja

except:
    print("Ju lutem shenoni ndonjeren nga kërkesat!")

while True:
        try:
                clientrequest, adresa = serverSocket.recvfrom(2048)
                k=kerkesaa(clientrequest,adresa)
                serverSocket.sendto(str.encode(k), adresa)
        except:
            serverSocket.sendto(str.encode("Nuk mund te lidheni"))
