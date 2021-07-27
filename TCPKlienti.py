import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ndr= input("Deshironi ta nderroni portin dhe ip adresen (nese po
shtypni PO): ")
ndr = ndr.upper()
def change():
 try:
 j = input("Caktoni portin :")
 serverPort = int(j)
 host = input("Caktoni ipaddresen :")
 serverSocket.connect((host, serverPort))
 except:
 print("Nuk mund te lidheni provoni perseri")
 return change()
if(ndr=='PO'):
 change()
else:
 host = 'localhost'
 serverPort = 13000
 serverSocket.connect((host, serverPort))
print("****************************************** TCP
*********************************************************")
print("* Kërkesat që mund të plotësohën :
*")
print("* IPADDRESS | PORT | COUNT | REVERSE | PALINDROME | TIME | GAME
| GCF | CONVERT | LETTERS | PERQINDJA *")
print("***************************************************************
******************************************")
print("")
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
 print("Lidhja juaj me severin u shkëput .Kalofshi një ditë të
mirë !")
 serverSocket.close()
 break
 else:
 serverSocket.sendall(str.encode(kerkesa))
 serverAnswerByte = serverSocket.recv(2048)
 serverAnswer = serverAnswerByte.decode("utf-8")
 print(serverAnswer)
 print("Vazhdoni me kerkese tjeter ose shtyp 0 per dalje.")
 print('')
