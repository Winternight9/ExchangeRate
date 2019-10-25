import socket
import time
import datetime 


def exchange(money):
    value = float(money[0])
    currency = money[1]
    listcurrency = []
    if currency == 'Baht':
        a = float(value*0.03312) 
        b = f"{a:.2f} US$"
        listcurrency.append(b)
        a = float(value*0.02978)
        b = f"{a:.2f} Euro"
        listcurrency.append(b)
        a = float(value*3.59728)
        b = f"{a:.2f} Yen"
        listcurrency.append(b)
    elif currency == 'US$':
        a = float(value*30.1875) 
        b = f"{a:.2f} Baht"
        listcurrency.append(b)
        a = float(value*0.89912)
        b = f"{a:.2f} Euro"
        listcurrency.append(b)
        a = float(value*108.596)
        b = f"{a:.2f} Yen"
        listcurrency.append(b)   
    elif currency == 'Euro':
        a = float(value*1.11220) 
        b = f"{a:.2f} US$"
        listcurrency.append(b)
        a = float(value*33.5762)
        b = f"{a:.2f} Baht"
        listcurrency.append(b)
        a = float(value*120.780)
        b = f"{a:.2f} Yen"
        listcurrency.append(b)    
    elif currency == 'Yen':
        a = float(value*0.00921) 
        b = f"{a:.2f} US$"
        listcurrency.append(b)
        a = float(value*0.00828)
        b = f"{a:.2f} Euro"
        listcurrency.append(b)
        a = float(value*0.27801)
        b = f"{a:.2f} Baht"
        listcurrency.append(b)             

    return listcurrency[0],listcurrency[1],listcurrency[2]


date_time = datetime.datetime.now()
date = (date_time.strftime("%d %b %Y, %I:%M %p"))

s = socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)
s.bind(('192.168.1.106',10001))
s.listen(1)

sock,info = s.accept()
msg=sock.recv(1024)

value = msg.decode().split(" ")
other1,other2,other3 = exchange(value)

sock.send(bytes(str.encode(f"{date} \n{value[0]} {value[1]} = {other1}\n         = {other2} \n         = {other3}")))

time.sleep(0.3)
