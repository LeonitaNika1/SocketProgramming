import socket
host = 'localhost'
serverPort = 13000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("****************************************** UDP **********************************************************")
print("*                              Kërkesat që mund të plotësohën :                                         *")
print("* IPADDRESS | PORT | COUNT | REVERSE | PALINDROME | TIME | GAME | GCF | CONVERT | LETTERS | PERQINDJA    *")
print("*********************************************************************************************************")
print("")
adresa=(host, serverPort)
while True:
    kerkesa = input("Ju lutem shkruani njerën nga kërkesat :")
    kerkesa = kerkesa.upper()
    if len(kerkesa) > 128:
        print("Kerkesa nuk mund te jete me e gjate se 128 karaktere!")
        continue
    if kerkesa == '':
        print("Komanda është jo valide.Ju lutem shenoni nje kerkese!")
        continue
    elif kerkesa == "0":
        print("Lidhja juaj me severin u shkëput .Kalofshi një ditë të mirë !")
        serverSocket.close()
        break
    serverSocket.sendto(str.encode(kerkesa), (host, serverPort))
    try:
        pergjigja,adresa= serverSocket.recvfrom(2048)
        print(pergjigja.decode("utf-8"))
    except Exception:
        print("serveri nuk eshte gjetur")
