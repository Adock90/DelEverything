import DelEverythingLib
from DelEverythingUI import *
import sys
import time

noAdmin = ""

try: 
    noAdmin = sys.argv[1]
except:
    print("[DelEverything] No arguments supplied")

print("[DelEverything] Initializing")
print("[DelEverything] Checking Compatible OS")
appChecker = DelEverythingLib.DelEverythingUserConfig.OperatingSystem()
DelEverythingLib.DelEverythingUserConfig.OperatingSystem.GetOperatingSystem(appChecker)
CheckOS = DelEverythingLib.DelEverythingUserConfig.OperatingSystem.CheckIfOperatingSystemIsCompatible(appChecker, "Windows")

if noAdmin != "--no-admin":
    CheckAdmin = DelEverythingLib.DelEverythingUserConfig.OperatingSystem.WindowsManagement.detectAdmin()
else:
    print("[DelEverything] No Admin mode")



class App:
    print("[DelEverything] App Class Started")
    print("[DelEverything] App Class __init__ initalizing")
    def __init__(self):
        self.ScanDir = "C:\\Users\\Adam\\Documents\\DELEverything"
        print("[DelEverything] App Class __init__ Started")
        self.app = DelEverythingUI(700, 500, "DelEverything", "../Media/DelEverythingLogo.ico", "system", "blue")
        if CheckOS == False:
            self.app.DelPlainMessageBox("error", "Incompatible OS", "Your OS Does Not Meet the requirements")
            print("[DelEverything] Quitting. Bye")
            sys.exit(1)
        if os.path.exists("..\\Settings\\Settings.csv") == False:
            print("[DelEverything] No Settings")
            self.app.DelNotify("DelEverything", "Setup Settings", "You don't have any 'Settings\\Setttings.csv' file. Please Click Continue->Scan Options and click 'Submit Settings'", "short", "SMS", False, None, None)
        #self.XButtonBinder = self.app.DelWinManagerAttributes("WM_DELETE_WINDOW", self.Close(False))
        self.WelcomeTitle = self.app.DelLabel("Welcome to \n DelEverything Malware Scanner", 200, 50, ("Arial", 25, "bold"))
        
        self.PageOneContinue = self.app.DelButton(0, 100, "Continue", 100, ("Arial", 10), lambda: self.OptionsPage())
        
        
        
        self.close = self.app.DelButton(0, 0, "Close", 100, ("Arial", 10), lambda: self.Close(True))
        self.close.anchor(SE)
        
        self.app.DelAppRunner()
    
    def VTWriteUp(self, key):
        if key == None or key == "":
            print("[DelEverything] No Key Provied")
            self.app.DelPlainMessageBox("error", "Failed Virustotal", "No Key Provided")
        else:   
            print("[DelEverything] Generating Encryption Key")
            PassKeyGener = DelEverythingLib.DelEverythingUserConfig.VirusTotalAPIKeyManagement.GenerateKey()
            print("[DelEverything] Encrytption of Key")
            DelEverythingLib.DelEverythingUserConfig.VirusTotalAPIKeyManagement.SaveKey(key, PassKeyGener)
            self.app.DelNotify("DelEverything", "Key Saved", "Your VirusTotal API key has been Saved securely", "short", "SMS", False, "Show", "https://www.virustotal.com/gui/home/upload")
            self.app.DelPlainMessageBox("info", "Key Saved", "Your VirusTotal API key has been Saved securely")
        self.VTAPIKeyBut.pack_forget()
        self.VTAPIKeyEnt.pack_forget()
        self.OptionsPage()
    
    def WriteSettings(self, dataOne, dataTwo):
        UserSetObj = DelEverythingLib.DelEverythingUserConfig.UserSettingsStore()
        UserSetObj.CheckFile()
        UserSetObj.WriteValue(dataOne, dataTwo)
        self.ProcessesScanSwitch.forget()
        self.VirusTotalScan.forget()
        self.SubmitSettings.forget()
        self.OptionsPage()
        
    def Close(self, ShouldIQuit):
        if ShouldIQuit == True:
            self.CloseChoice = messagebox.askyesno("Are you Sure?", "Are you sure you want to quit")
            if self.CloseChoice == True:
                print("[DelEverything] App Window Class Killing")
                self.app.DelDestroyApp()
                print("[DelEverything] Window Destroyed Exiting")
                sys.exit(0)
            else:
                pass
        else:
            self.app.DelDestroyApp()
            
    def VirusTotal(self):
        self.VirusTotalBut.pack_forget()
        self.ScanOptions.pack_forget()
        self.StartScan.forget()
        
        self.VTAPIKeyEnt = self.app.DelEntry(0, 100, ("Arial", 20), 350, 30, "VirusTotal API Key", show="*")
        self.VTAPIKeyBut = self.app.DelButton(100, 100, "Submit", 100, ("Arial", 10), lambda: self.VTWriteUp(self.app.DelGetInput(self.VTAPIKeyEnt)))
    
    def ScanSettings(self):
        self.VirusTotalBut.pack_forget()
        self.ScanOptions.pack_forget()
        self.StartScan.forget()
        
        self.ProcessesScanVar = self.app.DelVar("Str", "on")
        self.VirusTotalScanVar = self.app.DelVar("Str", "off")
        
        self.ProcessesScanSwitch = self.app.DelSwitch(100, 100, "Scan Processes", self.ProcessesScanVar)
        self.VirusTotalScan = self.app.DelSwitch(100, 0, "Use VirusTotal", self.VirusTotalScanVar)
        
        self.SubmitSettings = self.app.DelButton(100, 50, "Submit Settings", 5, ("Arial", 10), lambda: self.WriteSettings(self.VirusTotalScanVar.get(), self.ProcessesScanVar.get()))
    
    def Scanning(self, full, JustProc=False):
        CountFile = 0
        self.FullScanBut.forget()
        self.QuickScanBut.forget()
        self.ProcScan.forget()
        
        TotalClean = True
        Stop = False
        
        if full == True:
            self.ScanDir = "C:\\"
        elif JustProc:
            pass
        else:
            self.ScanDir = DelEverythingUI.DelFileDialog("Folder")
        
        CheckProc = DelEverythingLib.CheckProcesses()
        
        if JustProc:
            input("")
            sys.exit(1)
        
        for (filenames, dirnames, dirpath) in os.walk(self.ScanDir):
            new = os.chdir(filenames)
            if Stop:
                break
            for file in os.listdir(new):
                CountFile += 1
                print(f"[{CountFile}] {os.getcwd()}\\{file}")
                Score = DelEverythingLib.CheckFile(f"{os.getcwd()}\\{file}", False, None)
                if Score < 5:
                    print("Clean")
                elif Score == -4632846238462374:
                    Stop = True
                    break
                else:
                    TotalClean = False
                    print("Dirty")
                    try:
                        os.remove(f"{os.getcwd()}\\{file}")
                    except:
                        try:
                            subprocess.run(["powershell", "-command", "rm "+os.getcwd()+"\"+file])
                        except:
                            print(f"Failed to delete {os.getcwd()}\\{file}")
        if TotalClean == False:
            ChoiceToReboot = DelEverythingUI.DelChoiceMessageBox("yesno", "Detections", "As we detected threats, In order to ensure all of the system memory is clean.\nWe need to reboot. Do you want to reboot now.")
            if ChoiceToReboot == True:
                subprocess.run(["shutdown.exe", "/r", "/c", "'DelEverything is rebooting your PC'", "/t", "15"])
            
        print(f"[DelEverything] Scanned {CountFile} files")
        input("")
        sys.exit(0)
            
    def BackPageMain(self, ElementObjArray):
        for i in range(len(ElementObjArray)):
            ElementObjArray[i].forget()

        self.OptionsPage()
    
    def StartScanPage(self):
        self.VirusTotalBut.forget()
        self.ScanOptions.forget()
        self.StartScan.forget()
        
        self.FullScanBut = self.app.DelButton(0, 10, "Full Scan(Recommended)", 5, ("Arial", 10), lambda: self.Scanning(True))
        self.QuickScanBut = self.app.DelButton(0, 11, "Quick Scan", 5, ("Arial", 10), lambda: self.Scanning(False))
        self.ProcScan = self.app.DelButton(0, 12, "Just Processes", 5, ("Arial", 10), lambda: self.Scanning(False, True))
        self.BackButton = self.app.DelButton(0, 13, "Back", 5, ("Arial", 15), lambda: self.BackPageMain([self.FullScanBut, self.QuickScanBut, self.BackButton, self.ProcScan]))
    
    def OptionsPage(self):
        self.PageOneContinue.pack_forget()
        self.WelcomeTitle.pack_forget()
        
        self.VirusTotalBut = self.app.DelButton(0, 11, "VirusTotal", 100, ("Arial", 10), lambda: self.VirusTotal())
        self.ScanOptions = self.app.DelButton(0, 12, "Scan Options", 100, ("Arial", 10), lambda: self.ScanSettings())
        self.StartScan = self.app.DelButton(0, 13, "Start Scan", 100, ("Arial", 10), self.StartScanPage)
        
    
if __name__ == "__main__":
    print("[DelEverything] Starting App Class")
    app = App()
    print("[DelEverything] Quitting")