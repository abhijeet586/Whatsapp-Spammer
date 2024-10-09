import time
import pyautogui as pg #To auto spam 
import pywhatkit #To send msg on whatsapp
F=1

for i in range(100):#Mention the amount of times the message has to be sent
    if F==1:
        pywhatkit.sendwhatmsg("+91XXXXXXXXXX","The Message you want to send",22,8)#Mention recievers number,the message,the time at which it should send the message
        F=F+1
        time.sleep(5)
    elif F==2:
        pg.write('The Message you want to send')
        pg.press('enter')
 
    



