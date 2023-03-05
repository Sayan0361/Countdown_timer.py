''' Python Minor Project '''

''' Create a CountDown Timer using Python 
   Features to include reset, stop , resume , pause '''


import datetime                         # to work with date and time    
import tkinter as tk                    # for GUI   
from tkinter import messagebox as msg   # for messagebox
import winsound as ws                   # for providing basic sound


class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self._timer_on=False
        self.pause=False


    ''' Showing Widgets'''
    '''The pack() function will basically organise the widgets in blocks before placing it in the parent widget '''
    def show_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()
        self.quit.pack()
        

    ''' Creating Widgets and adding buttons '''
    def create_widgets(self):
        self.label=tk.Label(self,text="ENTER THE TIME IN SECONDS :- ",font=("times new roman",16,"bold"),width=25,bg='CadetBlue1')
        self.entry=tk.Entry(self,justify="center")
        self.entry.focus_set()
        self.reset=tk.Button(self,text="RESET",command=self.reset_button,cursor="hand2",font=("times new roman",16,"bold"),width=8,bg='CadetBlue1')
        self.start=tk.Button(self,text="START",command=self.start_button,cursor="hand2",font=("times new roman",16,"bold"),width=8,bg='CadetBlue1')
        self.stop=tk.Button(self,text="STOP",command=self.stop_button,cursor="hand2",font=("times new roman",16,"bold"),width=8,bg='CadetBlue1')
        self.pause=tk.Button(self,text="PAUSE",command=self.pause_button,cursor="hand2",font=("times new roman",16,"bold"),width=8,bg='CadetBlue1')
        self.resume=tk.Button(self,text="RESUME",command=self.resume_button,cursor="hand2",font=("times new roman",16,"bold"),width=8,bg='CadetBlue1')
        self.quit=tk.Button(self,text="QUIT",command=self.quit_button,cursor="hand2",font=("times new roman",16,"bold"),width=8,bg='CadetBlue1')
        

    ''' The main Countdown function '''
    def countdown(self):
        self.label["text"]=self. convert_seconds_left_to_time()
        if self.seconds_left:    
            self.seconds_left=self.seconds_left-1
            self._timer_on=self.after(1000,self.countdown)
        else:
            self._timer_on=False
            ws.MessageBeep()
            msg.showinfo("Time Countdown", " TIME'S UP ")


    '''Reset Button function'''
    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.label["text"]="ENTER THE TIME IN SECONDS : - "
        self.stop.forget()
        self.reset.forget()
        self.pause.forget()
        self.resume.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()


    '''Stop Button function'''
    def stop_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()


    '''Start Button function'''
    def start_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.quit.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.quit.pack()


    '''Stop timer function'''
    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on=False

    
    '''Pause Button function'''
    def pause_button(self):
        self.pause=True
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on=False
        

    '''Resume Button function'''
    def resume_button(self):
        self.pause=False
        if self._timer_on==False:
            self._timer_on=True
        self.countdown()


    def  convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)


    '''Quit Button function'''
    def quit_button(self):
        if tk.messagebox.askokcancel("QUIT", " WOULD YOU LIKE TO QUIT ? "):
            root.destroy()


if __name__=="__main__":
    root=tk.Tk()  # root is the name of the main window 
    root.resizable(width=False,height=False)  # cancelling the option of resizable
    root.geometry("580x420")   # setting the geometry
    root.title("COUNTDOWN TIMER") # title of the main window
    root.config(bg ='dark turquoise') # adding bg colour
    countdown=Countdown(root) 
    countdown.pack()
    root.mainloop() # to run the appplication and process the event
    
    
    

