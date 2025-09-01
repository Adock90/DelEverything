import requests
import json
import hashlib
import os
from cryptography.fernet import Fernet
import DelEverythingHash

def LoadKey(password=''):
    hashObj = hashlib.sha256()
    try:
        hashObj.update(password)
        hashObj.digest()
        hashObj.hexdigest()
    except:
        print("Hash Error")
    
    with open("VTKey.key", "rb") as VTKey:
        content = VTKey.read()
        
        key = Fernet(hashObj)
        Decrypted = key.decrypt(content)
        
    
    return Decrypted


class VirusTotalCheck:
    def __init__(self, Password, Path):
        self.score = 0
        self.Path = Path
        self.APIKey = LoadKey(Password)
        self.Link = "https://www.virustotal.com/api/v3/"
        self.headers = {
            "x-apikey": self.APIKey,
            "User-Agent": "vtscan v.1.0",
            "Accept-Encoding": "gzip, deflate"
        }
    
    def SendToVT(self):
        self.hashFile = DelEverythingHash.HashChecker.FileHash(self.Path, "sha256")
        res = requests.get(self.Link+"files/"+self.hashFile)
        
        statCode = res.status_code
        
        if statCode == 200:
            result = res.json()
            stats = result.get("data").get("attributes").get("last_analysis_results")
            if stats:
                results = stats
                for i in results:
                    place = results[i].get("category")
                    if place == "malicous":
                        self.score += 15
        else:
            print("Failed to connect")