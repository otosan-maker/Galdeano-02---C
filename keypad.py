from machine import Pin
import time


strLastKey="Inicio"

#define F1 25
#define F2 26
#define F3 27
#define F4 14
#define F5 12
#define F6 13
#define C1 34
#define C2 35
#define C3 32
#define C4 33
#define C5 22
#define C6 39
#define C7 36

F1 = Pin(25, Pin.OUT)
F2 = Pin(26, Pin.OUT)
F3 = Pin(27, Pin.OUT)
F4 = Pin(14, Pin.OUT)
F5 = Pin(12, Pin.OUT)
F6 = Pin(13, Pin.OUT)

F1.off()
F2.off()
F3.off()
F4.off()
F5.off()
F6.off()

C1 = Pin(34, Pin.IN, Pin.PULL_DOWN)
C2 = Pin(35, Pin.IN, Pin.PULL_DOWN)
C3 = Pin(32, Pin.IN, Pin.PULL_DOWN)
C4 = Pin(33, Pin.IN, Pin.PULL_DOWN)
C5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
C6 = Pin(39, Pin.IN, Pin.PULL_DOWN)
C7 = Pin(36, Pin.IN, Pin.PULL_DOWN)



Caracteres = [
    [["mode","left","x","7","4","1","0"],
     ["up","cnt","down","8","5","2","."],
     ["graph","rigth","y","9","6","3","="],
     ["sin()","log()","var","+","-","*","/"],
     ["cos()","^","cat","'",",","(","del"],
     ["tan()","^2","pi","e"," ",")","exe"]],
    [["mode","left","x","j","n","r","v"],
     ["up","cnt","down","k","o","s","."],
     ["graph","rigth","y","l","p","t","="],
     ["a","d","g","m","q","u","z"],
     ["b","e","h","'",",","(","del"],
     ["c","f","i","e"," ",")","exe"]],
    [["mode","left","X","J","N","R","V"],
     ["up","cnt","down","K","O","S","."],
     ["graph","rigth","Y","L","P","T","="],
     ["A","D","G","M","Q","U","Z"],
     ["B","E","H","'",",","(","del"],
     ["C","F","I","e"," ",")","exe"]]]


Columns = [ C1, C2, C3, C4, C5, C6 , C7]
Files = [ F1, F2, F3, F4, F5, F6]

def get_key(idMode):
    strValue=""
    global strLastKey
    global lastKeyPressed
    keyPressed=0
    for idFil,file in enumerate( Files):
        file.on()
        for idCol,col in enumerate(Columns):
            if col.value() == 1:
                strValue=Caracteres[idMode][idFil][idCol]
                keyPressed=time.ticks_ms()
                #print("tecla F:"+str(idFil)+" C:"+str(idCol))
        file.off()
    if ((strValue == strLastKey) and (lastKeyPressed-time.ticks_ms()<250)):
        return ""
    else:
        strLastKey=strValue
        lastKeyPressed=keyPressed
        return strValue
    

    