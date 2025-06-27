from tkinter import *
from tkinter import messagebox, filedialog
import customtkinter as ctk
from winotify import Notification, audio
import os

class DelEverythingUI:
    def __init__(self, width, height, title, iconico, theme, colour):
        ctk.set_appearance_mode(theme)
        ctk.set_default_color_theme(colour)
        
        self.app = ctk.CTk()
        self.app.geometry(str(width)+"x"+str(height))
        self.app.title(title)
        self.app.iconbitmap(bitmap=iconico)
        
    
    def DelLabel(self, content, x, y, font):
        Lab = ctk.CTkLabel(self.app, text=content, font=font)
        Lab.pack(padx=x, pady=y)
        
        return Lab
    
    def DelEntry(self, x, y, font, placeholder):
        Ent = ctk.CTkEntry(self.app, placeholder_text=placeholder, font=font)
        Ent.pack(padx=x, pady=y)
        
        return Ent
    
    def DelButton(self, x, y, text, conerRadius, font, command):
        But = ctk.CTkButton(self.app, text=text, corner_radius=conerRadius, font=font, command=command)
        But.pack(padx=x, pady=y)
        
        return But
    
    def DelComboMenu(self, x, y, font, value):
        comboBox = ctk.CTkComboBox(self.app, values=value, font=font)
        comboBox.pack(padx=x, pady=y)
        
        return comboBox
    
    def DelFrame(self, width, height, x, y):
        frame = ctk.CTkFrame(self.app, width=width, height=height)
        frame.pack(padx=x, pady=y)
        
        return frame
    
    def DelGetInput(EntVar):
        Entered = EntVar.get()
        
        return Entered
    
    def DelDeleteElement(self, var):
        self.app.forget(var)
    
    def DelPlainMessageBox(Theme, title, msg):
        match Theme:
            case "info":
                messagebox.showinfo(title, msg)
            case "error":
                messagebox.showerror(title, msg)
            case "warn":
                messagebox.showwarning(title, msg)
    
    def DelChoiceMessageBox(Theme, title, msg):
        Data = 1
        match Theme:
            case "yesno":
                Data = messagebox.askyesno(title, msg)
            case "yesnocancel":
                Data = messagebox.askyesnocancel(title, msg)
            case "question":
                Data = messagebox.askquestion(title, msg)
            case "okcancel":
                Data = messagebox.askokcancel(title, msg)
            case "abortretrycancel":
                Data = messagebox.askretrycancel(title, msg)
        
        return Data
    
    def DelFileDialog(Action, filestypes, startdir):
        Data = None
        if startdir == None:
            startdir = os.getcwd()
        
        match Action:
            case "OpenFile":
                Data = filedialog.askopenfile(initialdir=startdir, filetypes=filestypes)
            case "OpenFiles":
                Data = filedialog.askopenfiles(initialdir=startdir, filetypes=filestypes)
            case "OpenFilename":
                Data = filedialog.askopenfilename(initialdir=startdir, filetypes=filestypes)
            case "OpenFilenames":
                Data = filedialog.askopenfilenames(initialdir=startdir, filetypes=filestypes)
            case "Folder":
                Data = filedialog.askdirectory(initialdir=startdir)
            case "SaveAsFile":
                Data = filedialog.asksaveasfile(initialdir=startdir, filetypes=filestypes)
            case "SaveAsFilename":
                Data = filedialog.asksaveasfilename(initialdir=startdir, filetypes=filestypes)
        
        return Data 
    
    def Notify(appId, title, msg, icon, duration, sound, loop, button, url):
        StartNotif = None
        
        if button == None:
            StartNotif = Notification(
                app_id=appId, 
                title=title, 
                msg=msg, 
                icon=icon, 
                duration=duration
            )
        else:
            StartNotif = Notification(
                app_id=appId, 
                title=title, 
                msg=msg, 
                icon=icon, 
                duration=duration,
                label=button,
                launch=url
            )
        
        match sound:
            case "SMS":
                StartNotif.audio(audio.SMS, loop=loop)
            case "LoopingAlarm":
                StartNotif.audio(audio.LoopingAlarm, loop=loop)
            case "LoopingCall":
                StartNotif.audio(audio.LoopingCall, loop=loop)
            case None:
                pass
        
        StartNotif.show()
    
    class DelCanvas:
        def __init__(self, area, width, height):
            self.canva = ctk.CTkCanvas(area, width, height)
            self.canva.pack(fill="both", expand=True)
        
        def DelCanvasText(self, x, y, font, text, fill):
            self.canva.create_text(x, y, text=text, font=font, fill=fill)
        
        def DelCanvasImage(self, x, y, image, anchor):
            self.canva.create_image(x, y, image=image, anchor=anchor)
    
    def DelAfter(self, TimeMilliseconds, commandAfter):
        self.app.after(TimeMilliseconds, commandAfter)
        
    def DelAppRunner(self):
        self.app.mainloop()
    
    def DelQuitApp(self):
        self.app.quit()
    
    def DelDestroyApp(self):
        self.app.destroy()