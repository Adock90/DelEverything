from cryptography.fernet import Fernet
import hashlib
import base64
import os
import platform
import sys
import csv
import datetime

class OperatingSystem:
    def __init__(self):
        print("[DelEverything] OS Info")
    def GetOperatingSystem(self):
        self.OperatingSystem = platform.platform()
        self.OperatingSystemVersion = platform.release()
        print("[DelEverything] Detected OS: "+self.OperatingSystem)
        return self.OperatingSystem
    
    def CheckIfOperatingSystemIsCompatible(self, TargetOS):
        OS = self.GetOperatingSystem()
        if OS.__contains__(TargetOS):
            print("[DelEverything] Detected Compatible OS")
            return True
        else:
            print("[DelEverything] Detected Invalid OS")
            return False
        
    def GetOperatingSystemVersion(self):
        return self.GetOperatingSystemVersion

class VirusTotalAPIKeyManagement:
    def LoadKey(password=''):
        hashObj = hashlib.sha256()
        try:
            hashObj.update(password)
            hashObj.digest()
            hashObj.hexdigest()
        except:
            print("Hash Error")
        
        with open("../Keys/VTKey.key", "rb") as VTKey:
            content = VTKey.read()
            
            key = Fernet(hashObj)
            Decrypted = key.decrypt(content)
            
        
        return Decrypted
    
    def SaveKey(vapikey, password=''):
        if vapikey == None or vapikey == "" or password == "" or password == None:
            print("[DelEverything] Failed Null Input")
            sys.exit(1)
        strPassword = str(password)
        strPassword = strPassword.encode("utf-8")
        print("[DelEverything] Encoding password string")
        strKey = str(vapikey)
        strKey = strKey.encode("utf-8")
        print("[DelEverything] Encoding API Key")
        key = Fernet(password)
        print("[DelEverything] Key Generated")
        if os.path.exists("../Keys") == False:
            print("[DelEverything] Dir Checks Failed")
            print("[DelEverything] Fixing Dir")
            os.mkdir("../Keys")
            print("[DelEverything] Fixed")
        print("[DelEverything] Opening File")
        with open("../Keys/VTKey.key", "wb") as VTKey:
            print("[DelEverything] File Open")
            print("[DelEverything] Encrypting VT API Key")
            Encrypted = key.encrypt(strKey)
            print("[DelEverything] Key Encrypted Now Writing Bytes")
            VTKey.write(Encrypted)
            print("[DelEverything] Written Key Closing File")
            VTKey.close()
            print("[DelEverything] File Closed")
    
    def GenerateKey():
        if os.path.exists("../Keys") == False:
            print("[DelEverything] Dir Checks Failed")
            print("[DelEverything] Fixing Dir")
            os.mkdir("../Keys")
            print("[DelEverything] Fixed")
        Key = Fernet.generate_key()
        print("[DelEverything] Key Generated")
        print("[DelEverything] Opening File")
        with open("../Keys/EncryptoK.key", "wb") as EncryptKeyFileHandler:
            print("[DelEverything] File Open")
            print("[DelEverything] Writing Key Bytes")
            EncryptKeyFileHandler.write(Key)
            print("[DelEverything] Written Key Bytes")
            print("[DelEverything] Closing File")
            EncryptKeyFileHandler.close()
            print("[DelEverything] Closed File")
            
        return Key
        

class LogFile:
    def __init__(self, File):
        self.filename = File
    
    def ReadLogFile(self):
        with open(self.filename, "r") as ReadLogFile:
            contents = ReadLogFile.read()
            ReadLogFile.close()
        
        return contents
    
    def OverWriteLogFile(self, content):
        timeNow = datetime.datetime.now()
        timeNowFormatted = timeNow.strftime("%d/%m/%Y: %H:%M:%S.%f")
        with open(self.filename, "w") as WriteLogFile:
            WriteLogFile.write(timeNowFormatted+"->"+content+"\n")
            WriteLogFile.close()
        
    def AppendWriteLogFile(self, content):
        timeNow = datetime.datetime.now()
        timeNowFormatted = timeNow.strftime("%d/%m/%Y: %H:%M:%S.%f")
        with open(self.filename, "a") as WriteLogFile:
            WriteLogFile.write(timeNowFormatted+"->"+content+"\n")
            WriteLogFile.close()


class UserSettingsStore:
    def __init__(self):
        pass
    def CheckFile(self):
        self.Changed = False
        self.SettingsPath = "../Settings/Settings.csv"
        self.SettingsContents = []
        
        if os.path.isfile(self.SettingsPath) != True:
            os.mkdir("../Settings")
            f = open(self.SettingsPath, "x")
            f.close()
            print("Installed settings")
            
        print("[DelEverything] Settings Initalizing")
        return self.Changed
        
        
    def FindValue(self, RowName, data):
        found = None
        with open(self.SettingsPath, "w") as SettingsF:
            SettingsFWriter = csv.reader(SettingsF)
            for row in SettingsFWriter:
                if row[0] == RowName:
                    found = row[1]
                    if found != data:
                        found = None
                        continue
                    else:
                        print("[DelEverything] Found Data")
                        break
            if found == None:
                print("[DelEverything] Data doesn't exist")
        
        return found
    
    def WriteValue(self, dataOne, dataTwo):
        written = False
        with open(self.SettingsPath, "w") as SettingsF:
            SettingsFWriter = csv.writer(SettingsF)
            
            SettingsFWriter.writerow(["VirusTotal", dataOne])
            SettingsFWriter.writerow(["ProcessesScan", dataTwo])
            
            written = True
            self.Changed = True
        if written == False:
            print("[DelEverything] Data doesn't exist")
        return self.Changed
    
    def GetAllData(self):
        if self.Changed == False:
            return self.SettingsContents
        else:
            FreshNewData = self.CheckFile()
            return FreshNewData