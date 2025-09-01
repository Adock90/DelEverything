from tkinter import *
from tkinter import messagebox, filedialog
import customtkinter as ctk
from winotify import Notification, audio
import os
import webbrowser
import subprocess
import platform
import time

class DelURLHandle:
    def __init__(self, url):
        print("[DelEverything] Opening "+url+" in default browser")
        webbrowser.open(url)
        print("[DelEverything] Opened "+url+" in default browser")

class DelAppHandler:
    def __init__(self, exe, arg):
        print("[DelEverything] Opening "+exe+" with args "+arg)
        subprocess.Popen([exe, arg])
        print("[DelEverything] Opened "+exe+" with args "+arg)

class DelEverythingImageHandler:
    def __init__(self, imgPath):
        print("[DelEverything] Creating Image Object from Path: "+imgPath)
        self.imgObj = PhotoImage(imgPath)
        print("[DelEverything] Created Image Object from Path: "+imgPath)

    def DelResizeImageObjZoom(self, x, y):
        print("[DelEverything] Zooming Image Object")
        self.imgObj.zoom(x, y)
        print("[DelEverything] Zoomed Image Object")
        
    def DelGetImgObj(self):
        print("[DelEverything] Retrieving Image Object")
        return self.imgObj
        
class DelEverythingUI:
    def __init__(self, width, height, title, iconico, theme, colour):
        ctk.set_appearance_mode(theme)
        print("[DelEverything] Set Apperence Theme: "+theme)
        ctk.set_default_color_theme(colour)
        print("[DelEverything] Setting the default colour theme to: "+colour)
        
        if platform.platform().__contains__("Win"):
            time.sleep(1)
            os.system("cls")
        else:
            time.sleep(1)
            os.system("clear")
            
        self.app = ctk.CTk()
        print("[DelEverything] Initalizing CTK")
        self.app.geometry(str(width)+"x"+str(height))
        self.app.title(title)
        self.app.iconbitmap(bitmap=iconico)
        
        print("[DelEverything] geometry: "+str(width)+"x"+str(height))
        print("[DelEverything] title: "+title)
        print("[DelEverything] icon: "+iconico)
    
    def DelOverrideWinManager(self):
        self.app.overrideredirect(1)
    
    def DelWinManagerAttributes(self, attrib, colour):
        self.app.wm_attributes(attrib, colour)
    
    def DelAttributes(self, attrib, bool):
        self.app.attributes(attrib, bool)
    
    def DelBind(self, ActionStr, command):
        self.app.bind(ActionStr, command)
    
    def DelResizeable(self, Rez):
        self.app.resizable(Rez, Rez)
        
    def DelVar(self, Type, defVal):
        Data = None
        
        match Type:
            case "Int":
                Data = ctk.IntVar(value=defVal)
            case "Str":
                Data = ctk.StringVar(value=defVal)
        
        return Data
    
    def DelLabel(self, content, x, y, font, image=None):
        Lab = ctk.CTkLabel(self.app, text=content, font=font,image=image)
        Lab.pack(padx=0, pady=0)
        Lab.configure(padx=x, pady=y)
        
        return Lab
    
    def DelEntry(self, x, y, font, width, height, placeholder, show=None):
        Ent = ctk.CTkEntry(self.app, width=width, height=height, placeholder_text=placeholder, font=font, show=show)
        Ent.pack(padx=0, pady=0)
        Ent.pack(padx=x, pady=y)
        
        return Ent
    
    def DelButton(self, x, y, text, conerRadius, font, command):
        But = ctk.CTkButton(self.app, text=text, corner_radius=conerRadius, font=font, command=command, anchor="c")
        But.pack(padx=0, pady=0)
        But.pack(padx=x, pady=y)
        
        return But
    
    def DelSwitch(self, x, y, text, variable, command=None, onvalue="on", offvalue="off"):
        Switch = ctk.CTkSwitch(self.app, text=text, command=command, variable=variable, onvalue=onvalue, offvalue=offvalue)
        Switch.pack(padx=0, pady=0)
        Switch.pack(padx=x, pady=y)
        
        return Switch
    
    def DelComboMenu(self, x, y, font, value):
        comboBox = ctk.CTkComboBox(self.app, values=value, font=font)
        comboBox.pack(padx=x, pady=y)
        
        return comboBox
    
    def DelFrame(self, width, height, x, y):
        frame = ctk.CTkFrame(self.app, width=width, height=height)
        frame.pack(padx=x, pady=y)
        
        return frame
    
    def DelGetInput(self, EntVar):
        Entered = EntVar.get()
        if Entered == None or Entered == "":
            print("[DelEverything] Null String ")
            
        return Entered
    
    def DelDeleteElement(self, var):
        self.app.forget(var)
    
    def DelPlainMessageBox(self, Theme, title, msg):
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
    
    def DelFileDialog(Action, filestypes=(("All Types", "*.*")), startdir=os.getcwd()):
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
    
    def DelNotify(self, appId, title, msg, duration, sound, loop, button, url):
        StartNotif = None
        
        
        StartNotif = Notification(app_id=appId, title=title, msg=msg, duration=duration)
        
        if button != None:
            StartNotif.add_actions(label=button, launch=url)
        
        match sound:
            case "SMS":
                StartNotif.set_audio(audio.SMS, loop=loop)
            case "LoopingAlarm":
                StartNotif.set_audio(audio.LoopingAlarm, loop=loop)
            case "LoopingCall":
                StartNotif.set_audio(audio.LoopingCall, loop=loop)
            case None:
                pass
        
        StartNotif.show()
    
    def DelProgressBar(self, x, y, ori="horizontal", mode="determinate", width=29, height=10, startpoint=0, border_width=0, border_color=None, fg_colour=None, determinate_speed=1, indeterminate_speed=.5):
        Progressbar = ctk.CTkProgressBar(self.app, orientation=ori, mode=mode, width=width, height=height)
        Progressbar.pack(padx=x, pady=y)
        Progressbar.set(startpoint)
        
    
    def DelCanvas(self, width, height, bg, fill="both"):
        self.canva = Canvas(self.app, width=width, height=height, bg=bg)
        self.canva.pack(fill=fill, expand=True)
        
    def DelCanvasText(self, font, text, fill):
        self.canva.create_text(text=text, font=font, fill=fill)
        
    def DelCanvasImage(self, x, y, image, anchor, fill="both"):
        self.canva.create_image(x, y, image=image, anchor=anchor)
    
    def DelAfter(self, TimeSeconds, commandAfter):
        self.app.after(TimeSeconds*1000, commandAfter)
        
    def DelAppRunner(self):
        self.app.mainloop()
    
    def DelWindowProtocol(self, ActionStr, command):
        self.app.protocol(ActionStr, command)
    
    def DelQuitApp(self):
        self.app.quit()
    
    def DelDestroyApp(self):
        self.app.destroy()