"""import time


from plyer import notification



if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink water",
            message="Pani peele na bhaya please",
  

            timeout=5

        )

        time.sleep(60*60)"""


from tkinter import *
from tkinter.ttk import *


# import tkinter module 
from tkinter import *   
  
# create a tkinter window
master = Tk()  
  
# Open window having dimension 200x100
master.geometry('600x600')  
    
# Create a Button
button = Button(master, 
                text = 'Submit', 
                bg='white', 
                activebackground='blue').pack()  

button2=Button(master,
text='exit',
bg='yellow',
activebackground='white'
).pack()
    

master.mainloop() 




    


 